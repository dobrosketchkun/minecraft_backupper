import os
import zipfile
import datetime
import time
import winsound
import keyboard 

#### CONFIG
INTERVAL = 10
MINUTES_OR_SECONDS = 'minutes' #minutes or seconds
HOTKEY_SAVE = 'v' # ctrl + this key
HOTKEY_EXIT = '/' # ctrl + this key
PATH = r"" # insert a path (for instance r"C:\Users\username\AppData\Roaming\.minecraft\saves\MyWorld")
BEEP = True #if True will beep, if False will not
############

screen_text = '''
    ███╗   ███╗██╗███╗   ██╗███████╗ ██████╗██████╗  █████╗ ███████╗████████╗
    ████╗ ████║██║████╗  ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
    ██╔████╔██║██║██╔██╗ ██║█████╗  ██║     ██████╔╝███████║█████╗     ██║   
    ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║     ██╔══██╗██╔══██║██╔══╝     ██║   
    ██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╗██║  ██║██║  ██║██║        ██║   
    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   
                                                                             
    ██████╗  █████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ ██████╗ ███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██████╔╝███████║██║     █████╔╝ ██║   ██║██████╔╝██████╔╝█████╗  ██████╔╝
    ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
    ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     ██║     ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                             
'''

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

def the_job_hotkey():
	global PATH
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	file_name = str(now) + '_' + PATH.split('\\')[-1] + '._hotkey.zip'
	file_name = file_name.replace(' ', '_').replace(':', '-')
	print('Hotkey: Backing up ' + file_name, end = '... ')
	zipf = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
	zipdir(PATH, zipf)
	zipf.close()
	beepboop()
	print('Done')

def the_job_auto():
	global PATH
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	file_name = str(now) + '_' + PATH.split('\\')[-1] + '.zip'
	file_name = file_name.replace(' ', '_').replace(':', '-')
	print('Auto: Backing up ' + file_name,  end = '... ')
	zipf = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
	zipdir(PATH, zipf)
	zipf.close()
	beepboop()
	print('Done')


if MINUTES_OR_SECONDS == 'minutes':
	_minutes_or_seconds = -2
elif MINUTES_OR_SECONDS == 'seconds':
	_minutes_or_seconds = -1
else:
	print('You can only use "minutes" or "seconds" for MINUTES_OR_SECONDS parameter')
	exit()

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now_s = now.split(':')[_minutes_or_seconds]
_interval_list = [str(int(t) + int(now_s[_minutes_or_seconds])) for t in range (0, 59, INTERVAL)]
interval_list = [('0' + _t) if len(_t) == 1 else _t for _t in _interval_list]

###

print(screen_text)
print('This program will back up your world "' + PATH.split('\\')[-1] +'" folder' +\
		' every ' + str(INTERVAL) + ' ' + MINUTES_OR_SECONDS + ' from ' + now + '\n' )
print('You can use hotkeys Ctrl+' + HOTKEY_SAVE +\
		' for manualy backing it up and Ctrl+' + HOTKEY_EXIT + ' for exit the program.\n')
print('Log:')


###

temp_time = None
isZero = False
while True: 
	_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	_now_s = _now.split(':')[_minutes_or_seconds]

	if not isZero:
		if _now_s in interval_list:
			the_job_auto()
			isZero = True
			temp_time = _now
	if _now != temp_time:
		isZero = False

	if keyboard.is_pressed('ctrl') and keyboard.is_pressed(HOTKEY_SAVE):  
		the_job_hotkey()
	if keyboard.is_pressed('ctrl') and keyboard.is_pressed(HOTKEY_EXIT):
		print('Manual exit.')
		break
