import logging
import datetime
import time
from utils import Tools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random

class TaoBao(object):

    num_instance = 0

    def __init__(self, config):

        self.browser = self.config_browser()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser,20)
        
        self.main_url = config["main_url"]      
        self.target_url = config["target_url"]
        self.amount_to_buy = config["amount_to_buy"];
        self.plan_to_buy = config["plan_to_buy"];
        self.prop_check_list = config["prop_check_list"]
        self.buy_time = config["buy_time"]
        
        self.table = None

    def login(self):

        self.browser.get(self.main_url)
        self.browser.find_element_by_link_text("亲，请登录").click()
        current_url = self.browser.current_url
        self.wait_redirect(current_url)

    def start(self):

        logging.info(f"Start")
        self.login()
        self.goto_detail()
        self.get_table()
        if self.table is not None:
            # self.input_form()
            self.wait_for_shop()
        else:
            logging.error(f"error: -> can't get table")
            self.close()

    def get_table(self):

        self.table = self.browser.find_element_by_xpath("//div[@class='tb-sku']")
        
    def wait_redirect(self, current_url):

        try:
            self.wait.until(lambda browser: browser.current_url != current_url)
        except TimeoutException:
            logging.warning(f"Timeout")

    def config_browser(self):

        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        #opts.add_experimental_option("prefs", {"profile.managed_default_content_settings.images":2})
        driver_dir = Tools.get_driver_dir()
        return Chrome(driver_dir, chrome_options=opts)

    def goto_detail(self):

        self.browser.get(self.target_url)

    # def prop_check(self, table):
        
    #     props = table.find_elements_by_xpath("./dl[contains(@class, 'tm-sale-prop') or contains(@class, 'tm-relate-wrapper')]")
    #     for i in props:
    #         print(i.get_attribute("class"))

    #     print(f"props: {len(props)}")
    #     print(f"list: {self.prop_check_list}")
    #     assert len(props) == len(self.prop_check_list)
    #     logging.info("working right")

    #     for i in zip(props, self.prop_check_list):
    #         i[0].find_elements_by_xpath(".//li")[i[1]].click()

    # def amount_check(self, table):

    #     amount = table.find_element_by_xpath("./dl[contains(@class, 'tb-amount')]").find_element_by_xpath(".//input[@type='text']")
    #     amount.send_keys(Keys.CONTROL + "a")
    #     amount.send_keys(Keys.DELETE)
    #     amount.send_keys(self.amount_to_buy)

    # def plan_check(self, table):
        
    #     if self.plan_to_buy is None:
    #         pass
    #     else:
    #         plans = table.find_element_by_id("J_Progressive")
    #         plans.find_elements_by_xpath(".//li")[self.plan_to_buy].click()



    # def input_form(self):

    #     self.prop_check(self.table)
    #     self.amount_check(self.table)
    #     self.plan_check(self.table)
        
    def wait_until_load(self, selector_text):

        self.wait.until(EC.presence_of_all_elements_located(By.XPATH, selector_text))

    def buy(self):

        

        current_url = self.browser.current_url
        #self.wait_redirect(current_url)

        while current_url == self.browser.current_url:
            try:
                self.table.find_element_by_id("J_LinkBuy").click()
            except:
                pass
            time.sleep(random.randrange(0, 0.5))

        self.sumit_order() 

    def sumit_order(self):

        current_url = self.browser.current_url

        while current_url == self.browser.current_url:
            try:
                self.browser.find_element_by_id("submitOrderPC_1").find_element_by_xpath(".//a[@role='button']").click()
            except:
                pass

            time.sleep(random.randrange(0, 0.5))
    @classmethod
    def count(cls):
        
        return cls.num_instance

    def wait_for_shop(self):
        
       while 1:
           now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
           Tools.time_distance(now, self.buy_time)
           if now > self.buy_time:
                self.buy()
            
    def close(self):
        self.browser.close()

def main():

    logging.basicConfig(level=logging.INFO)
    config = Tools.load_config_json()

    if config is not None:
        taobao = TaoBao(config)
        taobao.start()
    else:
        logging.warning("please input info to config.json")

if __name__ == "__main__":
    main() 