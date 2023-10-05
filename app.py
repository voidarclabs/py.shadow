import random
import os
import time
import app
import webbrowser
import edit
from playsound import playsound as ps
from supermail import EmailClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import zipfile
import glob

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

        elif x == "3":
            app.terminal()
            prnt()

        elif x == '4':
            app.email()
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

            elif file.split()[0] == 'edit':
                # edit.edit(file.split()[1])
                # 
                ## WARNING
                ## This code is not currently stable. Do not use!
                #
                print("Under production")

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

            elif file.split()[0] == 'play':
                ps(file.split()[1])

            elif file.split()[0] == 'help':
                help = open('../txt/filhelp.txt', 'r')
                print(help.read())

            else:
                print("# Not a recognised command. \n # Check documentation for more info")


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

def nano(file):
    os.system(f'nano {file}')
global logincred

def email():
    def prnt():
        os.system("clear")
        emtxt = open("txt/email.txt", "r")
        print(emtxt.read())

    def createlogin():
        try:
            os.system('rm login.txt')
        except:
            pass
        os.system('touch login.txt')
        loginfile = open('login.txt', 'w')
        loginfile.write(input('input email: '))
        loginfile.write('\n')
        loginfile.write(input('input password: '))
        loginfile.close()
        pass

    def login():
        global logincred
        logincred = open('login.txt', 'r')
        logincred = logincred.read()
        logincred = logincred.splitlines()
        if logincred == []:
            createlogin()
        else:
            pass

        logincred = open('login.txt', 'r')
        logincred = logincred.read()
        logincred = logincred.splitlines()
        
        if gmailchecker(logincred[0], logincred[1]) == True:
            print('Logged in!')
            pass
        else: 
            createlogin()


    def gmailchecker(username,password):
        import smtplib as s

        ID = username
        PASSW = password

        server = s.SMTP("smtp.gmail.com", 587)
        server.starttls()
        if server.login(ID,PASSW):
            server.quit()
            return True
        else:
            server.quit()
            return

    def getmail():
        webbrowser.open('https://mail.google.com')

    def writemail():
        try:
            os.system('rm email.txt')
        except:
            pass
        
        os.system('touch email.txt')
        nano('email.txt')

    def sendmail():
        writemail()
        recipient = input('Recipient: ')
        subject = input('Subject: ')
        text = open('email.txt', 'r')
        cc = input('CC: ')
        attach = input('Attachments:')
        

        email_user = logincred[0]
        email_password = logincred[1]
        email_rcver = recipient

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_rcver
        msg['Cc'] = cc
        msg['Subject'] = subject

        body = text.read()
        msg.attach(MIMEText(body, 'plain'))

        if attach != '':
            attachment = open(attach, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('content-disposition', 'attachment; filename=' + attach)
            msg.attach(part)
        else:
            pass

        text = msg.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        
        try:
            server.sendmail(email_user, email_rcver, text)
            server.quit()
            print("\nEmail Sent!\n")
            os.system('rm email.txt')
        except:
            try:
                server.quit()
            except:
                pass
            print('Unknown error. Please try again.')

    def mainloop():
        while True:
            email = input('E~# ')
            if email == 'readmail' or email == 'read':
                getmail()
            elif email == 'sendmail' or email == 'send':
                sendmail()
            elif email == 'help':
                emtxt = open("txt/emhelp.txt", "r")
                print(emtxt.read())
            elif email == 'clear':
                prnt()
            elif email == 'exit':
                break
            else:
                print("Command not recognised. Use 'help' for help")

    prnt()
    login()
    mainloop()
    
    
