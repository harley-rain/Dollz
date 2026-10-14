#### Image


#### Sprite 


#### Event

Pygame keeps track of user interaction while your game is open, these are called events and they are stored as objects
examples:
--- 
-Mouse Movement/Click
-Pressing a key
-Clicking the windows close button
--- 

.get() -method that gives us a list of waiting events and removes them from the queue.
putting this inside a for loop allows to process each event individually, in order. 
```python
pygame.event.get():
```

.type - events are objects with attributes, one of the attributes is type, .type will access this events type. 
no paraentheses bc we are accessing not calling a method 
```python
if event.type == pygame.QUIT: 
```



---


#### Mouse





---
10-13-26 - Created main. Window will run all through a while loop for now. Hardcoded color scheme 
using .display method to set window resolution and title the app
using .event method to read user "events" through the queue to quit the game, this is the only way besides 
force exit to exit app as of now 



