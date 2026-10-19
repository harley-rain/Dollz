import pygame

import pygame
from functools import lru_cache
from pathlib import Path

ASSET_PATH = Path("assets")

@lru_cache(maxsize=None)

def load_asset(category, name, color=None):

    if category == "bases":
        path = ASSET_PATH / "Bases" / f"{name}.png"

    elif category == "eyes":
        path = ASSET_PATH / "Eyes" / f"eyes_{name}.png"

    elif category == "hair":
        path = ASSET_PATH / "Hair" / f"{name}_{color}.png"

    elif category == "Bottoms":
        path = ASSET_PATH / "Bottoms" / f"{name}.png"

    else:
        raise ValueError(f"Unknown category: {category}")

    return pygame.image.load(str(path)).convert_alpha()
