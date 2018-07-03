# Author GiganticDragonfly
##### for login fuction
import urllib.parse 
import urllib.request 
import urllib
import time
import qrcode
import os
import json
import http
import pickle
import base64
import codecs
from http import cookiejar
from http.cookiejar import LWPCookieJar
from http.cookiejar import CookieJar
import urllib.error
import deHtml


def getUuid():
	print("--uuidGet.py->getUuid--")
	url="https://login.wx.qq.com/jslogin"
	params = {'appid':'wx782c26e4c19acffb'}
	uuid = 'fail\n most possible err: no internet connection';	flag = False
	data = bytes(urllib.parse.urlencode(params), encoding='utf8')
	response = dealer.open(url, data=data)
	str=response.read().decode('utf-8')
	uuid = str[50:62]
	if uuid is not None :
		flag = True
	return (uuid,flag)

def getQR(uuAns):
	#print("getQR") 
	#uuAns = uuidGet.getUuid()
	print(uuAns[0])
	if uuAns[1]==True:
		print ('uuid is:'+uuAns[0])
		url = "https://login.weixin.qq.com/l/"+uuAns[0]
		qrcode.make(url).save('img\gena\qr'+uuAns[0][0:9] +'.png')
		print('---------QRcode image is already save as :\n---------img\gena\qr'+uuAns[0][0:9] +'.png')
		QRImagePath = 'img\gena\qr'+uuAns[0][0:9] +'.png'
		os.system('call %s' % QRImagePath)
		return (uuAns[0],url)
	elif uuAns[1]==False:
		print ("Get uuid falied , try to do it again")
		return None

def deFace(faceID):
	faceData = base64.b64decode(faceID[20:]) #de sucess!!
	pic = open('img\\face\head.jpg','wb')
	pic.write(faceData)
	pic.close()
def getFace(uuid):
	url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login"
	params = {'loginicon':'true','uuid':uuid,'tip':'1'}
	data = bytes(urllib.parse.urlencode(params), encoding='utf8')
	response =dealer.open(url, data=data)
	str=response.read().decode('utf-8')
	
	while str.find('201') == -1:
		time.sleep(1)
		response = dealer.open(url, data=data)
		str=response.read().decode('utf-8')
	faceID = str[37:2437]
	deFace(faceID)
	return uuid




def login_prep(uuAns):
	print('-------def login_prep')
	url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login"
	#r=-1243780070&_=1530252136911
	params = {'loginicon':'true','uuid':uuAns[0],'tip':'1'}
	data = bytes(urllib.parse.urlencode(params), encoding='utf8')
	response = dealer.open(url, data=data)
	str=response.read().decode('utf-8')

	while str.find('200') == -1:
		time.sleep(1)
		response = dealer.open(url, data=data)
		str=response.read().decode('utf-8')
	#faceID = str[37:2437]
	print('-------def login_prep_______________OK')
	return str

def loging(uuAns,url):
	print('-------def loging')
	if url.find('200') != -1:
		ticket = url[101:136]
		print(ticket)
		url = url[38:181]+ '&fun=new'#+"&fun=new&version=v2&lang=zh_CN",headers=header
		#act like a true explorer
		#user_agent = ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		req = urllib.request.Request(url)
		response = dealer.open(req)
		data = response.read().decode("utf-8","replace")
		print(data)
		ptl = data.split("<pass_ticket>")
		ptr = ptl[1].split("</pass_ticket>")
		pass_ticket = ptr[0]

		skl = data.split("<skey>")
		skr = skl[1].split("</skey>")
		skeys = skr[0]

		sidl = data.split("<wxsid>")
		sidr = sidl[1].split("</wxsid>")
		wxsid = sidr[0]

		uinl = data.split("<wxuin>")
		uinr = uinl[1].split("</wxuin>")
		wxuin = uinr[0]
		print('-------def loging_______________OK')
		global tiks
		tiks = (ticket,pass_ticket,skeys,wxsid,wxuin)
		return tiks
	else :
		print('---------failed!!! \n --------- getting ticket failed!!!')
	return

def initing(uuAns,tiks):
	print('----------initing')
	url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?pass_ticket="+tiks[1]
	#for item in cookie:
	#	print('Name = %s' % item.name)
	#	print('Value = %s' % item.value)
	postData = {
		'BaseRequest': {
			'Uin': tiks[4],
			'Sid': tiks[3],
			'Skey': tiks[2],
			'DeviceID': 'e756936914066191'
		}
	}
	header={
	"Accept":"application/json, text/plain, */*",
	"Accept-Encoding":"gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Connection":"keep-alive",
	"Content-Length": "149",
	"Content-Type": "application/json;charset=UTF-8",
	"Host":"wx.qq.com",
	"Origin": "https://wx.qq.com",
	"Referer":"https://wx.qq.com/?&lang=zh_CN",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
	}

	data = json.dumps(postData).encode('utf-8')
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request,data).read()
	data = response.decode('utf-8')
	
	return response

def getContact():
	print("_______________________getContact")
	url="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?pass_ticket="+tiks[1]+"&skey="+tiks[2]  #&r=1530582947129&seq=0
	request = urllib.request.Request(url)
	response = dealer.open(request).read()
	data = response.decode('utf-8',"replace")
	with open('da.txt','wb') as f:
		f.write(response)
	print(len(data))


def main():
	# HTTPS准备
	global dealer
	#声明一个CookieJar对象实例来保存cookie
	global cookie
	cookie = cookiejar.CookieJar()
	#利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
	handler=urllib.request.HTTPCookieProcessor(cookie)
	#通过CookieHandler创建opener
	dealer =urllib.request.build_opener(handler)#making a opener dealer 
	#此处的open方法打开网页
	response = dealer.open('http://wx.qq.com')
	#打印cookie信息
	for item in cookie:
		print('Name = %s' % item.name)
		print('Value = %s' % item.value)
	uuAns = getUuid()
	qrAns = getQR(uuAns)
	print("---"+qrAns[0])
	getFace(qrAns[0])
	str= login_prep(uuAns)
	login_prep(uuAns)
	tiks =loging(uuAns,str)
	print(tiks)
	initing(uuAns,tiks)
	getContact()




if __name__ == "__main__":
	main()