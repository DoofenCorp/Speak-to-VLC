# Work in progress.
Keep checking for functionality additions. If any issues are discovered then kindly post them in issues.

Current Features:
* Connection with VLC
* Remote commands fully functional
* Tested on Python 3.10 (Should work with Python 3.5+) on Windows 10 Pro 22H2

Upcoming:
* Speech recognition integration for voice control (Probably within this week)
* ~Bug fix for "shutdown" command which works but raises asyncio's runtime error (within couple days)~ Fixed on 23 July 2023.

# SETUP GUIDE:

## 1. Install all requirements:

* Python 3.7+
* `telnetlib3` module
* `SpeechRecognition` module
1. Install Python 3 if not already installed.
1. Then run `req.bat` (Windows) OR `req.sh` (*nix/MacOS) to install all requirements from requirements.txt 
Note: Run the `req.bat` as Administrator on  Windows if you Python installed in `C:\Program Files\`. Similarly, try `sudo` mode for *nix/MacOS

##    2. Configure VLC Media Player to use telnet as an additional main interface:

* Open VLC Media Player
* Click Tools on Menu Bar
* Click on Preferences
* On the bottom left of popup window, under 'show settings' click on All
* In the left menu expand 'Interfaces' and click on Main Interfaces
* IMPORTANT: In main interfaces, checkmark on 'Telnet'
* Expand 'Main Interfaces' on the left pane and click on 'Lua'
* On the right pane configure 'Lua Telnet'
    * Lua Interface: `dummy`
    * Host: `localhost` or `127.0.0.1` for same computer or set remote IP
    * Port: `4212` is default, you can leave it as is or configure any other port if required
    * Password: Set your password
* Click on Save

## 3. Generate configuration file to establish connection

* Go to scripts directory
* Run `setup.py`
* Set host, port and password which were set in VLC media player in previous step
* `config.json` will be generated

## 4. Connect Python to VLC

* Launch VLC media player or play some media in VLC
* Run `connection.py`
* You'll see the `VLC>` prompt to issue commands. 
(List of commands available in `commands.txt`)


# Troubleshooting

Script is under continuous development and prone to problems. Common possible issues and fixes are listed in `troubleshooting.txt`
