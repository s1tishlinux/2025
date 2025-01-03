import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Initialize MLflow tracking
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("my_experiment")

# Load data
data = pd.read_csv("data/dataset.csv")  # Update with your dataset path
X = data.drop("target", axis=1)
y = data["target"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
with mlflow.start_run():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Log parameters
    mlflow.log_param("n_estimators", model.n_estimators)
    mlflow.log_param("max_depth", model.max_depth)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    mlflow.log_metric("accuracy", accuracy)

    # Log the model
    mlflow.sklearn.log_model(model, "model")

print("Model training and logging completed.")