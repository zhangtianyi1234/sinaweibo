#coding:utf-8
#获取所有加入群的QQ号码方法,done
import re,requests
from selenium import webdriver
#如果非linux，使用fixfox
#d = webdriver.Chrome('/home/zty123/chromedriver')
d = webdriver.Firefox()
url = "http://qun.qzone.qq.com"

d.get(url)
grouplist=[]

raw_input("enter after login:")

def getqq():
	allqq= re.findall('<span class="member_id">\((\d+)\)</span>',d.page_source)
	filesave=open('qqsave.txt','a+')
	for i in allqq:
		print i
		filesave.write(i+'\n')
	filesave.close()
def getgroupid():
	global grouplist
	list1 = re.findall('data-groupid="(\d+)"',d.page_source)	
	grouplist = list(set(list1))

getgroupid()


def getgroupinfo(id):
	groupurl = "http://qun.qzone.qq.com/group#!/%s/member"%id
	d.get(groupurl)
	d.refresh()
	#d.implicitly_wait(120)
	raw_input("enter after refresh:")
	getqq()

for id in grouplist:
	getgroupinfo(id)

