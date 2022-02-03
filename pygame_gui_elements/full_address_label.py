import pygame
import pygame_gui


def create_full_address_label(
    manager: pygame_gui.UIManager
) -> pygame_gui.elements.ui_label.UILabel:
    full_address_label = pygame_gui.elements.ui_label.UILabel(
        text='',
        relative_rect=pygame.Rect((470, 39), (120, 49)),
        manager=manager,
    )
    return full_address_label
