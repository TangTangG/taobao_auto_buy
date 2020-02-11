import sys
import os
import argparse
import logging

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from bin.tb import Taobao
from bin.tm_market import TM_Market
from lib.utils import read, welcome
from threading import Thread

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type = str, help = "商品网站链接")
    parser.add_argument("-t", "--time", type = str, help = "抢购时间, 格式参考 2020-01-09 20:00:00")
    args = parser.parse_args()

    if args.url and args.time:
        welcome("Command Line 参数读取成功", args.url, args.time)
        config = {"target_url" : args.url, "buy_time" : args.time}
    else:
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "config/config.json"))
        configs = read(config_path)
        tasks = zip(configs["target_url"], configs["buy_time"])
        #welcome(f"Get {len(list(tasks))} tasks")


    for config in tasks:

        if "chaoshi" in config[0]:
            chaoshi = TM_Market(config[0], config[1])
            #chaoshi.start()
            welcome("Config Json 参数读取成功", config[0], config[1])
            Thread(target = chaoshi.start).start()
        else:
            taobao = Taobao(config[0], config[1])
            #taobao.start()
            welcome("Config Json 参数读取成功", config[0], config[1])
            Thread(target = taobao.start).start()

if __name__ == "__main__":
    main()
