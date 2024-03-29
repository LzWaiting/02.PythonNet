'''此示例示意udp数据报套接字使用流程'''

from socket import *
import sys

if len(sys.argv) < 3:
	print('''
		argv is error!
		run as
		python3 udp_client.py 127.0.0.1 8888
		''')
	raise

# 从命令行输入IP端口
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

# 1. 创建udp数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
	# 2. 数据收发
	data = input('消息：')
	if not data:
		break
	sockfd.sendto(data.encode(),ADDR)
	data,addr = sockfd.recvfrom(1024)	# 接收信息的数量，超出后丢失
	print('从服务器收到：%s'%data.decode())

# 3. 关闭数据报套接字
sockfd.close()