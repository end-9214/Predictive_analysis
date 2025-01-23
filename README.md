# Predictive Analysis

In this Program -

* Upload a CSV file containing machine data (temperature, run time, downtime flag).
* Train a machine learning model (logistic regression or decision tree) to predict downtime based on temperature and run time.
* Make predictions on new data points to assess the likelihood of downtime.

## Requirements

* Python 3.6 or later
* Flask
* pandas
* scikit-learn
* requests (optional, only if using client-side Python code with `requests` library)

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```
## Running the Application
 1) Save the provided code (main.py) in a directory.
 2) Create a file named `requirements.txt` in the same directory with the following content:
        ```
        Flask==2.3.2
        pandas==2.0.3
        scikit-learn==1.3.0
        requests==2.31.0
        ```
 3) Open your terminal or command prompt, navigate to the directory containing the files, and run:
    ```bash
        python main.py
    ```

## For uploading CSV file -
    ```bash
        curl -X POST -F "file=@your_data.csv" [http://127.0.0.1:5000/upload](http://127.0.0.1:5000/upload)
        ```

## Training model - 
    Logistic Regression model-
```bash
        curl -X POST -H "Content-Type: application/json" -d '{}' [http://127.0.0.1:5000/train](http://127.0.0.1:5000/train)
        ```
    Decision Tree model - 
    ```bash
        curl -X POST -H "Content-Type: application/json" -d '{"model": "decision_tree"}' [http://127.0.0.1:5000/train](http://127.0.0.1:5000/train)
        ```

## Make predictions -
```bash
        curl -X POST -F "file=@your_data.csv" [http://127.0.0.1:5000/upload](http://127.0.0.1:5000/upload)
        ```