'''通过tcp套接字完成一个文件的发送
将一个文件从客户端发给服务端,或者从服务端发送给客户端均可
文件可以是文本,也可以是图片'''

from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.connect(('192.168.10.105',8888))

f = open('send.jpg','rb')

while True:
	data = f.read(4096)
	if not data:
		break
	s.send(data)

f.close()
s.close()