from socket import *
from time import sleep

# 设置目标地址
dest = ('192.168.10.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

# 设置能够发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
	sleep(2)
	try:
		s.sendto('来呀,带你去看蓝色土耳其'.encode(),dest)
	except (KeyboardInterrupt,SyntaxError):
		raise
	except Exception as e:
		print(e)

s.close()