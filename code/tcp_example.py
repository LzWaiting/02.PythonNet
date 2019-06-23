'''服务端'''

from socket import *

# 1. 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 2. 绑定服务端地址
sockfd.bind('0.0.0.0',8888)

# 3. 设置监听套接字，创建监听列队
sockfd.listen(5)

# 4. 等待处理客户端连接请求
connfd,addr = sockfd.accept()	# connfd 客户端连接套接字，addr 客户端地址

# 5. 收接发数据
data = connfd.recv(1024)
n = connfd.send(b'相应回复信息')

# 6. 关闭套接字
connfd.close()
sockfd.close()


'''客户端'''

# 1. 创建客户端套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 2. 连接服务端地址
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

# 3. 接收发数据
data = input('发送>>')
sockfd.send(data.encode())
data = sockfd.recv(1024).decode()

# 4. 关闭套接字
sockfd.close()