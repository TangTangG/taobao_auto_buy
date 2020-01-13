import platform
import os
import json
import sys
from dateutil import parser as date_parse
from functools import wraps

if "logging" not in sys.modules:
    print("can't use module logging")
else:
    import logging
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG) 

class Tools(object):

    base_config_json = {
                            "main_url" : "https://www.taobao.com/",
                            "target_url" : "https://detail.tmall.com/item.htm?spm=a1z10.4-b-s.w4007-21704868460.13.2d2d4d36ktntw0&id=607814862914",
                            "amount_to_buy" : 1,
                            "plan_to_buy" : None,
                            "prop_check_list" : [1, 2, 3],
                            "buy_time" : "2020-01-08 10:27:23", 
                       }

    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    

    @staticmethod
    def get_driver_dir():
        
        os_type = platform.system()
        drivers_dir = os.path.join(Tools.base_dir, "drivers")

        if os_type == "Linux":
            return os.path.join(drivers_dir, "chromedriver")
        elif os_type == "Darwin":
            return os.path.join(drivers_dir, "chromedriver_mac64")
        elif os_type == "Windows":
            return os.path.join(drivers_dir, "chromedriver_win32.exe")

        return None

    @staticmethod
    def load_config_json():

        config_json_dir = os.path.join(Tools.base_dir, "config.json") 

        if os.path.isfile(config_json_dir) and os.access(config_json_dir, os.R_OK):
            with open(config_json_dir, "r") as f:
                config = json.load(f)
            return config
        else:
            logging.warning(f"config file not existed or could not access it")
            logging.info(f"create default config.json")
            Tools.create_template_config_json(config_json_dir)
            return None
            
    @staticmethod
    def create_template_config_json(file_path: str) -> None:

        with open(file_path, "w") as f:
            json.dump(Tools.base_config_json, f, indent = 4)

    @staticmethod
    def time_distance(current: str, target: str):
        logging.info(f"{date_parse.parse(target) - date_parse.parse(current)}")

class do_until_redirect(object):

    def __init__(self, original_url, browser):

        self.original_url = original_url
        self.browser = browser    

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            while self.original_url:
                try:
                    result = func(*args, **kwargs)
                    return result
                except:
                    pass

        return wrapper