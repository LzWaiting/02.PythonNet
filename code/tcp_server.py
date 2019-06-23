'''此示例示意tcp套接字服务端编程
'''
from socket import *

# 1. 创建服务端套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 2. 绑定客户端地址
sockfd.bind(('0.0.0.0',9999))

# 3. 设置监听套接字
sockfd.listen(5)

while True:
	# 4. 等待接受连接
	print('Waiting for connect...')
	connfd,addr = sockfd.accept()
	print('connect from',addr)

	while True:
		# 5. 消息收发
		data = connfd.recv(1024)	# 1024服务端接收缓冲区大小
		if not data:
			break
		print(data.decode())
		n = connfd.send(b'Receive your message')
		print('发送了%d字节'%n)

	# 6. 关闭套接字
	connfd.close()

sockfd.close()


# 另开一个终端
# $ telnet 127.0.0.1 8888