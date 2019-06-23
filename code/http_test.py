from socket import *

# 1. 创建tcp套接字
s = socket(AF_INET,SOCK_STREAM)

# 2. 绑定服务端地址
s.bind(('0.0.0.0',8000))

# 3. 设置监听套接字 
s.listen(5)

while True:
	# 4. 等待处理客户端连接请求
	c,addr = s.accept()
	print('Connect from',addr) 
	data = c.recv(4096)
	print('*********************')
	print(data.decode())		# 浏览器发来的http 请求
	print('*********************')
	data = '''HTTP/1.1 200 OK
	Content-Encoding:gzip
	Content-Type:text/html

	<h1>Welcome to tedu</h1>
	<p>这是一个测试</p>	
	'''
	c.send(data.encode())
	c.close()

s.close()