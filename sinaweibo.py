# coding:utf-8
#import导包部分
import requests
import base64
import re
import rsa
import urllib
import json
import binascii
import time

'''
#INFO信息说明
1， 在提交POST请求之前， 需要GET 获取两个参数。
       地址是：http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.18)
       得到的数据中有 "servertime" 和 "nonce" 的值， 是随机的，其他值貌似没什么用。
2， 通过httpfox/chrome源码分析 观察POST 的数据， 参数较复杂，其中 “su" 是加密后的username, "sp"是加密后的password。"servertime" 和 ”nonce" 是上一步得到的。其他参数是不变的。
    username 经过了BASE64 计算： username = base64.encodestring( urllib.quote(username) )[:-1];
    password 经过了三次SHA1 加密， 且其中加入了 servertime 和 nonce 的值来干扰。
    即： 两次SHA1加密后， 将结果加上 servertime 和 nonce 的值， 再SHA1 算一次。
'''
#user,password用户名密码
username = 'zhangtianyi1234@126.com'
password = 'mbdhd2009'

session = requests.Session()
#login url登录地址
url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.5)&_=1364875106625'
url_login = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.5)'

# get servertime,nonce, pubkey,rsakv获取登录session相关登录时间等信息
resp = session.get(url_prelogin)
json_data = re.search('\((.*)\)', resp.content).group(1)
data = json.loads(json_data)

servertime = data['servertime']
nonce = data['nonce']
pubkey = data['pubkey']
rsakv = data['rsakv']

# calc su，第一步加密用户名
su = base64.b64encode(urllib.quote(username))

# calc sp，第二步，加密密码
rsaPublickey = int(pubkey, 16)
key = rsa.PublicKey(rsaPublickey, 65537)
message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
sp = binascii.b2a_hex(rsa.encrypt(message, key))
#post reqest,第三部，提交请求
postdata = {
                    'entry': 'weibo',
                    'gateway': '1',
                    'from': '',
                    'savestate': '7',
                    'userticket': '1',
                    'ssosimplelogin': '1',
                    'vsnf': '1',
                    'vsnval': '',
                    'su': su,
                    'service': 'miniblog',
                    'servertime': servertime,
                    'nonce': nonce,
                    'pwencode': 'rsa2',
                    'sp': sp,
                    'encoding': 'UTF-8',
                    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
                    'returntype': 'META',
                    'rsakv' : rsakv,
                    }

resp = session.post(url_login, data=postdata)
login_url = re.findall('replace\("(.*)"\)', resp.content)
# print login_url
resp = session.get(login_url[0])
# print resp.content
uid = re.findall('"uniqueid":"(\d+)",', resp.content)[0]
url = "http://weibo.com/u/" + uid
resp = session.get(url)
# print resp.content

# text:测试下使用Python写的登录和发文的demo，先获取地址信息
# def decode_content(content):  # 解码输入的文本
#         result = re.findall('<script>STK && STK.pageletM && STK.pageletM.view\((.*?)\)<\/script>', content)
#         for i in result:
#                 r = i.encode("utf-8").decode('unicode_escape').encode("utf-8")
#                 print r.replace("\/", "/")
# # def add_new(content, resp):  # 添加新微博的方法

def add_new():#create a new weibo发布新微博方法
    addurl = "http://weibo.com/aj/mblog/add?_wv=5&__" + str(time.time())
    content = "测试下使用python写的发文"
    data = {'text':content, 'rank':'0', 'location':'home', 'module':'stissue', '_t':'0'}
    headers = {}
    headers['set-cookie'] = resp.headers['set-cookie']
    headers['Referer'] = 'http://weibo.com/u/' + uid + '?topnav=1&wvr=5'
    respon = session.post(addurl, data, headers=headers)
    print respon.status_code
add_new("添加新微博的方法", resp)

# mid:3599892905366755
# d_expanded:off
# expanded_status:
# _t:0
# __rnd:1373792334798
# add_new()
# mid=3600011008917103
def forward(mid, content):  # forward other's weibo 转发别人微博方法
    forwardurl = "http://weibo.com/aj/mblog/forward?_wv=5&__" + str(time.time())
    data = {'uid':mid, 'style-type':2, 'reason':content, 'rank':0, 'location':'mblog', '_t':0}
    headers = {}
    headers['set-cookie'] = resp.headers['set-cookie']
    headers['Referer'] = 'http://weibo.com/u/3118088481?from=profile&wvr=5&loc=tabprofile'
    respon = session.post(forwardurl, data, headers=headers)
    print respon.status_code
forward(3600011008917103, "转发")

def followed(dstuid,oid):#folled other's weibo 关注他人微博的方法
        followedurl = "http://weibo.com/aj/f/followed?_wv=5&__rnd=%s"% int(time.time())
        data = {'uid':dstuid, 'rank':0, 'location':'mblog', '_t':0,'f':0,
                'oid':oid,
                'nogroup':'false',
                'challenge_uids':'',
                'check_challenge_value':'',
                'location':'home',
                'refer_sort':'interest',
                'refer_flag':'friend_bridge',
                'loc':1,
                }
        headers = {}
        headers['set-cookie'] = resp.headers['set-cookie']
        headers['Referer'] = 'http://weibo.com/u/'+oid+'?topnav=1&wv=5'
        respon = session.post(followedurl, data, headers=headers)
        print respon.status_code
followed('2898801847',uid)
    
