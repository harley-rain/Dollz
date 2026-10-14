# Header******
# 

import pygame 

# initialize library (prepares to run app)
pygame.init() 

# create a window(the surface that can be drawn on) and give it dimensions by calling .display.set_mode() 
window = pygame.display.set_mode((1000, 800))

# Set color scheme variables using RGB values 
PERIWINKLE = (161, 175, 241)
PINK = (255, 179, 217)

# set the title of app using .set_caption 
pygame.display.set_caption("Dollz!")

# create clock variable to limit the speed of every cycle of of running loop
clock = pygame.time.Clock()

# load in and save base assets to variables using .image.load
base_1 = pygame.image.load("assets/Bases/base_1.png").convert_alpha()
base_2 = pygame.image.load("assets/Bases/base_2.png").convert_alpha()
base_3 = pygame.image.load("assets/Bases/base_3.png").convert_alpha()

# load in and save eye assets to variables using .image.load
eyes_brown = pygame.image.load("assets/Eyes/eyes_brown.png").convert_alpha()
eyes_blue = pygame.image.load("assets/Eyes/eyes_blue.png").convert_alpha()
eyes_green = pygame.image.load("assets/Eyes/eyes_green.png").convert_alpha()
eyes_purple = pygame.image.load("assets/Eyes/eyes_purple.png").convert_alpha()
eyes_pink = pygame.image.load("assets/Eyes/eyes_pink.png").convert_alpha()

# default base and eyes
current_base = base_1
current_eyes = eyes_brown

# Create a character panelusing rect() method 
# prob gonna add these tg 
character_panel = pygame.Rect(50, 50, 900 , 700)

# RUNTIME LOOP 

# running boolean variable 
running = True; 

# Main while loop to control application during run time 
# while running == true
while running: 
    # loop through each event 
    for event in pygame.event.get():
        # is event type equal to event type:QUIT
        if event.type == pygame.QUIT:
            # then stop running 
            running = False
        
    # set clock frame goal to control loop 
    clock.tick(60) 
    # Use the .fill function to set window color
    window.fill(PINK)
    #
    pygame.draw.rect(window, PERIWINKLE, character_panel)

    
    #
    window.blit(current_base, (100,100))
    window.blit(current_eyes, (100,100))

    # Update the full display surface to the screen
    pygame.display.flip()
    

    
