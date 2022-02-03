import pygame
import pygame_gui


def create_post_code_menu(
    manager: pygame_gui.UIManager
) -> pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu:
    drop_down_menu = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
        options_list=['выкл. postcode', 'вкл. postcode'],
        starting_option='выкл. postcode',
        relative_rect=pygame.Rect((10, 10), (140, 25)),
        manager=manager
    )
    return drop_down_menu
