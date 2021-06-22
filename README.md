# Mario AI

This is a practice of genetics algorithm in AI to Super Mario game.
We get a level map and try to find the best solution for it.

![GamePreview][images/preview.gif]

## Map
Maps must be like this:
````
__G___L_
````
Items are defined in follwing:
 - G: Goomba
 - L: Lakitu
 - _: Empty Ground
 - M: Mushroom

## Solution
The given solutions are like this:
````
12011020001   __G__G_L___   13.5   True
````
items are describes in following:

First string is the action to be taken.

 - 0: Step forward
 - 1: Jump and go forward
 - 2: Sit and go forward

Second part is the map. Third is the total score and forth parts says wether this solution leads us to success or no.

# Requirements
To run this game you need to just type this command in terminal.
````
$ pip install -r requirements.txt
````

# Run the Game
To run the game just run main.py file with python interpreter:
````
$ python3 main.py
````
