import random
import os
import time
import app
import webbrowser

def bootscr():
    os.system("clear")
    load = "########"
    loadb = "########"
    for i in range(6):
        os.system("clear")
        boottxt = open("txt/boot.txt", "r")
        print(boottxt.read())
        print(" ")
        print("            " + load)
        load = load + loadb
        time.sleep(0.5)
    os.system("clear")
    time.sleep(0.75)
    return

def home():
    def prnt():
        os.system("clear")
        homtxt = open("txt/hom.txt", "r")
        print(homtxt.read())

    prnt()
    while True:
        x = input("/~# ")

        if x == "1":
            app.files()
            prnt()

        elif x == "2":
            app.google()

        elif x == "3" or x == "terminal":
            app.terminal()
            prnt()
        
        elif x == "clear":
            prnt()

        elif x == "g":
            helptxt = open("txt/help.txt", "r")
            print(helptxt.read())

        elif x == "exit":
            return
        
        else:
            inctxt = open("txt/inc.txt", "r")
            print(inctxt.read())

def files():
    while True:
        def prnt():
            os.system("clear")
            filtxt = open("txt/fil.txt", "r")
            print(filtxt.read())
        
        prnt()
        os.chdir("filesys")
        os.system("ls")
        
        while True:
            file = input("$~# ")
            if file == "exit":
                os.chdir("..")
                return

            elif file == "ls":
                os.system("ls")

            elif file.split()[0] == "nano":
                os.system(file)

            elif file.split()[0] == "cd":
                os.chdir(file.split()[1])

            elif file.split()[0] == "rm" or file.split()[0] == "remove":
                os.system("rm -r " + file.split()[1])
                print("Removed " + file.split()[1])

            elif file.split()[0] == "add" or file.split()[0] == "touch":
                os.system("touch " + file.split()[1])

            elif file.split()[0] == "mkdir":
                os.system(file)

            elif file == "clear":
                os.chdir("..")
                prnt()
                os.chdir("filesys")

            else:
                print("# Not a recognised command")


def google():
    while True:
        ur = str(input("]~# "))
        url = "https://" + ur
        webbrowser.open(url)
        return

def terminal():
    def prnt():
        os.system("clear")
        tertxt = open("txt/terminal.txt", "r")
        print(tertxt.read())

    
    prnt()
    os.chdir("filesys")

    while True:
        terminal = input("@~# ")

        if terminal == "exit":
            os.chdir("..")
            return
        elif terminal == "clear":
            os.chdir("..")
            prnt()
            os.chdir("filesys")
        else:
            os.system(terminal)