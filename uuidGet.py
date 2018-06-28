import urilib.parse 
import urllib.request 

def getUuid():
	print("getUuid")
	url="https://login.wx.qq.com/jslogin"
	params = {'appid':'wx782c26e4c19acffb'}
	uuid = 'fail'
	flag = False
	data = bytes(urllib.parse.urlencode(params), encoding='utf8')
	response = urllib.request.urlopen(url, data=data)
	print(response.read().decode('utf-8')
	out=[uuid,flag]
	return out

def main():
	print("uuidGet.py")
	getUuid()
)


if __name__ == "__main__":
	main()