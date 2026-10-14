import pygame 

# initialize library (starts up the features)
pygame.init() 

# create a window and give it dimensions by calling .display.set_mode() 
window = pygame.display.set_mode((800, 600))


# COLOR!!!!!
PERIWINKLE = (161, 175, 241)
PINK = (255, 179, 217)


# use the .fill function to change window color
window.fill(PINK)

# set the title of your app using .set_caption 
pygame.display.set_caption("Dollz")
