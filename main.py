"""

- Start ultility
- Click 'live view'
- Resize and arrange two windows

- Focus on EOS M200 and click shutter button
- Close `快速预览` windows

"""

import win32api

import win32con
import win32gui


def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

handles = []

def f(handle, arg):
    handles.append(handle)
    pass

win32gui.EnumWindows(f, handles);

for i in range(len(handles)):
    print(i, win32gui.GetWindowText(handles[i]))

n = int(input())

handle = handles[n]

rect = win32gui.GetWindowRect(handle)
print(rect)

