from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import os

app = Flask(__name__)

model = None
data = None

# Endpoint to upload the CSV file
@app.route('/upload', methods=['POST'])
def upload_file():
    global data
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    data = pd.read_csv(file)
    return "File uploaded successfully", 200

# Endpoint to train the model
@app.route('/train', methods=['POST'])
def train_model():
    global model, data
    if data is None:
        return "No data uploaded", 400

    X = data[['Temperature', 'Run_Time']]
    y = data['Downtime_Flag']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model_choice = request.json.get('model', 'logistic_regression')
    if model_choice == 'logistic_regression':
        model = LogisticRegression()
    else:
        model = DecisionTreeClassifier()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return jsonify({"accuracy": accuracy, "f1_score": f1})

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return "Model not trained", 400
    input_data = request.json
    temperature = input_data['Temperature']
    run_time = input_data['Run_Time']
    prediction = model.predict([[temperature, run_time]])
    probability = model.predict_proba([[temperature, run_time]])[0].max()

    downtime = "Yes" if prediction[0] == 1 else "No"
    return jsonify({"Downtime": downtime, "Confidence": round(probability, 2)})

if __name__ == '__main__':
    app.run(debug=True)
