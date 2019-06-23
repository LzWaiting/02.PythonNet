'''此示例示意套接字对象属性'''
from socket import *

s = socket()

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 	# 设置立即释放

print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))	# 获取套接字选项值 1

print(s.family)						# --> AddressFamily.AF_INET
print(s.type)						# --> SocketKind.SOCK_STREAM

s.bind(('192.168.10.105',8888)) 	
print(s.getsockname())				# --> ('192.168.10.105', 8888)

print(s.fileno())					# --> 3	本地一般从3开始
# sys.stdin.fileno()				# --> 0
# sys.stdout.fileno()				# --> 1
# sys.stderr.fileno()				# --> 2

s.listen(5)
c,addr = s.accept()
print('Connect from %s'%c.getpeername())		# 客户端连接套接字对应地址('192.168.10.105', 44968)
