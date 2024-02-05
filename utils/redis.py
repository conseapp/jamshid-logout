from utils.context_manager import RedisConnection
from utils.common import RedisConnectioKeys
from fastapi import HTTPException
import logging


async def logout(user_id: str, token: str, redis_credentials: RedisConnectioKeys):
    with RedisConnection(**redis_credentials, retries=3) as rd:
        key = f"jwt-{user_id}"
        if rd.exists(key):
            if rd.get(key) == token:
                # rd.delete(key)
                logging.info(f'The key "{key}" has been successfully removed from Redis.')
                logging.info(f"user {user_id} logged out")
                return True
            else:
                logging.error(f"logout failed, invalid token for user {user_id}")
                raise HTTPException(status_code=400, detail=f"logout failed, invalid token for user {user_id}")

        else:
            raise HTTPException(status_code=400, detail=f"logout failed, user {user_id} already logged out")
            logging.error(f"logout failed, user {user_id} already logged out")