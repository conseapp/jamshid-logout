from utils.context_manager import RedisConnection
from utils.common import RedisConnectioKeys
import logging


def logout(user_id: str, token: str, redis_credentials: RedisConnectioKeys):
    with RedisConnection(**redis_credentials, retries=3) as rd:
        key = f"jwt-{user_id}"
        if rd.exists(key) and rd.get(key) == token:
            # rd.delete(key)
            logging.info(f'The key "{key}" has been successfully removed from Redis.')
            logging.info(f"user {user_id} logged out")
            return True
        else:
            logging.error(f"logout failed, user {user_id} already logged out")
            return False

    # logging.warning(f"redis connection failed: {err}")
    # raise HTTPException(status_code=400, detail=f"redis connection failed: {err}")
