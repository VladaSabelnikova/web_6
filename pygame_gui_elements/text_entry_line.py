import pygame
import pygame_gui


def create_text_entry_line(manager):
    entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((320, 10), (150, 25)),
        manager=manager
    )
    return entry
