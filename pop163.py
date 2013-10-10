#coding:utf-8
import poplib,email,string

host="pop3.163.com"
username = "python4@163.com"
password = 'codepark'

p = poplib.POP3(host)

p.user(username)
p.pass_(password)

ret = p.stat()
for i in range(1,ret[0] + 1):
	all_list = p.top(i,0)

ret = p.list()

h,message,octet = p.retr(13)

p.quit()


mail=email.message_from_string(string.join(message,'\n'))



subject = email.Header.decode_header(mail.get('subject'))

if type(subject[0][0]) in (type(b' '),):
	print subject[0][0].decode(subject[0][1])
else:
	print subject[0][0]

for par in mail.walk():
	if not par.is_multipart():
		name = par.get_param("name")
		if not name:
			pass#print par.get_payload(decode=True)
		else:
			print "有附件"

print mail.get('In-Reply-To')
print mail.get('References')
print mail.get('Message-ID')
print mail.keys()
