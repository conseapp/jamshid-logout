from utils.context_manager import RedisConnection
from utils.common import RedisConnectioKeys
from utils.config import logger
from fastapi import HTTPException



async def logout(user_id: str, token: str, redis_credentials: RedisConnectioKeys):
    with RedisConnection(**redis_credentials, retries=3) as rd:
        key = f"jwt-{user_id}"
        if rd.exists(key):
            if rd.get(key) == token:
                # rd.delete(key)
                logger.info(f'The key "{key}" has been successfully removed from Redis.')
                logger.info(f"user {user_id} logged out")
                return "done"
            else:
                logger.error(f"logout failed, invalid token for user {user_id}")
                return "invalid token"

        else:
            logger.error(f"logout failed, user {user_id} already logged out")
            return "invalid user_id"
