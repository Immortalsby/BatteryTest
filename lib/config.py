''' configuration '''
import random

class BasicConfig():
    INIT_LOG = True # Initialize log everytime when launch the script
    INIT_COUNT = True # Initialize count file everytime when launch the script
    INIT_STORE_CONFIG = True # Send store config everytime when launch the script
    COUNT_FILE_NAME = "TEST_COUNT"
    ESLINFO_FILE_NAME = "ESL_INFO"
    ALL_LOG_FILE_NAME = "Hanshow_Battery_Test_All.log"
    ERROR_LOG_FILE_NAME = "error.log"
    ESLWORKING_LOG_PATH = "S:\\tomcat\\eslworking-3.0.4\\log\\eslworking.log"  # IMPORTANT!
    DEFAULT_PRODUCT_NAME = "Test product"
    MAX_BIND_TIME = 3
    MAX_UNBIND_TIME = 4
    MAX_UPDATE_PRICE = 10
    MAX_UPDATE_STOCK = 500
    MAX_FLASH_TIME = 18
    MAX_SWITCH_PAGE = 3650
    SWITCH_PAGE_DURATION = 10

class StoreConfig():
    storeConfig =  {
            "magnet_actions": [
                "flash_light"
            ],
            # "switch_page": {
            #     "page_id": 1,
            #     "stay_time": 10
            # },
            "flash_light": {
                "colors": [
                "red"
            ],
                "on_time": 7,
                "off_time": 27,
                "sleep_time": 27,
                "loop_count": 30
        }
    }

class ConnectionConfig():
    URL = "http://127.0.0.1"
    PORT = "9000" # eslworking port
    CUSTOMER_CODE = "handy"
    STORE_CODE = "handy"
    URL_FULL = URL + ":" + PORT + "/api3/" + CUSTOMER_CODE + "." + STORE_CODE

DATA_TEMPLATE = {
                "esl_id": "",
                "sid": "398479930002" + str(random.randint(0,9999)),
                "back_url": "http://127.0.0.1:8000/restful/callback",
                "template": "_UNBIND",
                "item_name": "unbind"
}

DATA_UNBIND = {
                "sid": "398479930002" + str(random.randint(0,9999)),
                "priority":10,
                "template": "",
                "back_url": "http://127.0.0.1:8000/restful/callback",
                "force_update":'true',
                "screen":{
                    "name":"",
                    "args": {
                        "price1": "",
                        "itemName": "",
                        "price2Description": "",
    		            "price1Description": ""
                    }
                }
}


''' end of config '''