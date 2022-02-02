from typing import Tuple

import pygame
import pygame_gui


def create_drop_down_menu(

) -> Tuple[pygame_gui.UIManager,
           pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu]:

    manager = pygame_gui.UIManager((700, 450))
    drop_down_menu = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
        options_list=['map', 'sat', 'sat,skl', 'sat,trf,skl', 'map,trf,skl'],
        starting_option='map',
        relative_rect=pygame.Rect((470, 10), (120, 25)),
        manager=manager
    )
    return manager, drop_down_menu