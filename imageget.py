#coding:utf-8
#获取目标网站image
import urllib
from selenium import webdriver

b = webdriver.Firefox()
b.get('http://www.google.com/recaptcha/demo/recaptcha')

# get the image source
img = b.find_element_by_xpath('//div[@id="recaptcha_image"]/img')
src = img.get_attribute('src')

# download the image
urllib.urlretrieve(src, "captcha.png")

driver.close()
