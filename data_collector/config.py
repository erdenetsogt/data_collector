# data_collector/config.py
import os

# Өгөгдлийн сангийн тохиргоо
DB_CONFIG = {
    'host': 'localhost',
    'user': 'erdene',
    'password': 'Pa55w0rd@123',
    'database': 'nodejs_prisma'
}

# Log файлын зам
LOG_DIR = '/var/log/data_collector'
LOG_FILE = os.path.join(LOG_DIR, 'data_collector.log')
