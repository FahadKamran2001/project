# Project README
[<img src="https://github.com/{{ FahadKamran2001 }}.png" width="60px;"/><br /><sub><ahref="https://github.com/{{ FahadKamran2001 }}">{{ FahadKamran2001 }}</a></sub>](https://github.com/{{ FahadKamran2001 }}/{{ project }}
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

[requirements.txt](https://github.com/FahadKamran2001/project/blob/main/requirements.txt)

## Workflow
-The workflow consists of the the automatic DVC setup, Concept Drift Checking, and Auto Retrain & Deployment
[project-execution.yml](https://github.com/FahadKamran2001/project/blob/main/.github/workflows/project-execution.yml)

## Preprocessing Function
[preprocess.py](https://github.com/FahadKamran2001/project/blob/main/preprocess.py)

## Retraining Code
[main.py](https://github.com/FahadKamran2001/project/blob/main/main.py)

## Tasks Implementation
[task.txt](https://github.com/FahadKamran2001/project/blob/main/tasks.txt)






 
