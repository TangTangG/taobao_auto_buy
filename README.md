# taobao_auto_buy

## Requirements
* python3.8
  * selenium==3.141.0
* chrome
  * chromedriver
  
## How to use
1. clone project
```
git@github.com:Jesseslco/taobao_auto_buy.git
```
2. install python3.8
3. install requirements
```
pip3 install selenium==3.141.0
```
4. download chromedriver
5. configure config.json
6. run
```
python3 taobao.py
```
## Configuration
### config.json
```
{
 "main_url" : "https://www.taobao.com/",
 "target_url" : "",
 "amount_to_buy" : 1,
 "prop_check_list" : [0,0],
 "buy_time" : "2020-01-08 12.00.00"
}
```
## Noticed
* star if you like this project
* for any problem, please raise a issue
