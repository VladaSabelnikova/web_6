import pygame

from get_response import get_response_from_static_api
from show_img import show_img


def main() -> None:
    longitude, latitude, delta = [input() for _ in range(3)]
    response_static = get_response_from_static_api(longitude, latitude, delta)

    map_file = show_img(response_static)

    pygame.init()
    pygame.display.set_caption('Большая задача')
    screen = pygame.display.set_mode((600, 450))
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    map_file.unlink()


if __name__ == '__main__':
    main()
