# data_collector/collector.py
from apscheduler.schedulers.blocking import BlockingScheduler
from database import Database
from logger import setup_logger
import time

class DataCollector:
    def __init__(self):
        self.logger = setup_logger()
        self.db = Database()
        self.scheduler = BlockingScheduler()

    def collect_data(self):
        """Энд өөрийн хүссэн логик бичнэ"""
        # Жишээ нь системийн мэдээлэл цуглуулах
        import psutil
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        return f"CPU: {cpu_percent}%, Memory: {memory}%"

    def job(self):
        if not self.db.connect():
            self.logger.error("Could not connect to database")
            return

        try:
            data = self.collect_data()
            if self.db.insert_data(data):
                self.logger.info(f"Successfully inserted data: {data}")
            else:
                self.logger.error("Failed to insert data")
        finally:
            self.db.disconnect()

    def start(self):
        self.logger.info("Starting data collector...")
        self.scheduler.add_job(self.job, 'interval', minutes=1)
        
        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            self.logger.info("Stopping data collector...")