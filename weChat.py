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
import base64
import codecs
from http import cookiejar
from http.cookiejar import LWPCookieJar
from http.cookiejar import CookieJar
import urllib.error
import deHtml
import re
import sys
import deData
import random

def getR():
	randomTicket = -int(time(time()))
	return randomTicket

def getUuid():
	if testing:
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
	if testing:
		print(uuAns[0])
	if uuAns[1]==True:
		if testing:
			print ('uuid is:'+uuAns[0])
		url = "https://login.weixin.qq.com/l/"+uuAns[0]
		qrcode.make(url).save('img\gena\qr'+uuAns[0][0:9] +'.png')
		if testing:
			print('---------QRcode image is already save as :\n---------img\gena\qr'+uuAns[0][0:9] +'.png')
		QRImagePath = 'img\gena\qr'+uuAns[0][0:9] +'.png'
		os.system('call %s' % QRImagePath)
		
		return (uuAns[0],url)
	elif uuAns[1]==False:
		if testing:
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
	data = bytes(urllib.parse.urlencode(params), encoding='utf-8')
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
	if testing:
		print('-------def login_prep')
	urlL="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login"
	#r=-1243780070&_=1530252136911
	params = {'loginicon':'true','uuid':uuAns[0],'tip':'1'}
	data = bytes(urllib.parse.urlencode(params), encoding='utf8')
	response = dealer.open(urlL, data=data)
	url=response.read().decode('utf-8')
	if testing:
		print(url)
	while url.find('200') == -1:
		response = dealer.open(urlL, data=data)
		url=response.read().decode('utf-8')
		if testing:
			print(url)
		time.sleep(1)
	#faceID = str[37:2437]
	if testing:
		print('-------def login_prep_______________OK')
	return url

def loging(uuAns,url):
	if testing:
		print('-------def loging')
	if url.find('200') != -1:
		ticket = url[101:136]
		if testing:
			print(ticket)
		url = url[38:181]+ '&fun=new'#+"&fun=new&version=v2&lang=zh_CN",headers=header
		#act like a true explorer
		#user_agent = ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		req = urllib.request.Request(url)
		response = dealer.open(req)
		data = response.read().decode("utf-8","replace")
		if testing:
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
		if testing:
			print('-------def loging_______________OK')
		global tiks
		tiks = (ticket,pass_ticket,skeys,wxsid,wxuin)
		return tiks
	else :
		if testing:
			print('---------failed!!! \n --------- getting ticket failed!!!')
	return

def initing(uuAns,tiks):
	if testing:
		print('----------initing')
	url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?pass_ticket="+tiks[1]
	#for item in cookie:
	#	print('Name = %s' % item.name)
	#	print('Value = %s' % item.value)
	global BaseRequest
	BaseRequest={'Uin': tiks[4],'Sid': tiks[3],'Skey': tiks[2],'DeviceID': 'e756936914066191'}
	
	postData = {'BaseRequest': BaseRequest}

	data = json.dumps(postData).encode('utf-8')
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request,data).read()
	data = response.decode('utf-8')
	
	return response

def getContact( dosave ):
	if testing:
		print("_______________________getContact")
	url="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?pass_ticket="+tiks[1]+"&skey="+tiks[2]  #&r=1530582947129&seq=0
	request = urllib.request.Request(url)
	response = dealer.open(request).read()
	if dosave:
		with open('da.txt','wb') as f:
			f.write(response)

	data = response.decode('utf-8')
	#data = re.sub(r'<span class=".*"></span>' , '' , data )
	data = json.loads(data)
	global friendlist
	friendlist=data['MemberList']
	if testing:
		print('____length of mlist')
		print(len(friendlist))

def selectFriend(remark):
	for element in friendlist:
		if element["RemarkName"]==remark:
			return element
			break
		if element["NickName"]==remark:
			return element
			break
	return False

def send(ToUserName,sendMsg):
	if testing:
			print("_______________________send")
	url="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket="+tiks[1]
	R_ID = str(random.random())[2:]+'1'
	Msg={
			"Type":1,"Content":sendMsg,
			"FromUserName":user['UserName'],
			"ToUserName":ToUserName,
			"LocalID":R_ID,"ClientMsgId":R_ID
		}
	postData = {'BaseRequest':BaseRequest,"Msg":Msg,"Scene":0}
	data = json.dumps(postData).encode('utf-8')
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request,data).read()

def countGroup():
	listG = []
	with open('data.csv','r', encoding="gb18030") as f:
		for line in f:
			row = []
			if line.find("@@") == -1:
				continue
			line = line.split(",")
			for element in line:
				row.append(element)
			listG.append(row)
	with open("group.csv","w",encoding="gb18030",newline="") as groupcsv:
		for i in listG:
			response7=i
			response7=str(response7)
			print(response7)
			groupcsv.write(response7+'\n')
	#将群组写入csv
	return listG

def sendAMsg():
	name = input("---------------------目标好友或群聊：")
	tar_friend = selectFriend(name)
	while tar_friend ==False :
		name = input("---------------------没能找到该好友\n---------------------请填写接受好友备注名：")
		tar_friend = selectFriend(name)
	print('---------------------您选择的好友为：\n')
	print(tar_friend)

	ToUserName = tar_friend['UserName']
	if testing:
		print(ToUserName)
	
	msg = "Wechat program :Tencent weChat System Wrong Message "
	msg = input('---------------------请填写发送信息')
	send(ToUserName,msg)


def main():
	global testing
	testing = False
	# HTTPS准备
	global dealer
	#声明一个CookieJar对象实例来保存cookie
	global cookie
	cookie = cookiejar.CookieJar()
	#利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
	handler=urllib.request.HTTPCookieProcessor(cookie)
	#通过CookieHandler创建opener
	dealer =urllib.request.build_opener(handler)#making a opener dealer 
	dealer.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'),
		('Host', 'wx.qq.com'),
		('Accept', 'application/json, text/plain, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'),
		('Referer', 'https://wx.qq.com/'),
		('DNT', '1')]
	#此处的open方法打开网页
	response = dealer.open('http://wx.qq.com')
	#打印cookie信息
	if testing:
		for item in cookie:
			print('Name = %s' % item.name)
			print('Value = %s' % item.value)
	uuAns = getUuid()
	qrAns = getQR(uuAns)
	print('---------------------请扫描二维码登陆')
	if testing:
		print("---"+qrAns[0])
	getFace(qrAns[0])
	str= login_prep(uuAns)
	login_prep(uuAns)
	tiks =loging(uuAns,str)
	if testing:
		print(tiks)
	init_data = initing(uuAns,tiks)
	global user
	with open('initDa.txt','wb') as f:
		f.write(init_data)
	with open('initDa.txt','r',encoding='utf-8') as f:
		user=json.loads(f.read())['User']
	if testing:
		print(user)
	getContact(False)
	save = False
	if save:
		deData.deDa()
	
	task = False
	print("\n----------1 : 发送一条消息\n----------2 ：查看所有联系人及群组\n----------3 ：查看所有群组\n----------tune : 调试模式\n---------- 回车：退出\n")
	task = input("请输入数字编号")
	
	while task:
		if task == '1':
			print('发送消息')
			sendAMsg()
		if task == '2':
			print('查看所有联系人及群组')
		if task == '3':
			print('查看所有群组')
			print(countGroup())
		if task == '0':
			print('推出')
			task = False
		#if task == 'tune':
		#	print('调试')
		#	testing = True
		else:
			print("\n----------1 : 发送一条消息\n----------2 ：查看所有联系人及群组\n----------3 ：目前为止的骚操作\n----------0 或 回车：退出\n")
			task = input("请输入数字编号")

if __name__ == "__main__":
	main()