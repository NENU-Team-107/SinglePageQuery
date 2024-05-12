# Single Page Query Application

[中文文档](./README-zh.md)

## Run

### Linux

1. download the python 3.11 or higher version

2. open the powershell to run command followed(only run in your first startup):
    ```bash
    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    ```

3. run command `python app.py` to run the service

4. open the browers with url `localhost:8080`



### Windows

1. download the python 3.11 or higher version

2. open the powershell to run command followed(only run in your first startup):
    ```bash
    python -m venv .venv
    . .venv/bin/Activate.ps1
    pip install -r requirements.txt
    ```

3. run command `python app.py` to run the service

4. open the browers with url `localhost:8080`

## Usage

If you want to update or create a new table or dbffile, please move the file into `data` folder and restart the servcie.
