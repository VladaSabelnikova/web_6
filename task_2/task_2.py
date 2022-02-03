import pygame

from get_map_file import get_map_file
from settings import KEY_PG_UP, KEY_PG_DOWN


def main() -> None:
    longitude, latitude, delta = [input() for _ in range(3)]
    map_file = get_map_file(longitude, latitude, delta)

    pygame.init()
    pygame.display.set_caption('Большая задача')
    screen = pygame.display.set_mode((600, 450))

    running = True
    step = 0.5
    old_delta = delta

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == KEY_PG_UP:
                    delta = str(min(float(delta) / step, 50))

                elif event.key == KEY_PG_DOWN:
                    delta = str(max(float(delta) * step, 0.0001))

        if old_delta != delta:
            old_delta = delta
            map_file = get_map_file(longitude, latitude, delta)

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    map_file.unlink()


if __name__ == '__main__':
    main()
