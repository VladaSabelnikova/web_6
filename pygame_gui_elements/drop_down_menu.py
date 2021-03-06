import pygame
import pygame_gui


def create_drop_down_menu(
    manager: pygame_gui.UIManager
) -> pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu:
    drop_down_menu = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
        options_list=['map', 'sat', 'sat,skl', 'sat,trf,skl', 'map,trf,skl'],
        starting_option='map',
        relative_rect=pygame.Rect((320, 10), (150, 25)),
        manager=manager
    )
    return drop_down_menu
