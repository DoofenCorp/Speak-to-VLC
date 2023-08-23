# Constantly under development
Keep checking for functionality additions. If any issues are discovered then kindly post them in issues.

Current Features:
* Connection with VLC
* Remote commands fully functional
* Speech Recognition implemented in Alpha mode. Lot of improvements and testing needed which would be done in coming days. (13 August 2023). This is a very young alpha release so kindly be patient with it as it may or may not work as expected adhering to the environment (An example is that you may have to speak few times).

* Note: With this Alpha implementation I have removed (not really, just commented it) the previous manual telnet client functionality, this now works entirely on voice commands. If needed you can uncomment line 76 in `connection.py` and remove/comment line 77.

* Tested on Python 3.10 (Should work with Python 3.8+) on Windows 10 Pro 22H2

Upcoming:
* Improved speech recognition after rigorous testing and possible implementation of offline recognition
* Task scheduling capability integrated into the setup to automatically launch the script with VLC. (Focused for Windows machines)
* ~Speech recognition integration for voice control (Probably within this week)~ Implemented in v1.0.0-alpha on 13 August 2023.
* ~Bug fix for "shutdown" command which works but raises asyncio's runtime error (within couple days)~ Fixed on 23 July 2023.

# SETUP GUIDE:

Download the latest release from [Releases](https://github.com/DoofenCorp/Speak-to-VLC/releases)

Current latest release: v1.0.1-alpha

## 1. Install all requirements:

1. Install Python >=3.8 if not already installed.
1. Then run `req.bat` (Windows) OR `req.sh` (*nix/MacOS) to install all requirements from requirements.txt 
* Note: Run the `req.bat` as Administrator on  Windows if you have Python installed in `C:\Program Files\`. Similarly, try `sudo` mode for *nix/MacOS
* Internet connectivity for speech recognition
* Python 3.8+
* `cryptography` library
* `telnetlib3` module
* `SpeechRecognition` module
* `pyaudio` module
    * **Windows:** It'll install automatically with step 2.
    * **Debian/Ubuntu:**
        1. `sudo apt-get install -y portaudio19-dev`
        1. `sudo apt-get install python-pyaudio python3-pyaudio` 
    * **Redhat:**
        1. `sudo dnf install portaudio-devel redhat-rpm-config`
        1. `sudo pip3 install pyaudio`
            * If you encounter any error then try: `sudo dnf install python-pyaudio`
    * **MacOS:** 
        1. `brew install portaudio`
        2. `pip3 install pyaudio`

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

### Voice commands:

`play` - To play media

`pause` - To pause playback

`stop` - To stop playback

`fullscreen` - Enter/Exit fullscreen

`shutdown` - Exit VLC

`increase volume` - Increase volume by 10%

`decrease volume` - Decrease volume by 10%

`stop listening` - Turns off voice command

`faster` - Faster playback by 0.5x

`slower` - Slower playback by 0.5x

`normal` - Normal playback

Other simple commands listed in commands.txt also work. Complex to speak commands like `atrack` (for changing audio track) will be broken down into simple commands to implement their functionality in upcoming releases.

# Troubleshooting

Application is under continuous development and prone to problems. Common possible issues and fixes are listed in `troubleshooting.txt`
