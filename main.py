# Harley Coxon 
# CMPS 4143 - Python/Java 
# Python is awesome assignment 
# Dollz! is a character desktop app that allows the user to customize a doll character 
# Dollz! was created using Python and the Pygame library. 

import random
from pathlib import Path
import pygame 
# import function from asset file 
from assets import load_asset
# import functions from customization panel 
from customization import (
    ASSET_CHOICES,
    REMOVE_ASSET,
    draw_customization,
    handle_customization_event,
)

# initialize library (prepares to run app)
pygame.init() 

# create a window(the surface that can be drawn on) and give it dimensions by calling .display.set_mode() 
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Dollz!")

# Set color scheme variables using RGB values 
PERIWINKLE = (161, 175, 241)
PINK = (255, 179, 217)
PURPLE = (180, 151, 231)
WHITE = (255, 255, 255)

# Keep the logo in the unused lower-right area of the customization panel.
logo = pygame.image.load(Path(__file__).resolve().parent / "logo.png").convert_alpha()
logo = pygame.transform.smoothscale(logo, (180, 180))
logo_card = pygame.Rect(560, 460, 290, 210)
logo_caption_font = pygame.font.SysFont("verdana", 15)
logo_credits = (
    logo_caption_font.render("Created using python and pygame", True, PURPLE),
    logo_caption_font.render("By Harley Coxon", True, PURPLE),
)

# create clock variable to limit the speed of every cycle of of running loop
clock = pygame.time.Clock()

# Keep each selected asset's loader arguments so the matching option can be highlighted.
selected_asset_args = {
    "backgrounds": ("Backgrounds", "backgrounds_1"),
    "eyes": random.choice(ASSET_CHOICES["eyes"])[1],
    "hair": ("hair", "short", "black"),
    "tops": None,
    "bottoms": None,
    "base": random.choice(ASSET_CHOICES["base"])[1],
}
selected_assets = {
    category: load_asset(*asset_args) if asset_args is not None else None
    for category, asset_args in selected_asset_args.items()
}
selected_hair_style = "short"
selected_hair_color = "black"


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (
                selected_category,
                asset_args,
                selected_hair_style,
                selected_hair_color,
            ) = handle_customization_event(
                event, selected_category, selected_hair_style, selected_hair_color
            )
            if asset_args == REMOVE_ASSET:
                selected_asset_args[selected_category] = None
                selected_assets[selected_category] = None
            elif asset_args is not None:
                selected_asset_args[selected_category] = asset_args
                selected_assets[selected_category] = load_asset(*asset_args)
    
    # set clock frame goal to control loop 
    clock.tick(60) 
    # Use the .fill function to set window color
    window.fill(PINK)

    # DRAW Panels
    pygame.draw.rect(window, PERIWINKLE, panel)
    pygame.draw.rect(window, PURPLE, character_panel)
    pygame.draw.rect(window, PERIWINKLE, inner_character_panel)

    
    window.blit(selected_assets["backgrounds"], (0,0))
    window.blit(selected_assets["base"], (100,100))
    window.blit(selected_assets["eyes"], (100,100))
    if selected_assets["bottoms"] is not None:
        window.blit(selected_assets["bottoms"], (100,100))
    if selected_assets["tops"] is not None:
        window.blit(selected_assets["tops"], (100,100))
    window.blit(selected_assets["hair"], (100,100))


    draw_customization(
        window,
        selected_category,
        selected_hair_style,
        selected_hair_color,
        selected_asset_args,
    )
    pygame.draw.rect(window, WHITE, logo_card, border_radius=12)
    pygame.draw.rect(window, PURPLE, logo_card, width=3, border_radius=12)
    window.blit(logo, logo.get_rect(midtop=(logo_card.centerx, logo_card.top - 2)))
    for index, credit in enumerate(logo_credits):
        credit_y = logo_card.top + 160 + index * 22
        window.blit(credit, credit.get_rect(center=(logo_card.centerx, credit_y)))

    # Update the full display surface to the screen
    pygame.display.flip()
