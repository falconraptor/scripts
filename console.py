import sys
from time import sleep

class Progress:
	def __init__(self, title='', length=40):
		self.length = length
		text = "-" * self.length + "] 00%"
		sys.stdout.write(title + ": [" + text + chr(8) * len(text))
		sys.stdout.flush()

	def progress(self, x):
		x_char = int(x * self.length // 100)
		text = "#" * x_char + "-" * (self.length - x_char) + "]" + ' {:02d}%'.format(x)
		sys.stdout.write(text + chr(8) * len(text))
		sys.stdout.flush()
		progress_x = x_char


	def endprogress(self, ):
		sys.stdout.write("#" * self.length + "] 100%\n")
		sys.stdout.flush()

progress = Progress('test', length=10)
for x in range(10):
	progress.progress(x*10)
	sleep(1)
progress.endprogress()