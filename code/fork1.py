import os 
from time import sleep

pid = os.fork()

if pid < 0:
	print('Create process failed')
elif pid == 0:
	sleep(1)
	print('Child get pid:',os.getpid())
	print('Child get parent pid',os.getppid())
else:
	print('parent get child pid:',pid)
	print('parent get pid',os.getpid())