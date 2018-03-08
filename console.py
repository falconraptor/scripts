from sys import stdout
from time import sleep


class Progress:
    def __init__(self, title='', length=80):
        self.length = length
        text = '-' * self.length + '] 00%'
        stdout.write(title + ': [' + text + chr(8) * len(text))
        stdout.flush()

    def value(self, x):
        x_char = int(x * self.length // 100)
        text = '#' * x_char + ' ' * (self.length - x_char) + ']' + ' {:02d}%'.format(x)
        stdout.write(text + chr(8) * len(text))
        stdout.flush()

    def finish(self):
        stdout.write('#' * self.length + '] 100%\n')
        stdout.flush()


progress = Progress('test', length=10)
for x in range(10):
    progress.value(x * 10)
    sleep(1)
progress.finish()
