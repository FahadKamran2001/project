# Project README

## DVC Setup

### Install DVC on Windows

- Install the DVC Windows bit version from the [DVC website](https://dvc.org/).
- Run the setup and give it all necessary permissions.
- Add `dvc.exe` to the system's path variables in the environment variables.
- Restart your computer.
- Install the DVC VSCode extension from the [DVC website](https://dvc.org/).
- Navigate to the project directory, open VSCode there, and make sure the folder is a Git repository created by Git or GitHub Desktop.
- Open the VSCode terminal and run the following command:

    ```bash
    dvc init
    ```

- Press F1, search for "DVC: show setup," and click on it.
- If there's a green tick or warning sign next to the DVC logo, it indicates the DVC installation status.
- Run the data generator file "random_data.py" to get the data file "dummy_sensor_data.csv":

    ```bash
    python random_data.py
    ```

- If 'dummy_sensor_data.csv' is being tracked by Git, remove it with the following commands:

    ```bash
    git rm -r --cached 'dummy_sensor_data.csv'
    git commit -m "stop tracking dummy_sensor_data.csv"
    ```

- Add 'dummy_sensor_data.csv' to DVC:

    ```bash
    dvc add dummy_sensor_data.csv
    ```

- Add the Google Drive identifier to the DVC config file in the `.dvc` folder.

    ```ini
    [core]
        remote = storage
    ['remote "storage"']
        url = gdrive://1ZJZmaYaA77kOh0IdPIO************
    ```

- Save the file and commit the changes.
- Push the data to Google Drive:

    ```bash
    dvc push
    ```

- Check the DVC setup:

    ```bash
    dvc remote storage
    ```

## Requirements.txt

```plaintext
pandas==2.1.4
numpy==1.26.2
jinja2==3.1.2
flask==3.0.0
mlflow==2.9.2
scikit-learn==1.3.2
xgboost==2.0.3
dvc[gdrive]




 
