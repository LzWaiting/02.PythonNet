from socket import *

# 1. 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 2. 设置套接字可以发送接收广播
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# 3. 绑定固定接收端口
sockfd.bind(('0.0.0.0',9999))

while True:
	try:
		msg,addr = sockfd.recvfrom(1024)
		print('从{}获取信息：{}'.format(addr,msg.decode()))
	except (KeyboardInterrupt,SyntaxError):
		raise
	except Exception as e:
		print(e)

sockfd.close()
