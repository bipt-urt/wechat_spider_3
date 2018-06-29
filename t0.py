# test 0 
# for testing QRcode generation fuctionality
import qrGena
import uuidGet
import time
qrAns = qrGena.getQR()
print("---"+qrAns[0])

uuidGet.getFace(qrAns[0])
