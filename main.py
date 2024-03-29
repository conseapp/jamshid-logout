from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import JSONResponse
from utils.redis import logout as redis_logout
from utils.common import is_valid_token, RedisConnectioKeys
from dotenv import load_dotenv
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

redis_credentials: RedisConnectioKeys = {
    'host': 'localhost',
    'port': '6379',
    'password': str(os.getenv('REDIS_PASSWORD'))
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

    authentication = await is_valid_token(received_token)
    if authentication is True:
        result = await redis_logout(user_id=user_id, token=received_token, redis_credentials=redis_credentials)
        if result == "done":
            return JSONResponse(f"user {user_id} logged out successfully", status_code=200)
        elif result == "invalid token":
            raise HTTPException(status_code=400, detail=f"logout failed, invalid token for user {user_id}")
        elif result == "invalid user_id":
            raise HTTPException(status_code=400, detail=f"logout failed, user {user_id} already logged out")

    else:
        raise HTTPException(status_code=401, detail="Invalid token")
