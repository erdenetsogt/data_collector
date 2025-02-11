# data_collector/database.py
import mysql.connector
from config import DB_CONFIG
import logging

class Database:
    def __init__(self):
        self.config = DB_CONFIG
        self.logger = logging.getLogger(__name__)

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            self.logger.error(f"Database connection error: {str(e)}")
            return False

    def disconnect(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def insert_data(self, data):
        try:
            sql = "INSERT INTO your_table (timestamp, data) VALUES (NOW(), %s)"
            self.cursor.execute(sql, (data,))
            self.connection.commit()
            return True
        except Exception as e:
            self.logger.error(f"Data insertion error: {str(e)}")
            return False