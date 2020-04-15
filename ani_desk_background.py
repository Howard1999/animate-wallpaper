from find_window import *
from my_webview import *
from threading import Thread
import time

title = 'temp'
url = 'https://www.google.com/'

def setup_wallpaper():
	time.sleep(2)#wait for webview
	w = get_WorkerW()
	v = get_window_id(None, title)
	set_parent(v,w)

t = Thread(target = setup_wallpaper)
t.start()

get_webview(title, url)
