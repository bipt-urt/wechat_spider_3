import uuidGet
def getQR():
	print("getQR")
	uuAns = uuidGet.getUuid()
	print(uuAns[0])
	if uuAns[1]==True:
		print ('uuid is:'+uuAns[0])
	elif uuAns[1]==False:
		print ("Get uuid falied , try to do it again")




def main():
	print("qrGet.py")

if __name__ == "__main__":
	main()