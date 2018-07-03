# Author GiaganticDragonbfly
# for decodeing base64 data
# defalut save as .jpg
import pickle
import base64
def deFace(faceID):
	faceData = base64.b64decode(faceID[20:]) #de sucess!!
	pic = open('img\\face\head.jpg','wb')
	pic.write(faceData)
	pic.close()
