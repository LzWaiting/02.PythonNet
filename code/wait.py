import os
from time import sleep

pid = os.fork()

if pid < 0:
	print('Create process failed')
elif pid == 0:
	sleep(3)
	print('Child process exit',os.getpid())
	os._exit(2)
else:
	# pid,status = os.wait()
	while True:
		sleep(1)
		# 通过非阻塞形式捕获子进程退出
		pid,status = os.waitpid(-1,os.WNOHANG)
		print(pid,status)
		print(os.WEXITSTATUS(status))	# 获取子进程状态
		if pid != 0:
			break
	while True:
		pass

