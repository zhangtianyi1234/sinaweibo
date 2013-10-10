#coding:utf-8
#刷新url网页地址，增加点击量的方法
from selenium import webdriver
import time

while 1:
	d = webdriver.Firefox()

	for i in range(0,8):
			d.get("http://witting.blog.51cto.com/7555529/1286776")
			time.sleep(1)
			d.get("http://witting.blog.51cto.com/7555529/1284399")
			#d.find_element_link_by_text('下载文档').click()
	time.sleep(2)
	d.quit()


