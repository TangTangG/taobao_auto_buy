
import sys
import os
def main():
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from taobao_auto_buy.bin.tb import Taobao
    from taobao_auto_buy.bin.tm_market import  TM_Market

    main_url = "https://www.taobao.com/"
    target_url = "https://chaoshi.detail.tmall.com/item.htm?spm=a3204.7933263.0.0.703422580SQkX7&id=538402184082&rewcatid=51454011"
    buy_time = "2020-01-14 04:59:00"
    if "chaoshi" in target_url:
        chaoshi = TM_Market(main_url, target_url, buy_time)
        chaoshi.start()
    else:
        taobao = Taobao(main_url, target_url, buy_time)
        taobao.start()

if __name__ == "__main__":
    main()
