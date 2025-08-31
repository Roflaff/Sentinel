import logging
from datetime import datetime
import os
from zoneinfo import ZoneInfo

def setup_logger(log_filename: str = "error.log") -> logging.Logger:
    # 현재 파일 (logger.py) 위치 기준 → Sentinel/utils
    current_file_dir = os.path.dirname(os.path.abspath(__file__))

    # Sentinel/utils → Sentinel → 상위로 올라가면 프로젝트 루트
    project_root = os.path.dirname(os.path.dirname(current_file_dir))

    # logs 디렉토리 (프로젝트 루트/logs)
    log_dir = os.path.join(project_root, "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, log_filename)

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


error_logger = setup_logger("error.log")
