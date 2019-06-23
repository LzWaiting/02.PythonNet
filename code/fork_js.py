import os
from time import sleep

def f1():
	sleep(3)
	print('第一件事')

def f2():
	sleep(4)
	print('第二件事')

pid = os.fork()

if pid < 0:
	print('Create process failed')
elif pid == 0:
	p = os.fork()	# 创建二级子进程
	if p == 0:
		f2()	# 做第二件事
	else:
		os._exit(0)
else:
	os.wait()	# 等一级子进程退出
	f1()	# 做第一件事