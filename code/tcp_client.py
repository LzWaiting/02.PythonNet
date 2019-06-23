'''此示例示意tcp套接字客户端编程
'''
from socket import *

# 1. 创建客户端套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 2. 发起连接
server_addr = ('192.168.10.105',8888)
sockfd.connect(server_addr)

while True:
	# 3. 消息收发
	data = input('发送>>')
	if not data:
		break
	sockfd.send(data.encode())
	data = sockfd.recv(1024)
	print(data.decode())

# 4. 关闭套接字
sockfd.close()
