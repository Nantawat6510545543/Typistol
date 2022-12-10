# Typistol
**Typistol** is a typist game where players take on the role of a shooter. By shooting each time, players need to type the correct word to shoot enemies. If the player misspelled or typed too late, the player will take damage. If the player exhausts the character's HP, it is considered game over. And every time the player defeats an enemy, the game gets more and more difficult.

This game is actually an academic project which is a part of the 01219114/01219115 Programming 1 course at Kasetsart University. The game is made possible using Python 3 and the builtin module, [turtle](https://docs.python.org/3/library/turtle.html).

## Features
- Player stats, equipment and items stats are displayed whenever they change.
- Player can type input in real time.
- Enemy attack time displayed in real time.

## Required Software
- Python >= 3.7 w/ Tk/Tcl installed

## Launch Instructions
Make sure you have all the required software installed.
```bash
~/ > git clone https://github.com/Nantawat6510545543/Typistol.git
~/ > cd Typistol
 > python main.py
```

## Gameplay
Get input through console to select the options.

**Tutorial** : Explains how to play across the screen in text. Click on the screen to go to the next tip.

**Main game** :The game, every action of the player must go through the console only. The player has to type the correct word while looking at the game screen. The game ends when the player gets their health down to 0.

**Leaderboard** : Show the leaderboard.

**Find a player** : Find a player by name

## Program Design

`Stage` : This class is an operator and a means of communication between the file and the game itself, as well as the player and the enemy. It also has the function of recording scores.

`Player` : This class is used to define the properties that the player has, most of the data in this class will persist.

`Enemy` : This class is used to define the properties that the enemy has.


## Code Structure
[main.py](main.py) : The main file for executing the start of the program.

[Game.py](Game.py) : The file for displaying the GUI of the program and game operation 

[Stage.py](Stage.py) : The files for controlling the stage and creating `Enemy`.

[Player.py](Player.py) : The file for entity `Player`.

[Enemy.py](Enemy.py) : The file for entity `Enemy`.

[word.txt](word.txt) : The file for storing 1000 words.

[record.json](record.json) : The file for storing the user's score.

[cowboy.gif](cowboy.gif) : The [image](https://dribbble.com/shots/4125593-Free-Assets-Wild-West-Pixel-Characters) to represent the player.

[enemy.gif](enemy.gif) : The [image](https://dribbble.com/shots/4125593-Free-Assets-Wild-West-Pixel-Characters) to represent the enemy.

[background.png](background.png) : The [image](https://www.pinterest.com/pin/357262182913353721/) to represent the background.

