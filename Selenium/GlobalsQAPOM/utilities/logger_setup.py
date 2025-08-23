import logging
import os


def setup_test_logger(test_name: str):
    """
    Configures and returns a logger instance for a given test name,
    writing all logs to a single logfile.log.
    """
    log_dir = './logfiles'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_path = os.path.join(log_dir, "logfile.log")

    # Get a logger instance. This will retrieve the existing one if it exists.
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    # Check if the logger already has a FileHandler to prevent duplicates
    if not any(isinstance(handler, logging.FileHandler) for handler in logger.handlers):
        file_handler = logging.FileHandler(log_file_path)

        # Define the formatter for the log messages
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger