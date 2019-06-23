import os,sys

# 结束进程,不再执行后面的内容
# os._exit(0)	# 等同于sys.exit()

try:
	sys.exit('hello world')
except SystemExit as e:		# 捕获退出信息
	print('退出',e)
print('process exit')