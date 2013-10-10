#coding:utf-8
#webqq自动登陆和群组信息察看
from selenium import webdriver
import time,re,requests
import getpass

class QQ:
	h={'Referer':'http://s.web2.qq.com/proxy.html?v=20110412001&callback=1&id=3'}
	def __init__(self):
		self.d=wendriver.Firefox()
		self.get('http://web2.qq.com/webqq.html')

	def login(self,qq,pw,check=0):
		self.d.find_element_by_id('alloy_icon_app_50_3').click()
		raw_input('refresh after enter')
		self.d.switch_to_frame('iframe_login')
		u=self.d.find_element_by_id('u')
		p=self.d.find_element_by_id('p')
		login=self.d.find_element_by_id('login_button')
		
		u.clear()
		u.send_keys(qq)
		p.send_keys(pw)
		if check:
			raw_input('input image,then enter')
		login.click()

a=QQ()
qq=raw_input('qq:')
pw=getpass.getpass('password')
a.login(qq,pw)

