# coding:utf-8
import config
import log
import time
import requests
import random
import json


def init_count():
    with open(config.BasicConfig.COUNT_FILE_NAME, "r+") as f_count:
        f_count.truncate(0)
        f_count.write("0,0,"+config.BasicConfig.DEFAULT_PRODUCT_NAME+" 1")
        log.log("Read " + config.BasicConfig.COUNT_FILE_NAME +
                ": File initalized with ---- " + "0,0,"+config.BasicConfig.DEFAULT_PRODUCT_NAME+" 1")
    f_count.close()


def read_count():
    with open(config.BasicConfig.COUNT_FILE_NAME, "r+") as f_count:
        data = f_count.read()
        data = {
            "price": int(data.strip().split(',')[0]),
            "stock": int(data.strip().split(',')[1]),
            "product": data.strip().split(',')[2]
        }
        log.log("Read " + config.BasicConfig.COUNT_FILE_NAME +
                ": File data got ---- " + str(data))
    f_count.close()
    return data


def write_count(data):
    with open(config.BasicConfig.COUNT_FILE_NAME, "r+") as f_count:
        f_count.write(str(data["price"])+"," +
                      str(data["stock"])+","+str(data["product"]))
        log.log("Write " + config.BasicConfig.COUNT_FILE_NAME + ": File data write with ---- " +
                str(data["price"])+","+str(data["stock"])+","+str(data["product"]))
    f_count.close()


def bindUpgrade_api(data, esl_id, model, message):
    url = config.ConnectionConfig.URL_FULL + '/esls/%s' % esl_id
    print("\n" + message+esl_id)
    log.log(message+esl_id)
    data = {
        "sid": "3984799300029881",
        "priority": 10,
        "template": model,
        "back_url": "http://127.0.0.1:8080/prismart/ogi/ew/httpHandler?customerCode=A001",
        "force_update": 'true',
        "screen": {
            "name": model,
            "args": {
                "price1": data["price"],
                "itemName": data["product"],
                "price1Description": data["stock"]
            }
        }
    }
    r = requests.put(url, json=data)
    if r.status_code == 200:
        log.log("Success!"+"Message:"+json.dumps(r.json()))
        print("Success!"+"Message:"+json.dumps(r.json()))
    else:
        log.log("Fail!"+"Message:"+json.dumps(r.json()))
        print("Fail!"+"Message:"+json.dumps(r.json()))


def unbind_api(esl_id):
    url = config.ConnectionConfig.URL_FULL + '/esls/bind'
    log.log("Start Unbinding Process For Esl: "+esl_id)
    print("\nStart Unbinding Process For Esl: "+esl_id)
    payload = {
        "data": [
            {
                "esl_id": esl_id,
                "sid": "398479930002" + str(random.randint(0, 9999)),
                "back_url": "http://127.0.0.1:8000/restful/callback",
                "template": "_UNBIND",
                "item_name": "unbind"
            }
        ]
    }
    r = requests.delete(url, data=json.dumps(payload))
    if r.status_code == 200:
        log.log("Success!"+"Message:"+json.dumps(r.json()))
        print("Success!"+"Message:"+json.dumps(r.json()))
    else:
        log.log("Fail!"+"Message:"+json.dumps(r.json()))
        print("Fail!"+"Message:"+json.dumps(r.json()))


def control_api(esl_id, type, model="NORMAL"):
    url = config.ConnectionConfig.URL_FULL + '/esls/control'
    if type == "flash":
        log.log("Start Flash Process For Esl: "+esl_id)
        print("\nStart Flash Process For Esl: "+esl_id)
        payload = {
            "data": [
                {
                    "esl_id": esl_id,
                    "sid": "398479930002" + str(random.randint(0, 9999)),
                    "back_url": "http://127.0.0.1:8000/restful/callback",
                    "flash_light": {
                        "colors": ["green"],
                        "on_time": 7,
                        "off_time": 27,
                        "sleep_time": 27,
                        "loop_count": 30
                    }
                }
            ]
        }
        r = requests.put(url, data=json.dumps(payload))
    elif type == "page":
        log.log("Start Page Change Process For Esl: "+esl_id)
        print("\nStart Page Change For Esl: "+esl_id)
        payload = {
            "data": [
                {
                    "esl_id": esl_id,
                    "sid": "398479930002" + str(random.randint(0, 9999)),
                    "back_url": "http://127.0.0.1:8000/restful/callback",
                    "switch_page": {
                        "page_id": 1,
                        "stay_time": 10
                    }
                }
            ]
        }
        r = requests.put(url, data=json.dumps(payload))
    elif type == "store_config":
        log.log("Start Sending Store Config For Esl: "+esl_id)
        print("\nStart Sending Store Config For Esl: "+esl_id)
        payload = {
            "data": [
                {
                    "esl_id": esl_id,
                    "sid": "398479930002" + str(random.randint(0,9999)),
                    "template": model,
                    "back_url": "http://127.0.0.1:8000/restful/callback",
                    "control": {
                        "flash_light": {
                            "colors": ["green"],
                            "on_time": 7,
                            "off_time": 27,
                            "sleep_time": 27,
                            "loop_count": 30
                        }
                    },
                    "store_config": {
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
                }
            ]
        }
        print(json.dumps(payload))
        r = requests.put(config.ConnectionConfig.URL_FULL +
                         '/esls', data=json.dumps(payload))
    if r.status_code == 200:
        log.log("Success!"+"Message:"+json.dumps(r.json()))
        print("Success!"+"Message:"+json.dumps(r.json()))
    else:
        log.log("Fail!"+"Message:"+json.dumps(r.json()))
        print("Fail!"+"Message:"+json.dumps(r.json()))


def bindUpgrade(type):
    data = read_count()
    if type == "bind":
        data["product"] = data["product"][0:-1] + \
            str(int(data["product"][-1]) + 1)
        message = "Starting Binding Process For Esl: "
    elif type == "price":
        data["price"] = data["price"] + 1
        message = "Starting Price Update Process For Esl: "
    elif type == "stock":
        data["stock"] = data["stock"] + 1
        message = "Starting Stock Update Process For Esl: "
    with open(config.BasicConfig.ESLINFO_FILE_NAME, "r+") as f_esl:
        line = f_esl.readline()
        while line:
            line = line.strip()
            esl_data = {
                "esl_id": line.strip().split(',')[0],
                "model": line.strip().split(',')[1]
            }
            bindUpgrade_api(
                data, esl_data["esl_id"], esl_data["model"], message)
            log.read_eslworking_log_file(esl_data["esl_id"])
            line = f_esl.readline()
    f_esl.close()
    write_count(data)


def unbind():
    with open(config.BasicConfig.ESLINFO_FILE_NAME, "r+") as f_esl:
        line = f_esl.readline()
        while line:
            line = line.strip()
            esl_data = {
                "esl_id": line.strip().split(',')[0],
                "model": line.strip().split(',')[1]
            }
            unbind_api(esl_data["esl_id"])
            log.read_eslworking_log_file(esl_data["esl_id"])
            line = f_esl.readline()
    f_esl.close()


def control(type):
    with open(config.BasicConfig.ESLINFO_FILE_NAME, "r+") as f_esl:
        line = f_esl.readline()
        while line:
            line = line.strip()
            esl_data = {
                "esl_id": line.strip().split(',')[0],
                "model": line.strip().split(',')[1]
            }
            if type == "flash":
                control_api(esl_data["esl_id"], "flash")
                time.sleep(80)
            elif type == "page":
                control_api(esl_data["esl_id"], "page")
                time.sleep(60+config.BasicConfig.SWITCH_PAGE_DURATION)
            elif type == "store_config":
                control_api(esl_data["esl_id"], "store_config", esl_data["model"])
                time.sleep(2)
            line = f_esl.readline()
    f_esl.close()
