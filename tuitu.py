#coding:utf-8
#微博推兔刷分程序,后台直接输入的形式完成,done
from selenium import webdriver
import requests,re,time

b = webdriver.Chrome("/home/zty123/chromedriver")
b.get("http://apps.weibo.com/tuituoo?ref=appsearch")
raw_input("等待输入。。。")
cookies = {}
all_cookies = b.get_cookies()
for s in all_cookies:
	cookies[s['name']] = s['value']
access_token = "2.00VFU1aDpQpX8Eeab5c989e50Ph6Ng"

def follow(sid):
	url1 = "http://tuitu.sinaapp.com/weibo/task/dofollow"
	url2 = "https://api.weibo.com/2/friendships/create.json"
	url3 = "http://tuitu.sinaapp.com/weibo/task/followsuccess"

	ret1 = requests.post(url1, data = {'sid':sid}, cookies = cookies)
	#source的值是固定的
	ret2 = requests.post(url2, data = {'source':'4071554311', 'uid':sid, '_cache_time':'0', 'method':'post', 'access_token':access_token}, cookies=cookies) 
	ret3 = requests.post(url3, data={'sid':sid}, cookies=cookies)

def unfollow(sid):
	url4 = 'https://api.weibo.com/2/friendships/destroy.json'
	ret4 = requests.post(url4, data = {'source':'4071554311', 'uid':sid, '_cache_time':'0', 'method':'post', 'access_token':access_token}, cookies=cookies) 
	ret4 = requests.post(url4, data={'sid':sid}, cookies=cookies)

def getsid():
	url = 'http://tuitu.sinaapp.com/weibo/task/followtuis/p/1/province/0/city/0'
	ret = requests.get(url, cookies=cookies)
	allid = re.findall('tu_follow\((\d+), this', ret.content)#this 前面有空格

	for i in allid:
		follow(i)
		#addfollow(i)
		print i+'已经关注'

getsid()
