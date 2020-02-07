from lib.base import *
class Taobao(AutoBuyBase):

    def __init__(self, target_url, buy_time):

        super().__init__(target_url, buy_time)

    def _login(self):

        self._browser.get(self._main_url)
        self._browser.find_element_by_link_text("亲，请登录").click()

        current_url = self._browser.current_url
        self._wait_redirect(current_url)

    def _goto_detail(self):

        self._browser.get(self._target_url)

    def _buy(self):

        buy_element = WebDriverWait(self._browser, 20).until(EC.presence_of_element_located((By.ID, "J_LinkBuy")))
        #buy_element.click()

        self._logger.info("正在倒计时")
        self._timer(self._buy_time)
        self._logger.info(f"开始抢购")

        buy_element = WebDriverWait(self._browser, 60).until(EC.element_to_be_clickable((By.ID, "J_LinkBuy")))
        self._click_until_redirect(buy_element, self._browser.current_url)

        self._checkout()

    def _checkout(self):

        sumit_element = WebDriverWait(self._browser, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@id='submitOrderPC_1']//a")))
        self._click_until_redirect(sumit_element, self._browser.current_url)
        self._logger.info("抢购结束")

    def start(self):

        self._logger.info("主程序启动")
        self._login()
        self._logger.info("登陆成功")
        self._goto_detail()
        self._logger.info("进入商品页面 请在抢购时间前完成填写选项")
        self._buy()

