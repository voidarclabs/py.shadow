from collections.abc import Callable, Iterable, Mapping
import os
import random
from typing import Any
import gtts
import threading
import time
import sys
try:
    import msvcrt  # For Windows
except ImportError:
    import tty
    import termios  # For Unix

def get_key():
    if sys.platform == 'win32':
        return msvcrt.getch().decode()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def boilerplatelol():
    l = list(fi[char[0]])
    l.pop(char[1])
    l.insert(char[1],mem)
    fi[char[0]] = ''.join(l)

    for i in range(top , bottom):
        print(fi[i])

def main():
    global char
    global file
    global top
    global bottom
    sys.stdout.flush()
    print("GAY")
    while True:
        key = get_key()
        if key == '\x1b':  # Escape key
            key += get_key() + get_key()
            if key == '\x1b[A':

                print('balls')
                boilerplatelol()
                print('balls')

                
                if char[0] - 1 < 0:
                    if len(file[char[0] - 1]) +1  < char[1]:
                        char[1] = len(file[char[0] + 1] ) -1
                    char[0] = 0
                else:
                    if len(file[char[0] - 1]) -1  < char[1]:
                        char[1] = len(file[char[0] + 1] ) -1
                    char[0] = char[0] - 1

                if char[0] < top and char[0] > 0:
                    top = top - 1
                    bottom = bottom - 1

            elif key == '\x1b[B':
                boilerplatelol()

                
                if char[0] + 1 > len(file)-1:
                    if len(file[char[0] + 1]) +1  < char[1]:
                        char[1] = len(file[char[0] + 1] ) -1
                    char[0] = len(file) - 1
                else:
                    if len(file[char[0] + 1]) -1  < char[1]:
                        char[1] = len(file[char[0] + 1] ) -1
                    char[0] = char[0] + 1

                if char[0] > bottom and char[0] > len(file):
                    top = top + 1
                    bottom = bottom + 1
            elif key == '\x1b[C':
                boilerplatelol()
                char[1] +=1
                

            elif key == '\x1b[D':
                boilerplatelol()
                char[1] -= 1
                
        elif key.isalpha():
            file[char[0]] = file[char[0]][char[1]:] + key + file[char[0]][:char[1]]

def edit(filename):
    global char
    global file
    global top
    global bottom

    if '.' not in filename:
        filename = filename + '.gay'
    else: pass

    if os.path.exists(filename) == True:
        print('pog')
        pass
    else:
        os.system('touch' + filename)
    file = open(filename ,'r+')
    file = file.read().splitlines()

    char = [0 , 0]
    top = 0
    bottom = 10
    th = thread1(file,char,top,bottom)
    th.start()
    time.sleep(2)
    main()

        
class thread1(threading.Thread):
    def __init__(self, file,ch,to,bo):
        super(thread1,self).__init__()
        self.file = file
        self.char = ch
        self.top = to
        self.bottom = bo
    def run(self) -> None:
        global char
        global mem
        global fi
        fi = self.file
        d = 0
        mem = ''
        while True:
            os.system('clear')
            
            if d == 1:
                mem = fi[char[0]][char[1]]
                l = list(fi[char[0]])
                l.pop(char[1])
                l.insert(char[1],'█')
                fi[char[0]] = ''.join(l)
                
                d = 0
            else:
                l = list(fi[char[0]])
                l.pop(char[1])
                l.insert(char[1],mem)
                fi[char[0]] = ''.join(l)
                d+=1

            for i in range(self.top , self.bottom):
                print(fi[i])
                
            
            time.sleep(0.5)