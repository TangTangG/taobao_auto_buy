import os
import json
import logging

def read(config_path):
    with open(config_path, "r") as f:
        return json.load(f)

def welcome(message, url, time):
    logging.basicConfig(level = logging.INFO)
    logging.info(message)
    logging.info(f"商品链接为 : {url}")
    logging.info(f"抢购时间为 : {time}")
