#HidachanBot v0.1.1ac--------a Twitch IRC bot By Joshua Powers
#Based on a project by Ryan Chesler https://youtu.be/sCagGV9Jl88
#Intended to work with Joycontrol by Robert Martin:
#                      https://github.com/mart1nro/joycontrol
#
#The versions marked with "ac" at the end are HidachanBot for ACNH
#builds. This build is not only game-specific, but intended for only
#changing the Reaction the character is using. If you're looking for
#the build that has all the buttons, look for the corresponding
#version without the "ac" in the version.
#
#Developed on a Raspberry Pi 3B utilizing Python 3.7.x in Raspbian
#

import socket
import pyautogui
import threading
import subprocess
import time

SERVER = "irc.twitch.tv" #Do not change this
PORT = 6667              #Do not change this
PASS = "oauth:" #You'll need an oauth for your bot to login
BOT = "yourbotname" #Your bot's name
CHANNEL = "channelname" #The channel your bot will attach to (You don't need the # before the channel name here)
OWNER = "yourname" #This will be your username
SWITCHBTMAC = "your switch's BT MAC address" #The Bluetooth MAC Address of your Switch. Before using the bot, start joycontrol and sync it to your switch. Near the top, it will have your Switch's BT MAC address. Put that here.
message = "" #Just declaring a string for later. Don't put anything here, please.
pyautogui.PAUSE = 0.2 #adjust the timing of calls

pyautogui.hotkey('alt', 'f2') #Opens a new terminal
time.sleep(0.5)
pyautogui.typewrite('lxterminal\n')
time.sleep(2.5) #Take into account load time of the terminal
pyautogui.typewrite('sudo python3 ~/joycontrol/run_controller_cli.py PRO_CONTROLLER -r ' + SWITCHBTMAC + '\n')
#The above command starts joycontrol--IT MUST BE THE ACTIVE WINDOW
#for the bot to work! You've been warned! If the bot's not working,
#check the active window! Also: if joycontrol doesn't start, you
#have this bot in the wrong folder--add it to where you have
#joycontrol installed!
time.sleep(10) #Take into account the amount of time it takes to
#sync with your switch

irc = socket.socket() #Twitch IRC connecty stuff.
irc.connect((SERVER, PORT))
irc.send(("PASS " + PASS + "\n" +
          "NICK " + BOT + "\n" +
          "JOIN #" + CHANNEL + "\n").encode())

def gamecontrol(): #if anyone says any of the below, press buttons!
    global message
    while True:
        if str.startswith(message.lower(), "!react1"):
            pyautogui.typewrite('zr\n')
            message = ""
            time.sleep(0.3)
            pyautogui.typewrite("stick l up\n")
            pyautogui.typewrite("stick l center\n")
            pyautogui.typewrite("a\n")
            time.sleep(0.3)
        elif str.startswith(message.lower(), "!react2"):
            pyautogui.typewrite('zr\n')
            message = ""
            time.sleep(0.3)
            pyautogui.typewrite("stick l h 3840 && stick l v 3840\n")
            pyautogui.typewrite("stick l center\n")
            pyautogui.typewrite("a\n")
            time.sleep(0.3)
        elif str.startswith(message.lower(), "!react3"):
            pyautogui.typewrite('zr\n')
            message = ""
            time.sleep(0.3)
            pyautogui.typewrite("stick l right\n")
            pyautogui.typewrite("stick l center\n")
            pyautogui.typewrite("a\n")
            time.sleep(0.3)
        elif str.startswith(message.lower(), "!react4"):
            pyautogui.typewrite('zr\n')
            message = ""
            time.sleep(0.3)
            pyautogui.typewrite("stick l h 3840 && stick l v 256\n")
            pyautogui.typewrite("stick l center\n")
            pyautogui.typewrite("a\n")
            time.sleep(0.3)
        elif str.startswith(message.lower(), "!react5"):
            pyautogui.typewrite('zr\n')
            message = ""
            time.sleep(0.3)
            pyautogui.typewrite("stick l down\n")
            pyautogui.typewrite("stick l center\n")
            pyautogui.typewrite("a\n")
            time.sleep(0.3)
        elif str.startswith(message.lower(), "!react6"):
            pyautogui.typewrite('zr\n')
            message = ""
            time.sleep(0.3)
            pyautogui.typewrite("stick l h 256 && stick l v 256\n")
            pyautogui.typewrite("stick l center\n")
            pyautogui.typewrite("a\n")
            time.sleep(0.3)
        elif str.startswith(message.lower(), "!react7"):
            pyautogui.typewrite('zr\n')
            message = ""
            time.sleep(0.3)
            pyautogui.typewrite("stick l left\n")
            pyautogui.typewrite("stick l center\n")
            pyautogui.typewrite("a\n")
            time.sleep(0.3)
        elif str.startswith(message.lower(), "!react8"):
            pyautogui.typewrite('zr\n')
            message = ""
            time.sleep(0.3)
            pyautogui.typewrite("stick l h 256 && stick left v 3840\n")
            pyautogui.typewrite("stick l center\n")
            pyautogui.typewrite("a\n")
            time.sleep(0.3)
        elif str.startswith(message.lower(), "!look"):
            pyautogui.typewrite('r\n')
            message = ""
        else:
            pass

def twitch():
    def joinchat(): #let's join the server!
        Loading = True
        while Loading:
            readbuffer_join = irc.recv(1024)
            readbuffer_join = readbuffer_join.decode()
            for line in readbuffer_join.split("\n")[0:-1]:
                print(line)
                Loading = loadingComplete(line)
            
    def loadingComplete(line): #let everyone know we've successfully joined
        if ("End of /NAMES list" in line):
            print ("Bot has joined #" + CHANNEL + "'s Channel!")
            sendMessage(irc, "Hello, everyone! :3 I'm here~!")
            return False
        else:
            return True

    def sendMessage(irc, message): #This is how we send messages!
        messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
        irc.send((messageTemp + "\n").encode())
    
    def getUser(line): #Someone sent a message? Who?
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    def getMessage(line): #Someone sent a message? What was it?
        global message
        try:
            message = (line.split(":",2))[2]
        except:
            message = ""
        return message

    def Console(line): #Someone maybe sent a command!
        if "PRIVMSG" in line:
            return False
        else:
            return True

    joinchat()

    while True:
        try:
            readbuffer = irc.recv(1024).decode() #check the readbuffer
        except: #if the readbuffer is empty, just drop it.
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            if "PING" in line and Console(line): #Get a ping? Send a pong!
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                irc.send(msgg)
                print("Ping? PONG!") #My way of telling you I'm alive!
                continue
            else:
                user = getUser(line)
                message = getMessage(line)
                print(user + " : " + message) #Someone said something!
                if str.startswith(message.lower(), "!help"):
                    sendMessage(irc, "Available commands: !react(1-8), !look. Have a wonderful and lovely day!")
                else:
                    pass

if __name__ == '__main__': #This lets me do two things at once!
    t1 = threading.Thread(target = twitch)
    t1.start()
    t2 = threading.Thread(target = gamecontrol)
    t2.start()
