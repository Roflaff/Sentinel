import logging
from datetime import datetime
import os
from zoneinfo import ZoneInfo

def setup_logger(log_path: str = "logs/upload_error.log") -> logging.Logger:
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger("error_logger")
    logger.setLevel(logging.WARNING)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_path, encoding='utf-8')

        class KSTFormatter(logging.Formatter):
            def converter(self, timestamp):
                dt = datetime.fromtimestamp(timestamp, ZoneInfo("Asia/Seoul"))
                return dt.timetuple()

        formatter = KSTFormatter(
            '[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

error_logger = setup_logger("./logs/error.log")
