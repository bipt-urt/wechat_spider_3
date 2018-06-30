# Author GiganticDragonfly
##### for login fuction
import urllib.parse 
import urllib.request 
import time
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
		url = url[38:183]
		print(url)
		#act like a true explorer
		headers = {
		'GET https':'//weibo.cn/5273088553/info HTTP/1.1',
		'Host':' weibo.cn',
		'Connection':' keep-alive',
		'Upgrade-Insecure-Requests':' 1',
		'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
		'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Language':' zh-CN,zh;q=0.9',
		#'Cookie':' _T_WM=c1913301844388de10cba9d0bb7bbf1e; SUB=_2A253Wy_dDeRhGeNM7FER-CbJzj-IHXVUp7GVrDV6PUJbkdANLXPdkW1NSesPJZ6v1GA5MyW2HEUb9ytQW3NYy19U; SUHB=0bt8SpepeGz439; SCF=Aua-HpSw5-z78-02NmUv8CTwXZCMN4XJ91qYSHkDXH4W9W0fCBpEI6Hy5E6vObeDqTXtfqobcD2D32r0O_5jSRk.; SSOLoginState=1516199821',
		}

		#params = {'loginicon':'true','uuid':uuAns[0],'tip':'1'}
		#data= bytes(urllib.parse.urlencode(params), encoding='utf8')
		response = urllib.request.urlopen(url).read()
		print(response)
		print(response.find('pass_ticket'))
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




