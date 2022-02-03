import pygame
import pygame_gui


def create_resetting_search_result_button(
    manager: pygame_gui.UIManager
) -> pygame_gui.elements.UIButton:
    button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 10), (170, 29)),
        text='Сброс результата',
        manager=manager
    )
    return button
