import os
import zipfile
import datetime
import time
import winsound
import platform
import readchar

#### CONFIG
BACKGROUND_COLOR = '0' #You can only use this values: 0 to 9, A, B, C, D, E, F'
TEXT_COLOR = 'a' #You can only use this values: 0 to 9, A, B, C, D, E, F'
HOTKEY_EXIT = b'\x10' #ctrl + p
HOTKEY_SAVE = b'\x1a' #ctrl + z
PATH = r"" # insert a path (for instance r"C:\Users\username\AppData\Roaming\.minecraft\saves\MyWorld")
BEEP = True #if True will beep, if False will not
############

assert int(hex(int('0x' + BACKGROUND_COLOR.upper(), 16)), 16) <= 15, 'You can only use this values: 0 to 9, A, B, C, D, E, F'
assert int(hex(int('0x' + TEXT_COLOR.upper(), 16)), 16) <= 15, 'You can only use this values: 0 to 9, A, B, C, D, E, F'
os.system('color ' + BACKGROUND_COLOR.upper() + TEXT_COLOR.upper())

screen_text = '''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░███╗░░░███╗██╗███╗░░░██╗███████╗░██████╗██████╗░░█████╗░███████╗████████╗
░░░░████╗░████║██║████╗░░██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
░░░░██╔████╔██║██║██╔██╗░██║█████╗░░██║░░░░░██████╔╝███████║█████╗░░░░░██║░░░
░░░░██║╚██╔╝██║██║██║╚██╗██║██╔══╝░░██║░░░░░██╔══██╗██╔══██║██╔══╝░░░░░██║░░░
░░░░██║░╚═╝░██║██║██║░╚████║███████╗╚██████╗██║░░██║██║░░██║██║░░░░░░░░██║░░░
░░░░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═══╝╚══════╝░╚═════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██████╗░░█████╗░░██████╗██╗░░██╗██╗░░░██╗██████╗░███████╗██████╗░░░░░░░░░
░░░░██╔══██╗██╔══██╗██╔════╝██║░██╔╝██║░░░██║██╔══██╗██╔════╝██╔══██╗░░░░░░░░
░░░░██████╔╝███████║██║░░░░░█████╔╝░██║░░░██║██████╔╝█████╗░░██████╔╝░░░░░░░░
░░░░██╔══██╗██╔══██║██║░░░░░██╔═██╗░██║░░░██║██╔═══╝░██╔══╝░░██╔══██╗░░░░░░░░
░░░░██████╔╝██║░░██║╚██████╗██║░░██╗╚██████╔╝██║░░░░░███████╗██║░░██║░░░░░░░░
░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██╗░░██╗░██████╗░████████╗██╗░░██╗███████╗██╗░░░██╗░░░░░░░░░░░░░░░░░░░░░░
░░░░██║░░██║██╔═══██╗╚══██╔══╝██║░██╔╝██╔════╝╚██╗░██╔╝░░░░░░░░░░░░░░░░░░░░░░
░░░░███████║██║░░░██║░░░██║░░░█████╔╝░█████╗░░░╚████╔╝░░░░░░░░░░░░░░░░░░░░░░░
░░░░██╔══██║██║░░░██║░░░██║░░░██╔═██╗░██╔══╝░░░░╚██╔╝░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██║░░██║╚██████╔╝░░░██║░░░██║░░██╗███████╗░░░██║░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n
'''

screen_state = ''

def screen_state_update(new):
	global screen_state
	screen_state += new

def clear_screen():
	command = "cls" if platform.system().lower()=="windows" else "clear"
	os.system(command)

def printed(text):
	global screen_state
	clear_screen()
	screen_state_update(text)
	print(screen_state)

def beepboop(): # you can change the melody by changing freq and time in winsound.Beep(freq, time)
	if BEEP:      # and smart use of time.sleep() 
		winsound.Beep(300, 100)
		time.sleep(0.1)
		winsound.Beep(200, 100)
		time.sleep(0.1)
		winsound.Beep(500, 100)
		time.sleep(0.1)

def zipdir(path, ziph):
	for root, dirs, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file))

def the_job():

	text = 'Hotkey:\tBacking up '
	post = '._hotkey.zip'

	global PATH
	if BEEP:
		winsound.Beep(300, 100)
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	file_name = str(now) + '_' + PATH.split('\\')[-1] + post
	file_name = file_name.replace(' ', '_').replace(':', '-')
	_log = text + file_name + '... '
	printed(_log)
	zipf = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
	zipdir(PATH, zipf)
	zipf.close()
	beepboop()
	printed('\tDone.\n')

now = datetime.datetime.now()

_first_line = 'This program will back up your world "' + PATH.split('\\')[-1] +'" folder\n'

_second_line =  'You can use hotkeys Ctrl+z for manualy backing it up and Ctrl+p for exit the program.\n\nLog:\n'

printed(screen_text + _first_line + _second_line)

###



while True: 

	chars = readchar.readchar()
	if chars == HOTKEY_SAVE:
		the_job('hotkey')
	if chars == HOTKEY_EXIT:
		print('Manual exit.')
		break
