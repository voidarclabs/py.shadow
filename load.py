import time
import os
import random

def msg(num):
    msg = open("msg.txt", "r")
    x = msg.readlines()
    for i in range(num):
        print(random.choice(x))
        time.sleep(1)