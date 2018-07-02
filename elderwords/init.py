# init wechat 
import urllib.parse 
import urllib.request 
import time
import json
import http
from http.cookiejar import LWPCookieJar
from http.cookiejar import CookieJar
import login

def initing(uuAns,tiks):
	# HTTPS准备
	cookie_support = urllib.request.HTTPCookieProcessor(LWPCookieJar())
	opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CookieJar()))
	opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
	urllib.request.install_opener(opener)

	url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit"
	params = {'r':'-1504287718','pass_ticket':tiks[1]}
	data = json.dumps(params).encode('utf-8')
	request = urllib.request.Request(url=url, data=data)
	response = opener.open(request)
	data = response.read().decode('utf-8', 'replace')
	print(data)
	
	return response
