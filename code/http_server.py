from socket import *


def handleClient(c):
	request = c.recv(4096)
	request_lines = request.splitlines()
	for line in request_lines:
		print(line.decode())
	try:
		f = open('index.html')
	except IOError:
		response = 'HTTP/1.1 404 not found\r\n'
		response += '\r\n'		# 空行
		response += '===Sorry not found==='
	else:
		response = 'HTTP/1.1 200 OK\r\n'
		response += '\r\n'		# 空行
		response += f.read()
		f.close()
	finally:
		c.send(response.encode())
		

# 创建套接字
def main():
	s = socket(AF_INET,SOCK_STREAM)
	s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	s.bind(('0.0.0.0',9999))
	s.listen(5)
	print('listen to the post 9999')
	while True:
		c,addr = s.accept()
		print('Connect from',addr)
		# 处理请求
		handleClient(c)
		c.close()
	s.close()

if __name__ == '__main__':
	main()
