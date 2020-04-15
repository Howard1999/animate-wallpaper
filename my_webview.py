import webview as wv

def get_webview(title, url):
	view = wv.create_window(title, url, fullscreen=True)
	wv.start(view)
	
if __name__=='__main__':
	get_webview('hello world')

