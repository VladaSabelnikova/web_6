import pygame
import pygame_gui


def create_text_entry_line(
    manager: pygame_gui.UIManager
) -> pygame_gui.elements.UITextEntryLine:
    entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((470, 10), (120, 29)),
        manager=manager
    )
    return entry
