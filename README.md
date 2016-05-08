# Health Damage Speed

A shooting game created using PySDL2 for Python for Applications Final Project

Michelle Chen and Kevin Carter

#Requirements
* PySDL2
* Turtle
* PyAudio

pysdl2 turned out to be quite difficult to implement. There are not a lot of information guides on the basics of using SDL2 in Python for games available. Most of them are in C and C++ which made it difficult to start with. 

#Usage
Each player’s stats are put into use: the health entered is reflected in each player’s health bar (the green bars on the top), the damage determines how big the missile is and how much it depletes the opponent’s health if collided with, and the speed determines how fast the players move.  

1. Find someone to play with

2. Open up game.py and run it

3. In the popup window, Player1 first allocates 20 points their stats by using the arrow keys. (will check if you have not used all your points or have left a stat at 0) Press “ENTER” when finished

4. Next, Player2 also chooses their stats by using the arrow keys. Press “ENTER” when finished

5. Player1 chooses their character by clicking on any of the top 3 sprites

6. Player2 chooses their character by clicking on any of the bottom 3 sprites. Press “ENTER” when both players have selected their character.

7. Game window will pop up with the selected characters and health, damage, speed stats

8. Player1 on the left uses “W” and “S” keys to move up and down and “SPACE” to shoot a missile

9. Player2 on the right uses “UP” and “DOWN” arrow keys to move up and down and “RETURN” to shoot a missile 

10. Play :)

Notes: each of the 3 missiles a player can shoot has its own 2 second cool down, music played when game over is our original composition made using pyAudio (the file is included), missiles and collisions have sound effects.  

#Credit
Contribution for the project has been equally split despite the number of lines committed. (We worked side-by-side throughout the entire project)
