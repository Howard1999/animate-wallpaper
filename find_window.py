import win32gui, win32con

_WorkerW_list = []

def is_WorkerW(hwnd):
	className = win32gui.GetClassName(hwnd)
	return className == 'WorkerW'

def win_enum_handler(hwnd, ctx):
	if is_WorkerW(hwnd):
		_WorkerW_list.append(hwnd)

def get_WorkerW():
	win32gui.EnumWindows(win_enum_handler, None)
	return _WorkerW_list[len(_WorkerW_list)-1]
	
def set_parent(view, hwnd):
	win32gui.SetParent(view, hwnd)
	
def get_window_id(class_name = None, title = None):
	return win32gui.FindWindow(class_name, title)

	