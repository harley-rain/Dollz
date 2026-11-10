import pygame

# Colors
PINK = (255, 179, 217)
PERIWINKLE = (161, 175, 241)
PURPLE = (180, 151, 231)
WHITE = (255, 255, 255)

# Category buttons
CATEGORY_BUTTONS = {
    "eyes": pygame.Rect(480, 100, 140, 60),
    "hair": pygame.Rect(630, 100, 140, 60),
    "tops": pygame.Rect(780, 100, 140, 60),
    "bottoms": pygame.Rect(480, 170, 140, 60),
    "backgrounds": pygame.Rect(630, 170, 140, 60),
    "base": pygame.Rect(780, 170, 140, 60),
}

CATEGORY_LABELS = {
    "base": "Skin Color",
}

# Each choice is (button label, arguments to pass to load_asset).
# Choices use only assets that currently exist in the assets folders.
ASSET_CHOICES = {
    "eyes": [
        ("Blue", ("eyes", "blue")),
        ("Brown", ("eyes", "brown")),
        ("Green", ("eyes", "green")),
        ("Pink", ("eyes", "pink")),
        ("Purple", ("eyes", "purple")),
    ],
    "tops": [
        ("1", ("Tops", "tops_1")),
        ("2", ("Tops", "tops_2")),
        ("3", ("Tops", "tops_3")),
        ("4", ("Tops", "tops_4")),
    ],
    "bottoms": [
        (f"Bottoms {number}", ("Bottoms", f"bottoms_{number}"))
        for number in range(1, 5)
    ],
    "backgrounds": [
        ("Pink", ("Backgrounds", "backgrounds_1")),
        ("Purple", ("Backgrounds", "backgrounds_2")),
        ("Green", ("Backgrounds", "backgrounds_3")),
    ],
    "base": [
        (f"Skin {number}", ("bases", f"base_{number}"))
        for number in range(1, 4)
    ],
}

HAIR_STYLES = ("short", "straight", "curly", "pony", "spig", "cpig")
HAIR_COLORS = ("black", "blonde", "brown", "pink", "red")

# Asset choices are laid out in a 4-column grid in the right-side panel.
ASSET_BUTTON_X = 480
ASSET_BUTTON_Y = 270
ASSET_BUTTON_WIDTH = 100
ASSET_BUTTON_HEIGHT = 42
ASSET_BUTTON_GAP_X = 10
ASSET_BUTTON_GAP_Y = 10
ASSET_BUTTON_COLUMNS = 4
HAIR_STYLE_X = 480
HAIR_COLOR_X = 720
HAIR_OPTIONS_Y = 300
HAIR_OPTION_COLUMNS = 2
REMOVE_ASSET = ("__remove__",)


def _remove_button(category):
    """Place the remove button centered below this category's options."""
    option_rects = [button for _label, _args, button in _asset_buttons(category)]
    center_x = sum(button.centerx for button in option_rects) // len(option_rects)
    y = max(button.bottom for button in option_rects) + ASSET_BUTTON_GAP_Y
    return pygame.Rect(center_x - 25, y, 50, 28)


def _asset_buttons(category):
    """Return this category's asset options with their button rectangles."""
    choices = ASSET_CHOICES.get(category, [])
    buttons = []

    for index, (label, asset_args) in enumerate(choices):
        column = index % ASSET_BUTTON_COLUMNS
        row = index // ASSET_BUTTON_COLUMNS
        x = ASSET_BUTTON_X + column * (ASSET_BUTTON_WIDTH + ASSET_BUTTON_GAP_X)
        y = ASSET_BUTTON_Y + row * (ASSET_BUTTON_HEIGHT + ASSET_BUTTON_GAP_Y)
        rect = pygame.Rect(x, y, ASSET_BUTTON_WIDTH, ASSET_BUTTON_HEIGHT)
        buttons.append((label, asset_args, rect))

    return buttons


def _hair_option_buttons():
    """Return separate style and color button groups for the Hair category."""
    buttons = []

    groups = (
        ("style", HAIR_STYLES, HAIR_STYLE_X),
        ("color", HAIR_COLORS, HAIR_COLOR_X),
    )
    for group, options, start_x in groups:
        for index, option in enumerate(options):
            column = index % HAIR_OPTION_COLUMNS
            row = index // HAIR_OPTION_COLUMNS
            x = start_x + column * (ASSET_BUTTON_WIDTH + ASSET_BUTTON_GAP_X)
            y = HAIR_OPTIONS_Y + row * (ASSET_BUTTON_HEIGHT + ASSET_BUTTON_GAP_Y)
            rect = pygame.Rect(x, y, ASSET_BUTTON_WIDTH, ASSET_BUTTON_HEIGHT)
            buttons.append((group, option, option.capitalize(), rect))

    return buttons


def draw_customization(
    window,
    selected_category,
    hair_style="short",
    hair_color="black",
    selected_asset_args=None,
):
    font = pygame.font.SysFont("verdana", 16)
    small_font = pygame.font.SysFont("verdana", 12)

    # Draw category buttons.
    for category, button in CATEGORY_BUTTONS.items():
        color = PINK if category == selected_category else PURPLE
        pygame.draw.rect(window, color, button, border_radius=8)
        label = CATEGORY_LABELS.get(category, category.capitalize())
        text = font.render(label, True, WHITE)
        window.blit(text, text.get_rect(center=button.center))

    if selected_category == "hair":
        # Hair has two independent option groups: style and color.
        for title, x in (("Style", HAIR_STYLE_X), ("Color", HAIR_COLOR_X)):
            heading = font.render(title, True, WHITE)
            window.blit(heading, (x, HAIR_OPTIONS_Y - 34))

        selected_hair_options = {"style": hair_style, "color": hair_color}
        for group, value, label, button in _hair_option_buttons():
            color = PINK if selected_hair_options[group] == value else PURPLE
            pygame.draw.rect(window, color, button, border_radius=6)
            text = small_font.render(label, True, WHITE)
            window.blit(text, text.get_rect(center=button.center))
    else:
        if selected_category in ("tops", "bottoms"):
            remove_button = _remove_button(selected_category)
            pygame.draw.rect(window, PURPLE, remove_button, border_radius=6)
            remove_text = font.render("X", True, WHITE)
            window.blit(remove_text, remove_text.get_rect(center=remove_button.center))

        # Draw asset buttons only for the currently selected category.
        selected_asset_args = (selected_asset_args or {}).get(selected_category)
        for label, asset_args, button in _asset_buttons(selected_category):
            color = PINK if asset_args == selected_asset_args else PURPLE
            pygame.draw.rect(window, color, button, border_radius=6)
            text = small_font.render(label, True, WHITE)
            window.blit(text, text.get_rect(center=button.center))


def handle_customization_event(
    event, selected_category, hair_style="short", hair_color="black"
):
    """Return category, asset args, and the current hair style and color."""
    if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
        return selected_category, None, hair_style, hair_color

    # Selecting a category changes which asset buttons are shown.
    for category, button in CATEGORY_BUTTONS.items():
        if button.collidepoint(event.pos):
            return category, None, hair_style, hair_color

    if selected_category == "hair":
        for group, value, _label, button in _hair_option_buttons():
            if button.collidepoint(event.pos):
                if group == "style":
                    hair_style = value
                else:
                    hair_color = value
                return (
                    selected_category,
                    ("hair", hair_style, hair_color),
                    hair_style,
                    hair_color,
                )
        return selected_category, None, hair_style, hair_color

    if (
        selected_category in ("tops", "bottoms")
        and _remove_button(selected_category).collidepoint(event.pos)
    ):
        return selected_category, REMOVE_ASSET, hair_style, hair_color

    # Selecting an asset returns its load_asset arguments to main.py.
    for _label, asset_args, button in _asset_buttons(selected_category):
        if button.collidepoint(event.pos):
            return selected_category, asset_args, hair_style, hair_color

    return selected_category, None, hair_style, hair_color
