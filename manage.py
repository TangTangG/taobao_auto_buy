
import sys
import os
def main():
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from taobao_auto_buy.bin.tb import Taobao
    from taobao_auto_buy.bin.tm_market import  TM_Market

    main_url = "https://www.taobao.com/"
    target_url = "https://chaoshi.detail.tmall.com/item.htm?spm=a3204.13572463.9849059970.1.36c25768ubSbf8&id=20739895092&skuId=4227830352490"
    #target_url = "https://chaoshi.detail.tmall.com/item.htm?spm=a3204.12709799.3605942727.2.39206d70bJ61jX&pos=2&acm=lb-zebra-471145-6150817.1003.1.6178339&id=567140166040&scm=1003.1.lb-zebra-471145-6150817.FF-hyhsfZA-725677994_B-500106_C-None_D-567140166040_E-D_G-139.0_X-TmcsSFlog-FF_567140166040_6178339"
    buy_time = "2020-01-14 20:00:00"
    if "chaoshi" in target_url:
        chaoshi = TM_Market(main_url, target_url, buy_time)
        chaoshi.start()
    else:
        taobao = Taobao(main_url, target_url, buy_time)
        taobao.start()

if __name__ == "__main__":
    main()
