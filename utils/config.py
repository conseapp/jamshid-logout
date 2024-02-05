import logging

logger = logging.getLogger('jamshid-logout')
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(format)

logger.addHandler(file_handler)
