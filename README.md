![made-with-python](https://img.shields.io/badge/Made%20with-Python3-brightgreen)

<!-- LOGO -->
<br />
<h1>
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Metropolitano_Lisboa_logo.svg/1200px-Metropolitano_Lisboa_logo.svg.png" alt="Logo" width="140" height="110">
  <br>DinoBot
</h1>
  <p align="center">
    Play the Chrome Dino game using hand gestures or using a bot (WIP).
    <br />
    </p>
</p>
<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#usage">How To Use</a> •
  <a href="#examples">Examples</a> •
  <a href="#best-practice">Best Practice</a> •
</p>  

<p align="center">
  
![screenshot](img/clip.gif)
</p>                                                                                                                             
                                                                                                                                                      
## About The Project
DinoBot is a Python script for playing the Dinosaur Game (also known as the Chrome Dino). It has the option to control the game with your hand through a video capture device, and the option to play it AFK using a bot. I'm aware that the bot has very poor performance, feel free to open an issue about that.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/pearsettings44/DinoBot
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Start the script (using -v or -b flag)
   ```sh
   python3 ./dinobot.py -v
   ```

## Usage
```sh
usage: dinobot.py [-h] [-b] [-v]

optional arguments:
  -h, --help   show this help message and exit
  -b, --bot    play using a bot
  -v, --video  play using video capture
```
To quit the script - press 'q'

## Examples
![alt text](https://github.com/pearsettings44/DinoBot/blob/main/pic1.png?raw=true)
<p align="center">Hand closed (No command).</p>

![alt text](https://github.com/pearsettings44/DinoBot/blob/main/pic2.png?raw=true)
<p align="center">Index finger up (Jump).</p>

![alt text](https://github.com/pearsettings44/DinoBot/blob/main/pic3.png?raw=true)
<p align="center">Bot in action (should have used a gif :P)</p>


## Best Practice
For the most accurate results, here are some recommendation you should follow:
- When using your video capture device of choice, make sure it has a decent amount of fps.
- Make sure you're in a illuminated space, turn on desk lights or open the windows.
- Try to keep your hands facing the camera in a good angle.