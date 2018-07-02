# Author GiganticDragonfly
##### for login fuction
import urllib.parse 
import urllib.request 
import urllib
import time

from http.cookiejar import LWPCookieJar
from http.cookiejar import CookieJar

def login_prep(uuAns):
	url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login"
	#r=-1243780070&_=1530252136911
	params = {'loginicon':'true','uuid':uuAns[0],'tip':'1'}
	data = bytes(urllib.parse.urlencode(params), encoding='utf8')
	response = urllib.request.urlopen(url, data=data)
	str=response.read().decode('utf-8')

	while str.find('200') == -1:
		time.sleep(1)
		response = urllib.request.urlopen(url, data=data)
		str=response.read().decode('utf-8')
	#faceID = str[37:2437]
	return str

def loging(uuAns,url):
	
	if url.find('200') != -1:
		ticket = url[101:136]
		print(ticket)
		url = url[38:183]+ '&fun=new'#+"&fun=new&version=v2&lang=zh_CN",headers=header
		print(url)
		#act like a true explorer
		#user_agent = ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req)
		data = response.read().decode("utf-8","replace")
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

		return (ticket,pass_ticket,skeys,wxsid,wxuin)
	else :
		print('---------failed!!! \n --------- getting ticket failed!!!')
	return
	
###   need response like this:
#<error><ret>0</ret><message></message>
# <skey>@crypt_bb0777dc_10d27d54e309e1a46b95f20e06e9b67d</skey>
# <wxsid>0O3+4pKBU5vJO3ig</wxsid>
# <wxuin>1952541924</wxuin>
# <pass_ticket>POZDlX4AL2nwMFPvoZviOqhycYVka%2BJiP84Jq4B6WsliMvVhkUVvaLUmuZ6tZ3nk</pass_ticket>
# <isgrayscale>1</isgrayscale></error>




