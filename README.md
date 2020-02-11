[![HitCount](http://hits.dwyl.io/Jesseslco/taobao_auto_buy.svg)](http://github.com/Jesseslco/taobao_auto_buy)
# taobao_auto_buy
# 淘宝定时抢购
# 多线程版本 支持同时抢购几个商品[Dev]
### 目前多任务需要扫码几次, 后续再优化[TODO]
## Requirements
## 搭建环境
* python3
  * selenium
* chrome
  * chromedriver
  
## How to use
## 使用说明
1. clone 项目 或者 直接下载zip
```
git@github.com:Jesseslco/taobao_auto_buy.git
```

2. 安装python3

3. 安装依赖package
`python3 -m pip install -r requirements.txt`
Or
`pip3 install -r requirements.txt`

4. 下载chrome(版本79或者最新) chromedriver(需要匹配chrome版本)

   内置chrome79的chromedriver, 如果你的chrome是79, 无需手动下载chromedriver
   
   版本不是79的, 需要手动下载对应版本的chromedriver, 下载的chromedriver需要按照以下方式命名
     > Windows
     
       chromedriver_win.exe    
     > Linux
     
       chromedriver_linux
     > Mac
     
       chromedriver_mac
     
5. 修改config/config.json后运行
   * 修改config/config.json
         修改 config/config.json 然后命令行运行 `python3 manage.py`

## config.json
```
{
    "target_url": ["https://detail.tmall.com/item.htm?spm=a230r.1.14.20.149872d0N6ViJZ&id=598418850958&ns=1&abbucket=9", "https://detail.tmall.com/item.htm?spm=a230r.1.14.20.149872d0N6ViJZ&id=598418850958&ns=1&abbucket=9"],
    "buy_time": ["2020-02-08 03:42:00", "2020-02-09 05:22:00"] 
}
```
**target_url**是商品链接的列表

**buy_time**是抢购时间的列表, 需要严格按照示样格式填写

target_url 和 抢购时间 一一对应

## 支持网站
* 淘宝/天猫
* 天猫超市

## 注意事项
* 仅供学习交流使用, 勿商业用途
* 有任何使用问题, 请raise a issue
