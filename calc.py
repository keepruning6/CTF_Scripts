#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
URL= "http://123.206.87.240:8002/qiumingshan/"


def qiumingshan():
	session=requests.Session()
	response=session.get(URL)
#	print response.headers
	a=response.text
	soup=BeautifulSoup(a,'lxml')
#	print soup.prettify()
	print soup.div
	biaoda=soup.div.string
	print biaoda
	biaoda=biaoda.split("=")
	print biaoda[0]
	a=eval(biaoda[0])
	print a
	payload={'value':a}
	resonse2=session.post(URL,data=payload)
	print resonse2.text



if __name__=='__main__':
	qiumingshan()