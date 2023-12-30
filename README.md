# Project README
![Model Status](https://github.com/FahadKamran2001/project/actions/workflows/project-execution.yml/badge.svg)
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

## Google Auto-Authentication for Credential API

To set up Google Auto-Authentication for the credential API, follow the steps below:

1. Go to [Google Cloud Console](https://console.developers.google.com/).
2. Create a project for DVC remote connections.
3. Navigate to [Google Drive API in Cloud Marketplace](https://console.cloud.google.com/marketplace/product/google/drive.googleapis.com).
4. Enable the Google Drive API.
5. Go to [API Credentials Page](https://console.cloud.google.com/apis/credentials).
6. Select "Google Drive API" in the API selection dropdown.
7. Choose "Service Account" as the account type (select "Application Data" if prompted).
8. Click "Next."
9. In the Service ID field, enter 'gdrive-api'.
10. Add a description like 'Allows access to the Google Drive API.'
11. Click the "Create and Continue" button.
12. Click "Continue" as there is no need to grant service account access to the project.
13. Click "Done" as there is no need to provide user access to this account.
14. Go to [IAM & Admin > Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts).
15. Click on the project you created.
16. Click on the service account you just created.
17. In the "Keys" section, click "Add Key" and create a new key in JSON format.
18. Select JSON as the key type and click "Create."
19. Copy and paste the email associated with this service account. It should look like `service_account_name@project_id.iam.gserviceaccount.com` (e.g., `gdrive-api@project-409621.iam.gserviceaccount.com`).
20. Share the Google Drive folder where the DVC repository will reside with the service account email defined in the last step.
21. Open your repository locally in VSCode at the main branch.
22. Refer to the workflow file for updates on DVC.
23. Go to your repository's sections, navigate to Actions, and add the contents of `key.json` to the repository's secrets (copy-paste).
24. Name the secret (e.g., `GDRIVE_API`).
25. Add another secret for the GDrive link with a name like `GDRIVE_LINK` and paste the link, ensuring it's kept secure.
26. Add the service account email (e.g., `gdrive-api@project-409621.iam.gserviceaccount.com`) as `GDRIVE_CLIENT_ID`.

**Note:** Ensure that you keep your credentials secure, and do not expose sensitive information publicly. The secrets mentioned above should be treated with care and stored securely.

## MLFlow Remote Server Setup for GitHub

Follow these steps to set up MLFlow with a remote server on Dagshub for GitHub integration.

### Step 1: Connect with Dagshub

1. Go to [Dagshub](https://dagshub.com/).
2. Log in with your GitHub account.
3. Click the "Create+" button next to the profile icon.
4. Create a new repository, then click "Connect to Repository," and choose GitHub.
5. Authorize Dagshub with all repository access.
6. Choose the repository and click "Connect."

### Step 2: Obtain MLFlow Tracking URI

1. Click the "Remote" button on Dagshub.
2. Go to "Experiments" and copy the MLFlow tracking URI.

   Example:
   ```bash
   MLFLOW_TRACKING_URI=https://dagshub.com/FahadKamran2001/project.mlflow \
   MLFLOW_TRACKING_USERNAME=FahadKamran2001 \
   MLFLOW_TRACKING_PASSWORD=df259bdd7fb874eb28fc3d5745c2************ \
   python script.py
   ```

### Step 3: Add Secrets to GitHub Actions
Add these secrets to GitHub Actions, as they are used in the 'project-execution.yaml' file.

Example:

```bash
Copy code
export MLFLOW_TRACKING_URI=https://dagshub.com/FahadKamran2001/project.mlflow
export MLFLOW_TRACKING_USERNAME=FahadKamran2001
export MLFLOW_TRACKING_PASSWORD=df259bdd7fb874eb28fc3d5745c2************
```
### Step 4: MLFlow UI Setup
1. Go to the MLFlow UI from Dagshub.
2. Create an experiment named 'project' (same as used in the code).
#### Public Access Link
Anyone can view models and experiment data using the following link:

https://dagshub.com/FahadKamran2001/project.mlflow

Note: Ensure that GitHub Actions execute 'main.py' to generate contents for the link.
This single file contains all the steps and information for setting up MLFlow with a remote server on Dagshub for GitHub.

## Docker Deployment
[Dockerfile](https://github.com/FahadKamran2001/project/blob/main/Dockerfile)
to run execute following command
```bash
docker run -p 5000:5000 fahadkamran2001/random-forest-app:latest
```

## Flask Application
[app.py](https://github.com/FahadKamran2001/project/blob/main/app.py)

## Monitoring Concept Drift
[monitor.py](https://github.com/FahadKamran2001/project/blob/main/monitor.py)










 
