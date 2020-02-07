# taobao_auto_buy
# 淘宝自动购买

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
```
python3 -m pip install -r requirements.txt
or
pip3 install -r requirements.txt
```
4. 下载chrome(版本79或者最新) chromedriver(需要匹配chrome版本)
   内置chrome79的chromedriver, 如果你的chrome是79, 无需手动下载chromedriver
   版本不是79的, 需要手动下载对应版本的chromedriver, 下载的chromedriver需要按照以下方式命名
     > window
     * chromedriver_win.exe    
     > linux
     * chromedriver_linux
     > mac
     * chromedriver_mac
5. 命令行带参数运行 或者 修改config/config.json后运行
   * 命令行参数运行
         python3 manage.py -u [target_url] -t [buy_time]
   * 修改config/config.json
         修改 config/config.json 然后命令行运行 `python3 manage.py`

## config.json
```
{
    "target_url": "https://detail.tmall.com/item.htm?spm=a230r.1.14.20.149872d0N6ViJZ&id=598418850958&ns=1&abbucket=9",
    "buy_time": "2020-02-08 03:42:00"
}
```
target_url是商品链接
buy_time是抢购时间, 需要严格按照示样格式填写

## 支持网站
* 淘宝/天猫
* 天猫超市


## 注意事项
* 仅供学习交流使用, 勿商业用途
* 有任何使用问题, 请raise a issue
