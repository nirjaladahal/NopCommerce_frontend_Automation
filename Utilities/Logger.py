import logging
import os

class Logger:
    def __init__(self, log_folder="selenium_logs", log_file="test_log.log"):
        self.log_folder = log_folder
        self.log_file = os.path.join(self.log_folder, log_file)
        self.logger = self._setup_logger()

    def _setup_logger(self):
        os.makedirs(self.log_folder, exist_ok=True)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt='%m/%d/%y %I:%M:%S %p'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger

    def get_logger(self):
        return self.logger
