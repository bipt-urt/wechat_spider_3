import urllib
import urllib.request

print('2.py created')
alist = [1,2,3]
b = [1,2,3,alist]
c = [1,2,3,alist]
print(len(b))
_test123=[111,2]
print(_test123)
del b[1]
b.append('666')

print(b)
b.pop()
print(b)
b.pop(-1)
print(b[10:])
print(c)
c.pop(1)

print("______________________________________________")
c=[1,2,3,'4',5]
print(c)
print(c[-1])
print(c[-2])
print("______________________________________________")
path = r'c:\test.html'
print(path[:-4]+'htm')


print("______________________________________________")

uuAns = [1,2]
uuAns[0]

a='20fenernognei'
print(a.find('201'))


response = 'guirehguia23594uy23'
print(response.find('2359'))



a = "b'<error><ret>0</ret><message></message><skey>@crypt_bb0777dc_35847824ea29128f58f7bd252447a8cb</skey><wxsid>Oc+UvpZuA4fyLC8c</wxsid><wxuin>1952541924</wxuin><pass_ticket>bFSGvkYeMJltngiqco3udzmNM94gEiw5GS6I6Tt%2Bx3U6fagv8VZVzc%2BhOc6rMQGh</pass_ticket><isgrayscale>1</isgrayscale></error>'"
print(a[170:238])