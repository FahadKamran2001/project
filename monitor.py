import mlflow
from mlflow import MlflowClient, pyfunc
import subprocess
import pandas as pd
from preprocess import preprocess_data
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 

def fetch_model():
    model_name = "random-forest-best"
    client = MlflowClient(tracking_uri="https://dagshub.com/FahadKamran2001/project.mlflow")
    mlflow.set_tracking_uri("https://dagshub.com/FahadKamran2001/project.mlflow")
    model_metadata = client.get_latest_versions(model_name, stages=["None"])
    latest_model_version = model_metadata[0].version
    #print(latest_model_version)
    
    # Load the model as a PyFuncModel.
    model = pyfunc.load_model(f"models:/{model_name}/{latest_model_version}")
    return model

def fetch_data(data_file_path = 'dummy_sensor_data.csv'): 
    data = pd.read_csv(data_file_path)
    data = preprocess_data(data)
    return data

def save_metrics(mae, r2, mse):
    #print("Saving metrics for future analysis...")
    # Generate a pd dataframe to store the metrics
    metrics = pd.DataFrame(columns=['MAE', 'R2', 'MSE'])
    # Add the metrics to the dataframe
    metrics.loc[0] = [mae, r2, mse]
    # if metrics.csv does not exist, create it, else append the metrics to it
    try:
        existing_metrics = pd.read_csv('metrics.csv')
        updated_metrics = pd.concat([existing_metrics, metrics], ignore_index=True)
        updated_metrics.to_csv('metrics.csv', index=False)
    except FileNotFoundError:
        metrics.to_csv('metrics.csv', index=False)
    
def monitor_model():
    #Get the latest model from mlflow
    model = fetch_model()
    #Get the latest data from the data file
    data = fetch_data()
    #Evaluate model performance on the latest data
    predictions = model.predict(data)
    #Calculate error metrics
    mae = mean_absolute_error(data['Reading'], predictions)
    r2 = r2_score(data['Reading'], predictions)
    mse = mean_squared_error(data['Reading'], predictions)
    #print("Model error metrics: MAE:[{}], R2:[{}], MSE:[{}]".format(mae, r2, mse))
    save_metrics(mae, r2, mse)
    # Compare error metrics with threshold
    #if mae > 16 or mse > 500:
    #print("Model performance degraded! Retraining model.")
    print("true")
    #print(f"::set-output name=condition_result::{str(text).lower()}")

    
if __name__ == '__main__':
    monitor_model()
    
