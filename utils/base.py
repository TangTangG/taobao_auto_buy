import logging
import platform
import os
from datetime import datetime
from taobao_auto_buy.utils.exceptions import SystemUnsupported, InvalidInputUrl, InvalidInputTime, SubClassInvaild
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchAttributeException
from selenium.webdriver import Chrome, ChromeOptions
from urllib.parse import urlparse
class AutoBuyBase(object):

    __slots__ = ["_main_url", "_target_url", "_logger", "_browser", "_buy_time"]

    def __init__(self, main_url, target_url, buy_time):

        self._main_url = main_url
        self._target_url = target_url
        self._buy_time = buy_time

        # validation
        self._validate_input()

        self._logger = self._get_logger()
        self._browser = self._config_browser()

    def __repr__(self):

        class_name = self.__class__.__name__
        return f"{class_name}"

    def _is_url(self, url):

        try:
            result = urlparse(url)
            return True
        except ValueError:
            return False

    def _validate_url(self, url):

        accepted_url_keyword = ["taobao", "jd", "tmall"]

        if self._is_url(url) and any([x in url for x in accepted_url_keyword]):
            return 0
        else:
            raise InvalidInputUrl("", "")

    def _validate_time(self, time):

        try:
            datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        except:
            raise InvalidInputTime("", "")

    def _validate_input(self):

        self._validate_url(self._main_url)
        self._validate_url(self._target_url)
        self._validate_time(self._buy_time)

    def _get_logger(self):

        logger = logging.getLogger(name = self.__class__.__name__)
        logger.setLevel(logging.INFO)
        return logger

    def _get_driver_dir(self):

        os_type = platform.system()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        driver_dir = os.path.join(base_dir, "../drivers")

        if os_type == "Linux":
            return os.path.join(driver_dir, "chromedriver_linux")
        elif os_type == "Darwin":
            return os.path.join((driver_dir, "chromedriver_mac"))
        elif os_type == "Windows":
            return os.path.join(driver_dir, "chromedriver_win.exe")

        return None

    def _config_browser(self):

        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver_dir = self._get_driver_dir()
        self._logger.info(f"using {driver_dir}")
        return Chrome(driver_dir, chrome_options=opts)

    def _wait_redirect(self, current_url):

        wait = WebDriverWait(self._browser, 60)
        try:
            wait.until_not(lambda browser: self._browser.current_url == current_url)
        except TimeoutException as e:
            raise e

    def _click_until_redirect(self, element, current_url):

        while current_url == self._browser.current_url:
            try:
                element.click()
            except:
                continue

    def _click_until_new_tab(self, element):

        while len(self._browser.window_handles) == 1:
            try:
                element.click()
            except:
                continue

        self._browser.switch_to.window(self._browser.window_handles[1])


    def _login(self):

        raise SubClassInvaild

    def start(self):

        raise SubClassInvaild

    def _timer(self, buy_time):

        buy_time_raw = datetime.strptime(buy_time, "%Y-%m-%d %H:%M:%S")
        while datetime.now() < buy_time_raw:
            self._timer_printer(buy_time_raw)

    def _timer_printer(self, buy_time):

        print(f"{buy_time - datetime.now()}", end = "\r")
