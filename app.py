# app.py

from Sentinel.utils.logger import error_logger

if __name__ == "__main__":
    try:
        # Your main application logic here
        pass
    except Exception as e:
        error_logger.error(f"An error occurred: {e}")