from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import JSONResponse
from utils.redis import logout as redis_logout
from utils.common import is_valid_token
from dotenv import load_dotenv
import logging
import requests
import os

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://jamshid.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_credentials = {
    'host': 'localhost',
    'port': 6379,
    'password': os.getenv('REDIS_PASSWORD')
}


@app.post("/logout")
async def logout(user_id: str, token: str = Header(...)):
    """
    :description: logout user<br>
    :param user_id: user id<br>
    :param token: jwt token <br>
    :return: set user logout<br>
    """
    print(user_id)
    try:
        _, received_token = token.split()
    except Exception as err:
        return "Invalid Input: " + str(err)

    # authentication = await is_valid_token(received_token)
    authentication = True
    if authentication is True:
        await redis_logout(user_id=user_id, token=received_token, redis_credentials=redis_credentials)
        return JSONResponse(f"user {user_id} logged out successfully", status_code=200)

    else:
        raise HTTPException(status_code=401, detail="Invalid token")
