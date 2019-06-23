'''此示例示意udp套接字服务端流程'''
from socket import *

# 1. 创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 2. 绑定服务端地址
server_addr = ('0.0.0.0',9999)
sockfd.bind(server_addr)

while True:
	# 3. 数据收发
	data,addr = sockfd.recvfrom(1024)
	if not data:
		break
	print('Receive from %s:%s'%(addr,data.decode()))
	sockfd.sendto('已收到你的消息'.encode(),addr)

# 4. 关闭udp套接字
sockfd.close()