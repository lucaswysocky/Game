# Game

### Project description

A simple arcade game developed using pygame.


### Objective

Practice programming in Python (especially code refactoring skills) and build something fun while at it!


### Requires

* python 3.7 <=
* pygame 1.9.5 <=

### More info

Player has to shoot as many aliens as possible and try to beat the highest recorded score. The game starts with a play button. Player controls the spaceship using the left and right arrow keys and shoots laser bullets using the space button.
There can be up to 5 laser bullets flying in the field, which further increases difficulty.  
Run *Project_1.py* to start the game.

![](gif_1.gif)  

After shooting all the aliens, user advances to the next level. This increases spaceship's agility!

![](gif_2.gif) 
 

However, with each new level, the aliens approach faster and faster!

![](gif_3.gif) 


If aliens hit the bottom of the screen or the spaceship, the player looses a life. There are 3 lives per game.

![](gif_4.gif)


The file *settings.py* controls all the game's parameters, including how more difficult each level is, how agile the spaceship becomes etc.
The game keeps the record of the highest score achieved by anyone who plays it.

### Future improvements

* aliens shooting their own laser bullets
* obstacles the aliens can hide behind
* more nuanced movements the aliens can make
* personal user accounts
