import urilib.parse 
import urllib.request 





def getUuid():
	print("getUuid")
	url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb"
	uuid = 'fail'
	flag = False


	uuid = 'test'
	flag = True
	return [uuid,flag]

def main():
	print("uuidGet.py")
	url = "http://127.0.0.1:8000/book" 
	params = { 'name':'浮生六记', 'author':'沈复' } 
	data = bytes(urllib.parse.urlencode(params), encoding='utf8') 
	response = urllib.request.urlopen(url, data=data)
	print(response.read().decode('utf-8'))


if __name__ == "__main__":
	main()