import os


path = "./mypipe"

mode = 0o600

os.mkfifo(path, mode)
	
print("FIFO named '% s' is created successfully." % path)
