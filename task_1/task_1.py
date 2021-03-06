import pygame

from get_map_file import get_map_file


def main() -> None:
    longitude, latitude, delta = [input() for _ in range(3)]
    map_file = get_map_file(longitude, latitude, delta)

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
