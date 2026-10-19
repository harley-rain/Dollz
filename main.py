# Harley Coxon 
import pygame 
# import function from asset file 
from assets import load_asset
# import functions from customization panel 
from customization import draw_customization, handle_customization_event

# initialize library (prepares to run app)
pygame.init() 

# create a window(the surface that can be drawn on) and give it dimensions by calling .display.set_mode() 
window = pygame.display.set_mode((1000, 800))

# Set color scheme variables using RGB values 
PERIWINKLE = (161, 175, 241)
PINK = (255, 179, 217)
PURPLE = (180, 151, 231)

# set the title of app using .set_caption 
pygame.display.set_caption("Dollz!")

# create clock variable to limit the speed of every cycle of of running loop
clock = pygame.time.Clock()

# load_asset() loads then returns selected asset 
selected_base = load_asset("bases", "base_1")
selected_eyes = load_asset("eyes", "green")
selected_hair = load_asset("hair", "short", "black")
selected_bottoms = load_asset("Bottoms", "bottoms_2")

# highlighted button 
selected_category = None

# Create a character panelusing rect() method 
panel = pygame.Rect(50, 50, 900 , 700)
character_panel = pygame.Rect(50, 50, 400 , 700)
inner_character_panel = pygame.Rect(75,75, 350 , 650)

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

    # check for a click 
    if event.type == pygame.MOUSEBUTTONDOWN:
        selected_category = handle_customization_event(event, selected_category)
    
    # set clock frame goal to control loop 
    clock.tick(60) 
    # Use the .fill function to set window color
    window.fill(PINK)
    #
    pygame.draw.rect(window, PERIWINKLE, panel)
    pygame.draw.rect(window, PURPLE, character_panel)
    pygame.draw.rect(window, PERIWINKLE, inner_character_panel)

    #
    window.blit(selected_base, (100,60))
    window.blit(selected_eyes, (100,60))
    window.blit(selected_hair, (100,60))
    window.blit(selected_bottoms, (100,60))


    draw_customization(window, selected_category)

    # Update the full display surface to the screen
    pygame.display.flip()