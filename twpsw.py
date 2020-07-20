#TwitchPlaysSwitch v0.1.1--------a Twitch IRC bot By Joshua Powers
#Based on a project by Ryan Chesler https://youtu.be/sCagGV9Jl88
#Intended to work with Joycontrol by Robert Martin:
#                      https://github.com/mart1nro/joycontrol
#
#Developed on a Raspberry Pi 3B utilizing Python 3.7.x in Raspbian
#
# Multi command
#  -So players can perform two or more commands simultaneously. This
#   is supported by joycontrol's "&&" operator. Since some games have
#   a soft reset multi-button command, I'll add a condition to check
#   if a player is using an undesirable button combination and ignore
#   it completely. This will be on a per game basis and needs to be
#   activated and configured manually. I'll be sure to leave a comment
#   pointing it out.
# Sleep timer between commands
#  -No stress testing has been done, yet. Because high traffic can
#   potentially cause problems for the bot, a sleep command needs to
#   be added, giving the bot long enough to relay the command to the
#   Switch. I'll make this final determination after performing a
#   stress test.
# Command queue
#  -Might be necessary for high volume chat traffic, especially if a
#   sleep timer is necessary.
# Macro capability
#  -Because of the capabilities of joycontrol and pyautogui, this
#   should be relatively easy to implement. What I would like to do
#   is have the keypresses imported from file. Because of the nature
#   of modern games and hardware, as well as Twitch stream delay,
#   having macro commands on hand would potentially make certain
#   games far more playable.
# Potential future controls?
#  -The only things that joycontrol currently CANNOT DO is motion
#   controls and holding down buttons. If these functions get added
#   in the future, you can be certain I'll add them to the bot.

import socket
import pyautogui
import threading
import subprocess
import time

SERVER = "irc.twitch.tv" #Do not change this
PORT = 6667              #Do not change this
PASS = "oauth:" #You'll need an oauth for your bot to login
BOT = "yourbotsname" #Your bot's name
CHANNEL = "your channel" #The channel your bot will attach to (You don't need the # before the channel name here)
OWNER = "ownername" #This will be your username
SWITCHBTMAC = "xx:xx:xx:xx:xx:xx" #The Bluetooth MAC Address of your Switch. Before using the bot, start joycontrol and sync it to your switch. Near the top, it will have your Switch's BT MAC address. Put that here.
message = "" #Just declaring a string for later. Don't put anything here, please.

pyautogui.hotkey('shift', 'ctrl', 'n') #Opens a new terminal
time.sleep(2.5) #Take into account load time of the terminal
pyautogui.typewrite('sudo python3 run_controller_cli.py PRO_CONTROLLER -r ' + SWITCHBTMAC + '\n')
#The above command starts joycontrol--IT MUST BE THE ACTIVE WINDOW
#for the bot to work! If the bot's not working, check the active window!
#Also: if joycontrol doesn't start, you have this bot in the wrong 
#folder--add it to where you have joycontrol installed!
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
        if str.startswith(message.lower(), "!up"):
            pyautogui.typewrite('up\n')
            message = ""
        elif str.startswith(message.lower(), "!down"):
            pyautogui.typewrite('down\n')
            message = ""
        elif str.startswith(message.lower(), "!a"):
            pyautogui.typewrite('a\n')
            message = ""
        elif str.startswith(message.lower(), "!b"):
            pyautogui.typewrite('b\n')
            message = ""
        elif str.startswith(message.lower(), "!x"):
            pyautogui.typewrite('x\n')
            message = ""
        elif str.startswith(message.lower(), "!y"):
            pyautogui.typewrite('y\n')
            message = ""
        elif str.startswith(message.lower(), "!l"):
            if str.startswith(message.lower(), "!left"):
                pyautogui.typewrite('left\n')
                message = ""
            elif str.startswith(message.lower(), "!ls"):
                if str.startswith(message.lower(), "!ls1"):
                    pyautogui.typewrite('stick left h 256 && stick left v 256\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick left center\n')
                elif str.startswith(message.lower(), "!ls2"):
                    pyautogui.typewrite('stick left down\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick left center\n')
                elif str.startswith(message.lower(), "!ls3"):
                    pyautogui.typewrite('stick left h 3840 && stick left v 256\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick left center\n')
                elif str.startswith(message.lower(), "!ls4"):
                    pyautogui.typewrite('stick left left\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick left center\n')
                elif str.startswith(message.lower(), "!ls5"):
                    pyautogui.typewrite('l_stick\n')
                    message = ""
                elif str.startswith(message.lower(), "!ls6"):
                    pyautogui.typewrite('stick left right\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick left center\n')
                elif str.startswith(message.lower(), "!ls7"):
                    pyautogui.typewrite('stick left h 256 && stick left v 3840\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick left center\n')
                elif str.startswith(message.lower(), "!ls8"):
                    pyautogui.typewrite('stick left up\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick left center\n')
                elif str.startswith(message.lower(), "!ls9"):
                    pyautogui.typewrite('stick left h 3840 && stick left v 3840\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick left center\n')
                else:
                    pyautogui.typewrite('l_stick\n')
                    message = ""
            else:
                pyautogui.typewrite('l\n')
                message = ""
        elif str.startswith(message.lower(), "!r"):
            if str.startswith(message.lower(), "!right"):
                pyautogui.typewrite('right\n')
                message = ""
            elif str.startswith(message.lower(), "!rs"):
                if str.startswith(message.lower(), "!rs1"):
                    pyautogui.typewrite('stick right h 256 && stick right v 256\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick right center\n')
                elif str.startswith(message.lower(), "!rs2"):
                    pyautogui.typewrite('stick right down\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick right center\n')
                elif str.startswith(message.lower(), "!rs3"):
                    pyautogui.typewrite('stick right h 3840 && stick right v 256\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick right center\n')
                elif str.startswith(message.lower(), "!rs4"):
                    pyautogui.typewrite('stick right left\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick right center\n')
                elif str.startswith(message.lower(), "!rs5"):
                    pyautogui.typewrite('r_stick\n')
                    message = ""
                elif str.startswith(message.lower(), "!rs6"):
                    pyautogui.typewrite('stick right right\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick right center\n')
                elif str.startswith(message.lower(), "!rs7"):
                    pyautogui.typewrite('stick right h 256 && stick right v 3840\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick right center\n')
                elif str.startswith(message.lower(), "!rs8"):
                    pyautogui.typewrite('stick right up\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick right center\n')
                elif str.startswith(message.lower(), "!rs9"):
                    pyautogui.typewrite('stick right h 3840 && stick right v 3840\n')
                    message = ""
                    time.sleep(0.5)
                    pyautogui.typewrite('stick right center\n')
                else:
                    pyautogui.typewrite('r_stick\n')
                    message = ""
            else:
                pyautogui.typewrite('r\n')
                message = ""
        elif str.startswith(message.lower(), "!zl"):
            pyautogui.typewrite('zl\n')
            message = ""
        elif str.startswith(message.lower(), "!zr"):
            pyautogui.typewrite('zr\n')
            message = ""
        elif str.startswith(message.lower(), "!plus"):
            pyautogui.typewrite('plus\n')
            message = ""
        elif str.startswith(message.lower(), "!minus"):
            pyautogui.typewrite('minus\n')
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
                    sendMessage(irc, "Available button commands: a, b, x, y, l, r, zl, zr, up, down, left, right, plus, minus.")
                    sendMessage(irc, "Analog stick commands: ls, rs. To move the stick, add a number after it (0-9). The direction corresponds to your numpad! Using !ls5 or !rs5 or !ls or !rs without a number pushes the stick in as another button.")
                    sendMessage(irc, "Please remember to preface all commands with an '!' for them to work! Have a lovely day! :3")
                else:
                    pass

if __name__ == '__main__': #This lets me do two things at once!
    t1 = threading.Thread(target = twitch)
    t1.start()
    t2 = threading.Thread(target = gamecontrol)
    t2.start()
