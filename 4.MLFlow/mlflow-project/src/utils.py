def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Add preprocessing steps here
    return data

def log_metrics(metrics):
    import mlflow
    for key, value in metrics.items():
        mlflow.log_metric(key, value)

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import accuracy_score
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)