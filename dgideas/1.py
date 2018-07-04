import urllib.request
import http.cookiejar
import time
import json

wxToken = {}

def getR():
	randomTicket = "-1577634346"
	return randomTicket

def dropHTML(_rawData):
	return None

def wxGetLoginToken():
	jsLoginURL = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb"
	jsLogin = urllib.request.urlopen(jsLoginURL).read().decode("utf-8")
	return jsLogin.split("\"")[1]

def wxGetQRCode(QRCodeToken):
	qrCodeURL = "https://login.weixin.qq.com/qrcode/" + str(QRCodeToken)
	return urllib.request.urlopen(qrCodeURL).read()

def wxGetLoginStatus(QRCodeToken):
	loginStatusURL = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=" + str(QRCodeToken) + "&tip=0&r=-1575532129&_=1530583685459"
	loginStatus = urllib.request.urlopen(loginStatusURL).read().decode("utf-8")
	loginStatusNumber = loginStatus.split("window.code=")[1].split(";")[0]
	return [loginStatus, loginStatusNumber]

def getWxRedirectURL(rawLoginResponse):
	return rawLoginResponse.split("window.redirect_uri=\"")[1].split("\"")[0] + "&fun=new"

def wxRedirect(redirectURL):
	return urllib.request.urlopen(redirectURL).read().decode("utf-8")

def wxInit(wxToken):
	initURL = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-1577634346&pass_ticket=" + wxToken["pass_ticket"]
	postData = {
		'BaseRequest': {
			'Uin': wxToken["wxuin"],
			'Sid': wxToken["wxsid"],
			'Skey': wxToken["skey"],
			'DeviceID': 'e756936914066191'
		}
	}
	return urllib.request.urlopen(initURL, json.dumps(postData).encode('utf-8')).read().decode('utf-8')

def wxGetContact(wxToken):
	getContactURL = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?pass_ticket=" + wxToken["pass_ticket"] + "&r=" + getR() + "&seq=0&skey=" + wxToken["skey"]
	return urllib.request.urlopen(getContactURL).read().decode("utf-8")

def main():
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'),
		('Host', 'wx.qq.com'),
		('Accept', 'application/json, text/plain, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'),
		('Referer', 'https://wx.qq.com/'),
		('DNT', '1')]
	urllib.request.install_opener(opener)
	
	print("获取登录令牌...")
	wxToken["loginQRToken"] = wxGetLoginToken()
	print("获取到登录令牌为:" + str(wxToken["loginQRToken"]))
	
	QRCodeFilename = "qrcode.jpg"
	with open(QRCodeFilename, "wb") as QRCode:
		QRCode.write(wxGetQRCode(wxToken["loginQRToken"]))
	print("已生成二维码图片" + str(QRCodeFilename) + "，请使用手机扫描")
	
	while True:
		wxLoginStatus = wxGetLoginStatus(wxToken["loginQRToken"])
		if wxLoginStatus[1] == "201":
			print("已经扫描二维码，请在手机上点击登录")
		elif wxLoginStatus[1] == "200":
			print("确认登录微信")
			wxToken["redirectURL"] = getWxRedirectURL(wxLoginStatus[0])
			print("\t获得返回地址：" + wxToken["redirectURL"])
			break
		time.sleep(1)
	
	wxWebWechatToken = wxRedirect(wxToken["redirectURL"])
	wxToken["skey"] = wxWebWechatToken.split("<skey>")[1].split("</skey>")[0]
	wxToken["wxsid"] = wxWebWechatToken.split("<wxsid>")[1].split("</wxsid>")[0]
	wxToken["wxuin"] = wxWebWechatToken.split("<wxuin>")[1].split("</wxuin>")[0]
	wxToken["pass_ticket"] = wxWebWechatToken.split("<pass_ticket>")[1].split("</pass_ticket>")[0]
	print("获得微信网页版凭据信息：", end="")
	wxToken.pop("redirectURL")
	print(wxToken)
	
	wxInitData = json.loads(wxInit(wxToken))
	wxToken["displayname"] = wxInitData["User"]["NickName"]
	wxToken["username"] = wxInitData["User"]["UserName"]
	print("===你好，" + wxToken["displayname"] + "！===")
	print("最近联系人为:")
	for recentCommunicatePerson in wxInitData["ContactList"]:
		displayName = recentCommunicatePerson["RemarkName"] or recentCommunicatePerson["NickName"]
		print("\t" + displayName)
	
	wxContacts = json.loads(wxGetContact(wxToken))
	print("载入共计" + str(wxContacts["MemberCount"]) + "位联系人")
	
	while True:
		contactTo = input("请输入要发送消息的联系人:")
		searchedList = []
		for contacts in wxContacts["MemberList"]:
			if contacts["NickName"].find(contactTo) != -1 or contacts["RemarkName"].find(contactTo) != -1:
				searchedList.append({'NickName': contacts["NickName"], 'RemarkName': contacts["RemarkName"], 'UserName': contacts["UserName"]})
		if len(searchedList):
			print("找到以下联系人")
			break
		else:
			print("\t未找到任何联系人")
	for person in searchedList:
		print("\t\t*" + person["NickName"] + " " + person["RemarkName"] + " " + person["UserName"])
	if len(searchedList) > 1:
		contactToId = input("请输入需要联系的人员或群ID:")
	else:
		contactToId = searchedList[0]["UserName"]
	
	wxMessage = input("请输入消息:\n")

if __name__ == "__main__":
	main()