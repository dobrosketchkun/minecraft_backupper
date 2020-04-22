from datetime import timedelta 
import os
import zipfile
import datetime
import time
import winsound
import keyboard 
import platform


#### CONFIG
BACKGROUND_COLOR = '1' #You can only use this values: 0 to 9, A, B, C, D, E, F'
TEXT_COLOR = '7' #You can only use this values: 0 to 9, A, B, C, D, E, F'
INTERVAL = 10
MINUTES_OR_SECONDS = 'minutes' #minutes or seconds
HOTKEY_SAVE = 'v' # ctrl + this key
HOTKEY_EXIT = '/' # ctrl + this key
PATH = r""
# PATH = r"C:\Users\dobrosketchkun\AppData\Roaming\.minecraft\saves\totaly random world" # insert a path (for instance r"C:\Users\username\AppData\Roaming\.minecraft\saves\MyWorld")
BEEP = True #if True will beep, if False will not
############

assert int(hex(int('0x' + BACKGROUND_COLOR.upper(), 16)), 16) <= 15, 'You can only use this values: 0 to 9, A, B, C, D, E, F'
assert int(hex(int('0x' + TEXT_COLOR.upper(), 16)), 16) <= 15, 'You can only use this values: 0 to 9, A, B, C, D, E, F'
os.system('color ' + BACKGROUND_COLOR.upper() + TEXT_COLOR.upper())

screen_text = '''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░███╗░░░███╗██╗███╗░░░██╗███████╗░██████╗██████╗░░█████╗░███████╗████████╗░░░░
░░░░████╗░████║██║████╗░░██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝░░░░
░░░░██╔████╔██║██║██╔██╗░██║█████╗░░██║░░░░░██████╔╝███████║█████╗░░░░░██║░░░░░░░
░░░░██║╚██╔╝██║██║██║╚██╗██║██╔══╝░░██║░░░░░██╔══██╗██╔══██║██╔══╝░░░░░██║░░░░░░░
░░░░██║░╚═╝░██║██║██║░╚████║███████╗╚██████╗██║░░██║██║░░██║██║░░░░░░░░██║░░░░░░░
░░░░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═══╝╚══════╝░╚═════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██████╗░░█████╗░░██████╗██╗░░██╗██╗░░░██╗██████╗░██████╗░███████╗██████╗░░░░░
░░░░██╔══██╗██╔══██╗██╔════╝██║░██╔╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗░░░░
░░░░██████╔╝███████║██║░░░░░█████╔╝░██║░░░██║██████╔╝██████╔╝█████╗░░██████╔╝░░░░
░░░░██╔══██╗██╔══██║██║░░░░░██╔═██╗░██║░░░██║██╔═══╝░██╔═══╝░██╔══╝░░██╔══██╗░░░░
░░░░██████╔╝██║░░██║╚██████╗██║░░██╗╚██████╔╝██║░░░░░██║░░░░░███████╗██║░░██║░░░░
░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n
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

def the_job(type):
	if type == 'hotkey':
		text = 'Hotkey:\tBacking up '
		post = '._hotkey.zip'
	elif type == 'auto':
		text = 'Auto:\tBacking up '
		post = '.zip'
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



if MINUTES_OR_SECONDS == 'minutes':
	timedel = lambda x: timedelta(minutes=x)
elif MINUTES_OR_SECONDS == 'seconds':
	timedel = lambda x: timedelta(seconds=x)
else:
	print('You can only use "minutes" or "seconds" for MINUTES_OR_SECONDS parameter')
	exit()


###
now = datetime.datetime.now()

_first_line = 'This program will back up your world "' + PATH.split('\\')[-1] +'" folder' +\
		' every ' + str(INTERVAL) + ' ' + MINUTES_OR_SECONDS + ' from ' +\
		now.strftime("%Y-%m-%d %H:%M:%S") + '\n'

_second_line =  'You can use hotkeys Ctrl+' + HOTKEY_SAVE +\
		' for manualy backing it up and Ctrl+' + HOTKEY_EXIT + ' for exit the program.\n\nLog:\n'

printed(screen_text + _first_line + _second_line)

###

_time_to_act = now + timedel(INTERVAL)
time_to_act = _time_to_act.strftime("%Y-%m-%d %H:%M:%S")

while True: 
	_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	if _now != time_to_act:
		pass
	if _now == time_to_act:
		the_job('auto')
		_time_to_act = _time_to_act + timedelta(seconds=INTERVAL)
		time_to_act = _time_to_act.strftime("%Y-%m-%d %H:%M:%S")



	ctrl = keyboard.is_pressed('ctrl') 
	save_key = keyboard.is_pressed(HOTKEY_SAVE)
	exit_key = keyboard.is_pressed(HOTKEY_EXIT)
	if keyboard.read_key() == 'ctrl' and keyboard.read_key() == HOTKEY_SAVE:
		the_job('hotkey')
	if keyboard.read_key() == HOTKEY_SAVE and keyboard.read_key() == 'ctrl':
		the_job('hotkey')
	if keyboard.read_key() == 'ctrl' and keyboard.read_key() == HOTKEY_EXIT:
		print('Manual exit.')
		break
	if keyboard.read_key() == HOTKEY_EXIT and keyboard.read_key() == 'ctrl':
		print('Manual exit.')
		break
