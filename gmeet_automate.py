from pynput.keyboard import Key, Controller
import time, os
keyboard = Controller()

browser = "google-chrome"
link = "gsy-rsek-zhj"

os.system("gnome-terminal -e '"+browser+" http://meet.google.com/"+link+"'")

def presstabkey(num, tym, keys):
	time.sleep(tym)
	while num > 0 :
		keyboard.press(keys)
		keyboard.release(keys)
		num = num-1
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)


presstabkey(7, 20, Key.tab)
