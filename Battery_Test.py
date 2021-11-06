from lib import config as config
from lib import func as func
from lib import log as log
import progressbar
import time

def main():
    # Init Log File
    if config.BasicConfig.INIT_LOG == True:
        print("\nInitialize Log File...\n")
        log.init_log()
    # Init count file
    if config.BasicConfig.INIT_COUNT == True:
        print("Initialize Count File...\n")
        func.init_count()
    unbind_time = config.BasicConfig.MAX_UNBIND_TIME
    if config.BasicConfig.MAX_UNBIND_TIME > 0 or config.BasicConfig.MAX_BIND_TIME > 0:
        print("\n----------\nStarting Binding & Unbinding Process\n----------\n")
        log.log("----------Starting Binding & Unbinding Process----------")
        with progressbar.ProgressBar(max_value=
            config.BasicConfig.MAX_BIND_TIME + unbind_time 
            if unbind_time < config.BasicConfig.MAX_BIND_TIME 
            else 
            config.BasicConfig.MAX_BIND_TIME *2) as bar_bind:
            percentage = 0
            bar_bind.update(percentage)
            for i in range(config.BasicConfig.MAX_BIND_TIME):
                if unbind_time > 0:
                    unbind_time -= 1
                    #print("\nUnbinding...")
                    func.unbind()
                    time.sleep(0.2)
                    percentage += 1
                    bar_bind.update(percentage)
                #print("\nBinding...")
                func.bindUpgrade("bind")
                time.sleep(0.2)
                percentage += 1
                bar_bind.update(percentage)
    if config.BasicConfig.MAX_UPDATE_PRICE > 0:
        print("\n----------\nStarting Price Update Process\n----------\n")
        log.log("----------Starting Price Update Process----------")
        with progressbar.ProgressBar(max_value=
            config.BasicConfig.MAX_UPDATE_PRICE + unbind_time 
            if unbind_time > 0 else 
            config.BasicConfig.MAX_UPDATE_PRICE) as bar_bind:
            percentage = 0
            for i in range(config.BasicConfig.MAX_UPDATE_PRICE):
                if unbind_time > 0:
                    unbind_time -= 1
                    #print("\nUnbinding...")
                    func.unbind()
                    time.sleep(0.2)
                    bar_bind.update(percentage)
                    percentage += 1
                #print("\nBinding...")
                func.bindUpgrade("price")
                time.sleep(0.2)
                bar_bind.update(percentage)
                percentage += 1
    if config.BasicConfig.MAX_UPDATE_STOCK > 0:
        print("\n----------\nStarting Stock Update Process\n----------\n")
        log.log("----------Starting Stock Update Process----------")
        with progressbar.ProgressBar(max_value=
            config.BasicConfig.MAX_UPDATE_STOCK + unbind_time 
            if unbind_time > 0 else 
            config.BasicConfig.MAX_UPDATE_STOCK) as bar_bind:
            percentage = 0
            for i in range(config.BasicConfig.MAX_UPDATE_STOCK):
                if unbind_time > 0:
                    unbind_time -= 1
                    #print("\nUnbinding...")
                    func.unbind()
                    time.sleep(0.2)
                    bar_bind.update(percentage)
                    percentage += 1
                #print("\nBinding...")
                func.bindUpgrade("stock")
                time.sleep(0.2)
                bar_bind.update(percentage)
                percentage += 1
    if config.BasicConfig.INIT_STORE_CONFIG == True:
        print("\n----------\nStarting Sending Store Config\n----------\n")
        log.log("----------Starting Sending Store Config----------")
        func.control("store_config")
        for i in progressbar.progressbar(range(100)):
            time.sleep(0.02)
    if config.BasicConfig.MAX_FLASH_TIME > 0:
        print("\n----------\nStarting Flash Process\n----------\n")
        log.log("----------Starting Flash Process----------")
        with progressbar.ProgressBar(max_value=
            config.BasicConfig.MAX_FLASH_TIME + unbind_time 
            if unbind_time > 0 else 
            config.BasicConfig.MAX_FLASH_TIME) as bar_bind:
            percentage = 0
            for i in range(config.BasicConfig.MAX_FLASH_TIME):
                if unbind_time > 0:
                    unbind_time -= 1
                    #print("\nUnbinding...")
                    func.unbind()
                    time.sleep(0.2)
                    bar_bind.update(percentage)
                    percentage += 1
                #print("\nBinding...")
                func.control("flash")
                time.sleep(0.2)
                bar_bind.update(percentage)
                percentage += 1
    if config.BasicConfig.MAX_SWITCH_PAGE > 0:
        print("\n----------\nStarting Page Change Process\n----------\n")
        log.log("----------Starting page Change Process----------")
        with progressbar.ProgressBar(max_value=
            config.BasicConfig.MAX_SWITCH_PAGE + unbind_time 
            if unbind_time > 0 else 
            config.BasicConfig.MAX_SWITCH_PAGE) as bar_bind:
            percentage = 0
            for i in range(config.BasicConfig.MAX_SWITCH_PAGE):
                if unbind_time > 0:
                    unbind_time -= 1
                    #print("\nUnbinding...")
                    func.unbind()
                    time.sleep(0.2)
                    bar_bind.update(percentage)
                    percentage += 1
                #print("\nBinding...")
                func.control("page")
                time.sleep(0.2)
                bar_bind.update(percentage)
                percentage += 1

if __name__ == "__main__":
    main()