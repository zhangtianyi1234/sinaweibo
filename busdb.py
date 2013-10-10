#coding:utf-8
#bus公交换乘程序
from uliweb.orm import *
db= get_connection("sqlite:///beijing.db")

class cnbus(Model):
	xid  = Field(int)
	zhan = Field(str)
	kind = Field(int)

class cnchange(Model):
	src  = Field(int)
	dst  = Field(int)

class cnbusw(Model):
	busw = Field(str)

def getcnbusw(xid):
	b = cnbusw.get(cnbusw.c.id == xid)
	return b.busw 

#db.metadata.drop_all()

db.metadata.create_all()

'''
allxid = cnbusw.all()

for n in allxid:
	allzhan = cnbus.filter(cnbus.c.xid == n.id ).filter(cnbus.c.kind==1)
	temp = []
	for n1 in allzhan:
		zhanallbus = cnbus.filter(cnbus.c.zhan==n1.zhan).filter(cnbus.c.kind==1)
		for n2 in zhanallbus:
			if n2.xid == n.id:
				continue
			temp.append(n2.xid)

	for n3 in temp:
		a     = cnchange()
		a.dst = n3
		a.src = n.id
		a.save()
'''

start="1号航站楼"
end="八角"

l_start = []
l_end=[]

zhanallbus = cnbus.filter(cnbus.c.zhan==start.decode('utf-8')).filter(cnbus.c.kind==1)
for n2 in zhanallbus:
	l_start.append(n2.xid)

zhanallbus = cnbus.filter(cnbus.c.zhan==end.decode('utf-8')).filter(cnbus.c.kind==1)
for n2 in zhanallbus:
	l_end.append(n2.xid)

print l_start,l_end


list_start = [l_start]
list_start_all = l_start[:]

def getchange(l):
	global list_start,list_start_all
	list_temp1 = []
	for n in l:
		changes = cnchange.filter(cnchange.c.src == n)
		for n1 in changes:
			if n1.dst not in list_start_all:
				list_temp1.append(n1.dst)
			
	list_start.append(list_temp1)
	list_start_all += list_temp1

while 1:
	if list(set(list_start[-1]) & set(l_end)):
		break
	getchange(list_start[-1])


print list_start[-1]

