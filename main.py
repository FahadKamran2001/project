import pandas as pd
import numpy as np
import subprocess
import dvc
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 
from mlflow.models import infer_signature
import mlflow.sklearn, mlflow
from mlflow import MlflowClient
from preprocess import preprocess_data

def load_data():
    # Load the data from the csv file function
    data = pd.read_csv('dummy_sensor_data.csv')
    return data

def start():
    print("Simulate Sensor Data Generation? (y/n)")
    choice = 'n'
    if choice == 'y' :
        subprocess.call(['python', 'generate_data.py'])
    else:
        print("Skipping data generation...")
    #Loading the data
    print("*****Loading data*****")
    initial_data = load_data()
    print(initial_data.head())
    
    #Preprocessing the data
    print("*****Preprocessing the data*****")
    processed_data = preprocess_data(initial_data)
    print(processed_data.head())
    processed_data.to_csv('processed_data.csv', index=False)
    
    #Splitting the data into train and test
    print("*****Splitting the data into train and test*****")
    # Split the dataset into features (X) and target variable (y)
    X = processed_data.drop(['Timestamp', 'Reading'], axis=1)
    y = processed_data['Reading']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("*****Starting MLFlow Run*****")
    # Set the artifact_path to location where experiment artifacts will be saved
    artifact_path = "model"
    # Set the run name to identify the experiment run
    #run_name = "project"
    # Connecting to the MLflow server
    client = MlflowClient(tracking_uri="https://dagshub.com/FahadKamran2001/project.mlflow")
    mlflow.set_tracking_uri("https://dagshub.com/FahadKamran2001/project.mlflow")
    random_forest_experiment = mlflow.set_experiment("project")
    
    mlflow.sklearn.autolog()
    # Initiate a run, setting the `run_name` parameter
    with mlflow.start_run():#run_name=run_name) as run:
        
        print("*****Training the model*****")
        # Defining the parameters for the model 
        params = {"n_estimators": 100, "random_state": 42, "max_depth": 5}
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [3, 5, 10, None] 
        }
        # rf = RandomForestRegressor(**params)
        rf = GridSearchCV(RandomForestRegressor(), param_grid, cv=5, scoring='r2')
        # Train the model
        rf.fit(X_train, y_train)

        print("*****Evaluating the model*****")
        # Make predictions on the test set
        y_pred = rf.predict(X_test)        
        signature = infer_signature(X_test, y_pred)
        # Evaluate the model using mean squared error
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mse)
        score = rf.best_score_
        print(f"Evaluation Errors: MSE[{mse}], MAE[{mae}], R2[{r2}], RMSE[{rmse}]")
        mlflow_metrics = {
            "mse": mse,
            "mae": mae,
            "r2": r2,
            "rmse": rmse,
            "score": score
        }
        # Log the parameters usend for the model fit
        # mlflow.log_params(params)
        # Log the error metrics that were calculated during validation
        mlflow.log_metrics(mlflow_metrics)
        # Log an instance of the trained model for later use
        mlflow.sklearn.log_model(sk_model=rf, input_example=X_test, artifact_path=artifact_path)
    
    print("*****Deploy Best Model*****")
    print("Do you want to deploy the best model? (y/n)")
    choice = 'y'
    if choice != 'n':
        print("Deploying the best model")
        best_model = rf.best_estimator_
        best_params = rf.best_params_
        # Get the best model from the MLflow experiment
        best_run = client.search_runs(
            experiment_ids=random_forest_experiment.experiment_id,
            order_by=["metrics.training_mse ASC"],
            max_results=1,
        )[0]
        print("Best Run:", best_run.info.run_id)
        # Clear app/best_model folder if it exists
        subprocess.call(['rm', '-rf', 'app/best_model'])
        # Saving the best model, overwriting the previous best model
        # saving best_run as a pickle file
        mlflow.sklearn.save_model(best_model, "app/best_model")
        # Register the best model with MLflow
        mlflow.sklearn.log_model(
            sk_model=best_model,
            artifact_path="sklearn-model",
            signature= signature,
            registered_model_name="random-forest-best",
        )
        print("Model deployed successfully!")
    else:
        print("Skipping model deployment")
if __name__ == '__main__':
    start()
    
