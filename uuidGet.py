# Author GiganticGragonfly
# NEED INTERNET CONNECTION
# get uuid for WeChat(Tencent) login
# getUuid return:(uuid,flag)
# flag : Ture for getting uuid sucess

import urllib.parse 
import urllib.request 
import pickle
import faceDe

def getUuid():
	print("--uuidGet.py->getUuid--")
	url="https://login.wx.qq.com/jslogin"
	params = {'appid':'wx782c26e4c19acffb'}
	uuid = 'fail\n most possible err: no internet connection';	flag = False
	data = bytes(urllib.parse.urlencode(params), encoding='utf8')
	response = urllib.request.urlopen(url, data=data)
	str=response.read().decode('utf-8')
	uuid = str[50:62]
	if uuid is not None :
		flag = True
	return (uuid,flag)

def getFace(uuid):
	url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login"
	params = {'loginicon':'true','uuid':uuid,'tip':'1'}
	data = bytes(urllib.parse.urlencode(params), encoding='utf8')
	response = urllib.request.urlopen(url, data=data)
	str=response.read().decode('utf-8')
	
	while str.find('201') == -1:
		time.sleep(1)
		response = urllib.request.urlopen(url, data=data)
		str=response.read().decode('utf-8')
	faceID = str[37:2437] #Face ，base64编码，需要解码，再录入txt命名为jpg即可输出
	faceDe.deFace(faceID)

	


	print(faceID)


def purtest(a):
	print(a)

def main():
	print("--uuidGet.py--")
	print(getUuid())

if __name__ == "__main__":
	main()