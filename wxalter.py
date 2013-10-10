#coding:utf-8
#微信网页版群发信息程序
from selenium import webdriver
import time

#b = webdriver.Chrome('/home/zty123/chromedriver')
b=webdriver.Firefox()
b.get("http://wx.qq.com")
raw_input('refresh after enter')
a = b.find_elements_by_css_selector("a.friendDetail")

def send(i):
	b.find_element_by_xpath('//*[@id="chat_leftpanel"]/div[2]/div/div[1]/div[3]/a/span').click()        
	time.sleep(2)                                  
	id = i.get_attribute('id')
	if id == "con_item_weixin":
		pass
	b.find_element_by_xpath('//*[@id="%s"]'%id).click()
	time.sleep(3)
	b.find_element_by_xpath('//*[@id="popupWindow"]/div[2]/div/div[1]/div[5]/div/a/input').click()
	time.sleep(3)
	content=raw_input('输入您要发送的内容:')
	unicontent=content.encode('unicode')
	b.find_element_by_css_selector('textarea.chatInput').send_keys(unicontent)
	time.sleep(5)
for i in range(0,len(a)):
	print i 
	send(a[i])
