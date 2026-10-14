# Header******
# 


import pygame 

# initialize library (prepares to run app)
pygame.init() 

# create a window and give it dimensions by calling .display.set_mode() 
window = pygame.display.set_mode((1000, 800))

# Set color scheme variables using RGB values 
PERIWINKLE = (161, 175, 241)
PINK = (255, 179, 217)

# set the title of app using .set_caption 
pygame.display.set_caption("Dollz!")

# create clock variable to limit the speed of every cycle of of running loop
clock = pygame.time.Clock()

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
        clock.tick(60) 


    # Use the .fill function to change window color
    window.fill(PINK)
    # Update the full display surface to the screen
    pygame.display.flip()

