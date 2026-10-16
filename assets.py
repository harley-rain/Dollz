import pygame

def load_assets():
    # BASES
    base_1 = pygame.image.load("assets/Bases/base_1.png").convert_alpha()
    base_2 = pygame.image.load("assets/Bases/base_2.png").convert_alpha()
    base_3 = pygame.image.load("assets/Bases/base_3.png").convert_alpha()

    # EYES
    eyes_brown = pygame.image.load("assets/Eyes/eyes_brown.png").convert_alpha()
    eyes_blue = pygame.image.load("assets/Eyes/eyes_blue.png").convert_alpha()
    eyes_green = pygame.image.load("assets/Eyes/eyes_green.png").convert_alpha()
    eyes_purple = pygame.image.load("assets/Eyes/eyes_purple.png").convert_alpha()
    eyes_pink = pygame.image.load("assets/Eyes/eyes_pink.png").convert_alpha()

    # HAIR - CURLY
    curly_brown = pygame.image.load("assets/Hair/curly_brown.png").convert_alpha()
    curly_red = pygame.image.load("assets/Hair/curly_red.png").convert_alpha()
    curly_blonde = pygame.image.load("assets/Hair/curly_blonde.png").convert_alpha()
    curly_black = pygame.image.load("assets/Hair/curly_black.png").convert_alpha()
    curly_pink = pygame.image.load("assets/Hair/curly_pink.png").convert_alpha()

    # HAIR - CURLY PIGTAILS
    cpig_brown = pygame.image.load("assets/Hair/cpig_brown.png").convert_alpha()
    cpig_red = pygame.image.load("assets/Hair/cpig_red.png").convert_alpha()
    cpig_blonde = pygame.image.load("assets/Hair/cpig_blonde.png").convert_alpha()
    cpig_black = pygame.image.load("assets/Hair/cpig_black.png").convert_alpha()
    cpig_pink = pygame.image.load("assets/Hair/cpig_pink.png").convert_alpha()

    # HAIR - STRAIGHT PIGTAILS
    spig_brown = pygame.image.load("assets/Hair/spig_brown.png").convert_alpha()
    spig_red = pygame.image.load("assets/Hair/spig_red.png").convert_alpha()
    spig_blonde = pygame.image.load("assets/Hair/spig_blonde.png").convert_alpha()
    spig_black = pygame.image.load("assets/Hair/spig_black.png").convert_alpha()
    spig_pink = pygame.image.load("assets/Hair/spig_pink.png").convert_alpha()

    # HAIR - PONYTAIL
    pony_brown = pygame.image.load("assets/Hair/pony_brown.png").convert_alpha()
    pony_red = pygame.image.load("assets/Hair/pony_red.png").convert_alpha()
    pony_blonde = pygame.image.load("assets/Hair/pony_blonde.png").convert_alpha()
    pony_black = pygame.image.load("assets/Hair/pony_black.png").convert_alpha()
    pony_pink = pygame.image.load("assets/Hair/pony_pink.png").convert_alpha()

    # HAIR - STRAIGHT
    straight_brown = pygame.image.load("assets/Hair/straight_brown.png").convert_alpha()
    straight_red = pygame.image.load("assets/Hair/straight_red.png").convert_alpha()
    straight_blonde = pygame.image.load("assets/Hair/straight_blonde.png").convert_alpha()
    straight_black = pygame.image.load("assets/Hair/straight_black.png").convert_alpha()
    straight_pink = pygame.image.load("assets/Hair/straight_pink.png").convert_alpha()

    # HAIR - SHORT
    short_brown = pygame.image.load("assets/Hair/short_brown.png").convert_alpha()
    short_red = pygame.image.load("assets/Hair/short_red.png").convert_alpha()
    short_blonde = pygame.image.load("assets/Hair/short_blonde.png").convert_alpha()
    short_black = pygame.image.load("assets/Hair/short_black.png").convert_alpha()
    short_pink = pygame.image.load("assets/Hair/short_pink.png").convert_alpha()

    # ORGANIZE ASSETS
    bases = {
        "base_1": base_1,
        "base_2": base_2,
        "base_3": base_3
    }

    eyes = {
        "brown": eyes_brown,
        "blue": eyes_blue,
        "green": eyes_green,
        "purple": eyes_purple,
        "pink": eyes_pink
    }

    hair = {
        "curly": {
            "brown": curly_brown,
            "red": curly_red,
            "blonde": curly_blonde,
            "black": curly_black,
            "pink": curly_pink
        },
        "cpig": {
            "brown": cpig_brown,
            "red": cpig_red,
            "blonde": cpig_blonde,
            "black": cpig_black,
            "pink": cpig_pink
        },
        "spig": {
            "brown": spig_brown,
            "red": spig_red,
            "blonde": spig_blonde,
            "black": spig_black,
            "pink": spig_pink
        },
        "pony": {
            "brown": pony_brown,
            "red": pony_red,
            "blonde": pony_blonde,
            "black": pony_black,
            "pink": pony_pink
        },
        "straight": {
            "brown": straight_brown,
            "red": straight_red,
            "blonde": straight_blonde,
            "black": straight_black,
            "pink": straight_pink
        },
        "short": {
            "brown": short_brown,
            "red": short_red,
            "blonde": short_blonde,
            "black": short_black,
            "pink": short_pink
        }
    }

    return bases, eyes, hair
