# data_collector/config.py
import os

# Өгөгдлийн сангийн тохиргоо
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

# Log файлын зам
LOG_DIR = '/var/log/data_collector'
LOG_FILE = os.path.join(LOG_DIR, 'data_collector.log')
