import logging
import logging.handlers
import config
import time

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
rf_handler = logging.handlers.TimedRotatingFileHandler('./log/' + config.BasicConfig.ALL_LOG_FILE_NAME, when='midnight', interval=1, backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
f_handler = logging.FileHandler('./log/' + config.BasicConfig.ERROR_LOG_FILE_NAME)
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(f_handler)
logger.addHandler(rf_handler)

def log(message,level="info"):
    if level == "debug":
        logger.debug(message)
    elif level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)

def init_log():
    with open('./log/'+config.BasicConfig.ALL_LOG_FILE_NAME, "a+") as f_all:
        f_all.truncate(0)
    f_all.close()
    with open('./log/'+config.BasicConfig.ERROR_LOG_FILE_NAME, "a+") as f_error:
        f_error.truncate(0)
    f_error.close()

def read_eslworking_log_file(esl_id):
    timeout = time.time() + 60*5
    try:
        with open(config.BasicConfig.ESLWORKING_LOG_PATH) as f:
            f.seek(0,2)
            while True:
                line = f.readline()
                if "category=esl,action=esl_update_finished,user_code=%s.%s,eslid=%s,status=online" % (config.ConnectionConfig.CUSTOMER_CODE, config.ConnectionConfig.STORE_CODE, esl_id) in line or time.time() > timeout:
                    print(line)
                    break
                time.sleep(1)
    except Exception as e:
        print(e)