import logging
import os
from config import LOG_DIR, LOG_FILE

def setup_logger():
    # Log хавтас үүсгэх
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    # Logger тохируулах
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)