# Author GiaganticDragonbfly
# for decodeing base64 data
# defalut save as .jpg
import pickle
import base64
def deFace(faceID):
	#faceID='b'+"'"+faceID+"'"
	faceID=base64.b64decode(faceID[20:])
	print(faceID)
	pic = open('img\\face\head.jpg','wb')
	pickle.dump(faceID,pic)
	pic.close()
