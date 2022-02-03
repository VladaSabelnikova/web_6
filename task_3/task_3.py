import pygame

from checks import something_has_changed
from get_map_file import get_map_file
from settings import KEY_PG_UP, KEY_PG_DOWN, KEY_UP, KEY_DOWN, KEY_RIGHT, \
    KEY_LEFT


def main() -> None:
    longitude, latitude, delta = [input() for _ in range(3)]
    map_file = get_map_file(longitude, latitude, delta)

    pygame.init()
    pygame.display.set_caption('Большая задача')
    screen = pygame.display.set_mode((600, 450))

    running = True
    step_for_delta = 0.5
    step_for_lon_lat = 0.2
    old_delta = delta
    old_longitude = longitude
    old_latitude = latitude

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == KEY_PG_UP:
                    delta = str(min(float(delta) / step_for_delta, 50))

                elif event.key == KEY_PG_DOWN:
                    delta = str(max(float(delta) * step_for_delta, 0.0001))

                elif event.key == KEY_UP:
                    latitude = str(min(float(latitude) + step_for_lon_lat, 90))

                elif event.key == KEY_DOWN:
                    latitude = str(
                        max(float(latitude) - step_for_lon_lat, -90))

                elif event.key == KEY_RIGHT:
                    longitude = str(
                        min(float(longitude) + step_for_lon_lat, 180))

                elif event.key == KEY_LEFT:
                    longitude = str(
                        max(float(longitude) - step_for_lon_lat, 0))

        changes = something_has_changed(
            old_delta,
            delta,
            old_longitude,
            longitude,
            old_latitude,
            latitude
        )

        if changes:  # Хотя бы одно изменение было
            old_delta, old_longitude, old_latitude = changes
            map_file = get_map_file(longitude, latitude, delta)

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    map_file.unlink()


if __name__ == '__main__':
    main()
