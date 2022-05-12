import logging
import logging.handlers

def batch_task_logger(success_count, failure_count, pass_count):
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] >> %(message)s')
    streamHandler = logging.StreamHandler()
    fileHandler = logging.FileHandler('./batch_task.log')
    streamHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)
    logger.setLevel(level=logging.DEBUG)
    logger.info(f'{success_count} rows created, {failure_count} rows failed and {pass_count} rows passed')