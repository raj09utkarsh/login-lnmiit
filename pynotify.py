import platform
import os


def notify(title, message):
	if platform.system() == 'Darwin':
		cmd = 'osascript -e' + "'" + 'display notification' + '"' + f'{message}' + '"'  + 'with title' + '"' + f'{title}' +'"' + "'"
		os.system(cmd)
	elif platform.system() == 'Windows':
		pass
	elif platform.system() == 'Linux':
		pass
	else:
		pass
