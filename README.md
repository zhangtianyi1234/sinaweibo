### 
## ├── busdb.py 公交换乘代码
## ├── imageget.py 获取image代码
## ├── mailsql.py mail数据库
## ├── pop163.py  
## ├── qun_qzone.py QQ群成员
## ├── refreshurl.py 刷新url
## ├── selenium_qq2.py QQ登陆
## ├── sinaweibo.py   非API实现sina登陆
## ├── tuitu.py   新浪微博推图刷分
## ├── urlclick.py url测试点击
## ├── webqq.py  QQ登陆
## ├── wxalter.py  微信群发
## └── wx.py


------
python request写的新浪微博登录，发帖，转发，关注方法，没有使用sina 官方API，使用python request请求完成

### INFO信息说明
## 1， 在提交POST请求之前， 需要GET 获取两个参数。
地址是：http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.18)
得到的数据中有 "servertime" 和 "nonce" 的值， 是随机的，其他值貌似没什么用。

## 2.加密解析
通过httpfox/chrome源码分析 观察POST 的数据， 参数较复杂，其中 “su" 是加密后的username, "sp"是加密后的password。"servertime" 和 ”nonce" 是上一步得到的。其他参数是不变的。
- username 经过了BASE64 计算： username = base64.encodestring( urllib.quote(username) )[:-1];
- password 经过了三次SHA1 加密， 且其中加入了 servertime 和 nonce 的值来干扰。即：两次SHA1加密后， 将结果加上 servertime 和 nonce 的值， 再SHA1 算一次。
    步骤方法写在注释中了，相对清晰。

## import导包部分
import requests
import base64
import re
import rsa
import urllib
import json
import binascii
import time

### 方法总结：
登录方法默认，其他都是def 函数，包括：
def add_new():# create a new weibo发布新微博方法
def forward(mid, content):  # forward other's weibo 转发别人微博方法
def followed(dstuid,oid):# folled other's weibo 关注他人微博的方法
