# test 0 
# for testing QRcode generation fuctionality
import qrGena
import uuidGet
import time
import login
####ALL PROGRAMME STARTS HERE
uuAns = uuidGet.getUuid()
qrAns = qrGena.getQR(uuAns)
print("---"+qrAns[0])
uuidGet.getFace(qrAns[0])
str=login.login_prep(uuAns)
login.login_prep(uuAns)
login.loging(uuAns,str)
