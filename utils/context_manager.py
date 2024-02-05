import redis
import logging


class RedisConnection:
    def __init__(self, host, port, password, retries=1):
        self.host = host
        self.port = port
        self.password = password

    def __enter__(self):
        # Code to set up resources or perform actions before the block
        try:
            self.redis_client = redis.StrictRedis(host=self.host, port=self.port, password=self.password,
                                                  decode_responses=True)
        except Exception as err:
            print(err)
        # if self.redis_client.ping():
        #     return self.redis_client

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            logging.warning(f"redis connection failed: {exc_type}")
            logging.warning(f"redis connection failed message: {exc_value}")
        self.redis_client.close()
        return True