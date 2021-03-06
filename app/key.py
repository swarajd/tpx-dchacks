#http://stackoverflow.com/questions/1823762/sendkeys-for-python-3-1-on-windows

import win32api
import win32con
import win32ui
import time,sys

keyDelay = 0.1
keymap = {
    "Up": ord("F"), #win32con.VK_UP, #forward
    "Left": ord("L"), #win32con.VK_LEFT, #left
    "Down": ord("B"), #win32con.VK_DOWN, #backward
    "Right": ord("R"), #win32con.VK_RIGHT, #right
    "b": ord("S"), #stop
    "a": ord("A"),
    "y": ord("Y"), #for NDS
    "x": ord("X"), #for NDS
    "s": ord("S"), #start
    "e": ord("E") #select
}

def sendKey(button):
    win32api.keybd_event(keymap[button], 0, 0, 0)
    time.sleep(keyDelay)
    win32api.keybd_event(keymap[button], 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == "__main__":
    win = win32ui.FindWindow(None, sys.argv[1])
    print(sys.argv[1])
    win.SetForegroundWindow()
    win.SetFocus()
    sendKey(sys.argv[2])
    print(sys.argv[2])
