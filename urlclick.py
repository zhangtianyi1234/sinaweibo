#coding:utf-8
#察看网站所有连接的程序,done
from selenium import webdriver
import re,time,requests

b=webdriver.Firefox()
b.get('http://www.cpython.org')

links=b.find_elements_by_tag_name('a')
count=1
for l in links:
	n = b.execute_script("var d=document,a=d.createElement('a');a.target='_blank';a.href=arguments[0];a.innerHTML='.';d.body.appendChild(a);return a",l)
	href=n.get_attribute('href')
	if href.find('mailto:')>-1:
		continue
	n.click()
	time.sleep(1)
	b.switch_to_window(b.window_handles[-1])
	#b.get_screenshot_as_file(count+'.png')
	#b.save_screenshot(count+'.png')
	count += 1
	b.close()
	b.switch_to_window(b.window_handles[0])
