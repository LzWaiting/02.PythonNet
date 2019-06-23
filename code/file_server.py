'''通过tcp套接字完成一个文件的发送
将一个文件从客户端发给服务端,或者从服务端发送给客户端均可
文件可以是文本,也可以是图片'''

from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(('0.0.0.0',8888))

s.listen(5)

c,addr = s.accept()
print('Connect from',addr)

f = open('recv.jpg','wb')

while True:
	data = c.recv(4096)
	if not data:
		break
	f.write(data)

f.close()
c.close()
s.close()
