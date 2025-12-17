import pyperclip
import sys
from pynput.keyboard import Controller,Key
import time

key = Controller()
def paste():
    if sys.platform == "win32":
        with key.pressed(Key.ctrl):
            key.press('v')
            key.release('v')
        print("chala")
    else :
        with key.pressed(Key.cmd):
            key.press('v')
            key.release('v')
        print("ghuma")

def copy():
    first = None
    try :
        while True :
            take = pyperclip.paste()
            if take != first :
                print(f"{take}")
                first = take
            time.sleep(.5)
    except KeyboardInterrupt:
        print("null")
if __name__ == "__main__":
    copy()
