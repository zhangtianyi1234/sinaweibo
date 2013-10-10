#coding:utf-8
from selenium import webdriver
import requests,re,time
import getpass


class QQ:
	h = {"Referer":"http://s.web2.qq.com/proxy.html?v=20110412001&callback=1&id=3"}
	
	def __init__(self):
#		self.d = webdriver.Chrome('/home/zty123/chromedriver')#使用chrome浏览器报错
		self.d=webdriver.Firefox()
		self.d.get("http://web2.qq.com/webqq.html")

	def login(self,qq,pw,check=0):
		#show qq login window
		self.d.find_element_by_id("alloy_icon_app_50_3").click()
		time.sleep(2)
		self.d.switch_to_frame('ifram_login')
		u     = self.d.find_element_by_id('u')
		p     = self.d.find_element_by_id('p')
		login = self.d.find_element_by_id('login_button')

		u.clear()
		u.send_keys(qq)
		p.send_keys(pw)
		if check:
			raw_input("请在浏览器上输入验证码后，回车继续：")
		login.click()

	def getvfwebqq(self):
		for n in range(10):
			vfwebqq = re.findall('vfwebqq=(.*?)["&]',self.d.page_source)
			if len(vfwebqq) > 0:
				break
			time.sleep(1)
		self.vfwebqq = vfwebqq[0]

	def request(self):
		self.cookies = {}
		for s in self.d.get_cookies():
    			self.cookies[s['name']] = s['value']
		self.req = requests.Session()

	def getqqbyuin(self,uin):
		url = "http://s.web2.qq.com/api/get_friend_uin2?tuin=%s&verifysession=&type=1&code=&vfwebqq=%s&t=%s" % (uin,self.vfwebqq,int(time.time()))

		ret = self.req.get(url,cookies=self.cookies,headers=self.h)
		q = re.findall('"account":(\d+)',ret.content)
		tartgetfile=open("QQcheshi.txt",'a+')#注意读写文件
		if len(q) > 0:
			print q[0]
			tartgetfile.write(q[0]+'@qq.com'+'\n')
		tartgetfile.close()

	def getgroupuins(self):
		all_list = re.findall('"chatBox_groupMember_buddy " uin="(.*?)"',self.d.page_source)
		return all_list
	def getgroupqq(self):
		all_list = a.getgroupuins()
		for uin in all_list:
			a.getqqbyuin(uin)

 
a = QQ()
qq=raw_input("qq:")
pw=getpass.getpass("Passwd:")
a.login(qq,pw)
a.getvfwebqq()
a.request()


while 1:
	raw_input("选择你要查看的群组后继续：")
	a.getgroupqq()

	
#715186254 zhangting

