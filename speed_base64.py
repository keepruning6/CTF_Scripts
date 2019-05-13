#-*-coding:utf-8-*-

import requests
import base64

URL="http://ctf5.shiyanbar.com/web/10/10.php"



'''
def quick():
	response=requests.get(URL)
	a=response.headers['FLAG']
	a=base64.b64decode(a)
	print a
	key=a[25:]
	print key
	payload={'key':key}
	response2=requests.post(URL,data=payload)
	print response2.text


'''
def speed():
	session=requests.Session()    #注意这里和上面的区别在于需要使用session保持连接
	response=session.get("http://123.206.87.240:8002/web6/")
	a=response.headers['flag']
#	print a
	a=base64.b64decode(a)
#	print a
	a=a[33:]
	a=base64.b64decode(a)
	b='margin'
#	print a
	payload={b:a}
	response2=session.post("http://123.206.87.240:8002/web6/",data=payload)
	print response2.text
#	print response2.headers

if __name__=='__main__':
	speed()