# Jamshid Logout API

Simple Api removes user id key from redis when logout function called from front-end

### Built With
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## Usage

Method = POST

api docs
* https://logout.api.jamshid.app/docs

### roles request path
```console
https://logout.api.jamshid.app/{user_id}
```

### be sure to pass jwt token as "token" in header
token example
  ```console
  Bearer <token>
  ```


## Deploy

### 1. install python environment
```console
sudo apt install python3.10-venv
```
### 2. initialize environment
```console
python3 -m venv jamshidenv
```
### 3. activate environment
```console
source jamshidenv/bin/activate
```
### 4. install requirements
```console
pip3 install -r requirements.txt
```
### 5. run
```console
uvicorn main:app --host 0.0.0.0 --port 3455
```
