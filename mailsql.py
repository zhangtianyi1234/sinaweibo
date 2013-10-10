#coding=utf-8
from uliweb.orm import *
import datetime


db=get_connection('mysql://root:root@localhost/email?charset=utf8')

class mail(Model):
	s_email = Field(str)
	dt      = Field(datetime.datetime,auto_now_add=True)
	status  = Field(str)

def getemail(status):
	return mail.get(mail.c.status == status)

def getemails(status,count):
	return mail.filter(mail.c.status == status).limit(count)


def resetmail():
	while 1:
		n = getemail("1")
		if not n:
			break
		n.status = "0"
		n.save()
def setemailstatus(n,status):
	n.status = status
	n.save()


def getcheck():
	e = getemail("0")
	setemailstatus(e,'1')
	return e.s_email

#resetmail()

db.metadata.create_all()
#f = open("teach.txt")
#lines = f.readlines()
#for l in lines:
#	addmail(l.strip())
