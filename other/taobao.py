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
from selenium.webdriver.common.action_chains import ActionChains

class TaoBao(object):

    num_instance = 0

    def __init__(self, config):

        self.browser = self.config_browser()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser,20)
        
        self.main_url = config["main_url"]      
        self.target_url = config["target_url"]
        self.buy_time = config["buy_time"]
        
        self.is_market = "chaoshi" in self.target_url

    def click_until_redirect(self, element, current_url):

        while current_url == self.browser.current_url:
            try:
                element.click()
            except:
                pass

    def login(self):

        self.browser.get(self.main_url)
        self.browser.find_element_by_link_text("亲，请登录").click()
        current_url = self.browser.current_url
        self.wait_redirect(current_url)


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

    
    def wait_until_load(self, selector_text):

        self.wait.until(EC.presence_of_all_elements_located(By.XPATH, selector_text))

    def buy(self):

        current_url = self.browser.current_url
        buy_element = self.browser.find_element_by_id("J_LinkBuy")
        self.click_until_redirect(buy_element, current_url)

        self.checkout()
    
    def buy_market(self):

        current_url = self.browser.current_url
        arrow = self.browser.find_element_by_xpath("//div[@class='tm-mcRoot']//s[@class='arrow']")
        ActionChains(self.browser).move_to_element(arrow)
        self.wait_until_load("//a[@data-tmc='cart' and @class='tm-mcCartBtn']")

        element = self.browser.find_element_by_xpath("//a[@data-tmc='cart' and @class='tm-mcCartBtn']")
        self.click_until_redirect(element, current_url)

        self.checkout_market()

    def checkout(self):

        current_url = self.browser.current_url

        sumit_element = self.browser.find_element_by_id("submitOrderPC_1").find_element_by_xpath(".//a[@role='button']")
        self.click_until_redirect(sumit_element, current_url)

    def checkout_market(self):

        current_url = self.browser.current_url
        checkout_element = self.browser.find_element_by_id("J_Go")
        self.click_until_redirect(checkout_element, current_url)

    @classmethod
    def count(cls):
        
        return cls.num_instance

    def wait_for_shop(self):
        
       while 1:

           now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
           Tools.time_distance(now, self.buy_time)
           if now > self.buy_time:
                self.buy()
            
    def start(self):

        logging.info(f"Start")
        self.login()
        self.goto_detail()
        self.wait_for_shop()
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