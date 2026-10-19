import pygame

# Colors
PINK = (255, 179, 217)
PERIWINKLE = (161, 175, 241)
PURPLE = (180, 151, 231)

# Category buttons
eyes_button = pygame.Rect(480, 100, 140, 60)
hair_button = pygame.Rect(630, 100, 140, 60)
tops_button = pygame.Rect(780, 100, 140, 60)

bottoms_button = pygame.Rect(480, 170, 140, 60)
shoes_button = pygame.Rect(630, 170, 140, 60)
accessories_button = pygame.Rect(780, 170, 140, 60)


def draw_customization(window, selected_category):
    # Draw category buttons
    buttons = {
        "eyes": eyes_button,
        "hair": hair_button,
        "tops": tops_button,
        "bottoms": bottoms_button,
        "shoes": shoes_button,
        "accessories": accessories_button
    }

    my_font = pygame.font.SysFont("verdana", 36)

    for category, button in buttons.items():
        if category == selected_category:
            color = PINK
        else:
            color = PURPLE

        pygame.draw.rect(window, color, button, border_radius=8)

        text = my_font.render(category.capitalize(), True, (255, 255, 255))
        window.blit(text, text.get_rect(center=button.center))


def handle_customization_event(event, selected_category):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        buttons = {
            "eyes": eyes_button,
            "hair": hair_button,
            "tops": tops_button,
            "bottoms": bottoms_button,
            "shoes": shoes_button,
            "accessories": accessories_button
        }

        for category, button in buttons.items():
            if button.collidepoint(event.pos):
                return category

    return selected_category
