import pandas as pd

def preprocess_data(data):
    # removing the null values
    data = data.dropna()
    # removing the duplicates
    data = data.drop_duplicates()
    data = pd.get_dummies(data, columns=['Machine_ID', 'Sensor_ID'])
    # data horizontal enhancement
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data['Hour'] = data['Timestamp'].dt.hour
    data['DayOfWeek'] = data['Timestamp'].dt.dayofweek
    data['Month'] = data['Timestamp'].dt.month
    return data
