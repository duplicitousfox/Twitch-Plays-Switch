# Twitch-Plays-Switch
A script that reads Twitch IRC Chat and parses commands to send to joycontrol and pass button presses to your Switch!

This script should be placed in the same folder as joycontrol and run from there with "sudo python3 twpsw.py".

Be sure to create an account for your bot on Twitch, and get it an Oauth key from Twitch (required!) and put that in the PASS section of the code.
Also be sure to add your channel name, your Twitch name, and run Joycontrol so you can get your Switch's Bluetooth MAC address to place in the
SWITCHBTMAC field.

Once that's all there, run the bot! Due to the limitations of pyatuogui, the terminal for joycontrol needs to be active, and DON'T put your mouse cursor
in the corner of the screen! If joycontrol loses connection with your Switch (and it might!), you can simply reopen joycontrol without restarting the IRC bot.

As of current, there's no command buffer, so if you have high traffic in your Twitch chat, some commands may get dropped! I'll be working on adding that
function in the future.

# Macrobot.py 
This is a variant script that parses chat for commands and sends a series of keystrokes to joycontrol in order to do several button presses off of one
command. It's currently configured for Animal Crossing: New Horizons' photo mode in order to change the character's reaction poses, but these can be
modified for each game.

This otherwise operates exactly as twpsw.py (don't run both at the same time, though).
