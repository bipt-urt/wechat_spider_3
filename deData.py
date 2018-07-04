import json
import csv
import deHtml
import sys
import io

def deDa():
	with open("da.txt","r",encoding="utf8") as f:
		content = f.read()
		target = json.loads(content)
	mlist=target['MemberList']

	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
	with open("data.csv","w",encoding="gb18030",newline="") as datacsv:
		#dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
		csvwriter = csv.writer(datacsv,dialect = ("excel"))
		#csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
		csvwriter.writerow(['NickName','EncryChatRoomId', 'AttrStatus', 'UserName', 'SnsFlag', 'Province', 'Sex', 'StarFriend', 'IsOwner', 'Signature', 'City', 'PYQuanPin', 'AppAccountFlag', 'HideInputBarFlag', 'VerifyFlag', 'ContactFlag', 'Alias', 'PYInitial', 'MemberCount', 'OwnerUin', 'ChatRoomId', 'Uin', 'Statues', 'RemarkPYQuanPin', 'UniFriend', 'MemberList', 'HeadImgUrl', 'RemarkPYInitial', 'DisplayName', 'KeyWord', 'RemarkName'])
		for thing in mlist:
			for elemnent in thing:
				thing[elemnent]=deHtml.convert(str(thing[elemnent])).replace("\n","")
			datacsv.write(thing['NickName']+","+thing['EncryChatRoomId']+","+thing['AttrStatus']+","+thing['UserName']+","+thing['SnsFlag']+","+thing[ 'Province']+","+thing[ 'Sex']+","+thing['StarFriend']+","+thing['IsOwner']+","+thing[ 'Signature']+","+thing['City']+","+thing['PYQuanPin']+","+thing['AppAccountFlag']+","+thing['HideInputBarFlag']+","+thing['VerifyFlag']+","+thing['ContactFlag']+","+thing['Alias']+","+thing['PYInitial']+","+thing['MemberCount']+","+thing['OwnerUin']+","+thing['ChatRoomId']+","+thing['Uin']+","+thing['Statues']+","+thing['RemarkPYQuanPin']+","+thing['UniFriend']+","+thing['MemberList']+","+thing['HeadImgUrl']+","+thing['RemarkPYInitial']+","+thing['DisplayName']+","+thing['KeyWord']+","+thing['RemarkName']+'\n')
