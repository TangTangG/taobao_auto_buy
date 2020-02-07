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
2. install python3
3. install requirements
```
python3 -m pip install -r requirements.txt
or
pip3 install -r requirements.txt
```
4. download chrome(version=79 or lastest) and chromedriver(need to be updated with chrome)
   下载chrome(版本79或者最新) chromedriver(需要匹配chrome版本)
5. run with command line or configure config.json
   * Command Line
         python3 manage.py -u [target_url] -t [buy_time]
   * configure config.json
         modify the config/config.json then run `python3 manage.py`

## Configuration

## Supported
## 支持网站
* 淘宝/天猫
* 天猫超市

## Noticed
## 注意事项
* 仅供学习交流使用, 勿商业用途
* 有任何使用问题, 请raise a issue
