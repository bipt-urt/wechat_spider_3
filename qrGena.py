# Author GiganticGragonfly
# generate QRcode for WeChat(Tencent) login
# QRcode will be saved at : img\gena\qr**********.png
# ----------------------------------------
# require PIL and qrcode and Image 
# maybe need PlL

import uuidGet
import qrcode
def getQR():
	#print("getQR") 
	uuAns = uuidGet.getUuid()
	print(uuAns[0])
	if uuAns[1]==True:
		print ('uuid is:'+uuAns[0])
		url = "https://login.weixin.qq.com/l/"+uuAns[0]
		qrcode.make(url).save('img\gena\qr'+uuAns[0][0:9] +'.png')
		print('---------QRcode image is already save as :\n---------img\gena\qr'+uuAns[0][0:9] +'.png')
		return (uuAns[0],url)
	elif uuAns[1]==False:
		print ("Get uuid falied , try to do it again")
		return None





def main():
	print("qrGet.py")

if __name__ == "__main__":
	main()