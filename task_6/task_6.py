import pygame
import pygame_gui

from checks import something_has_changed_for_task_4
from gets import get_lon_lat_from_geocoder_response
from get_map_file import get_map_file
from get_response import get_response_from_geocoder_api
from pygame_gui_elements.create_manager import create_manager
from pygame_gui_elements.text_entry_line import create_text_entry_line
from settings import KEY_PG_UP, KEY_PG_DOWN, KEY_UP, KEY_DOWN, KEY_RIGHT, \
    KEY_LEFT
from pygame_gui_elements.drop_down_menu import create_drop_down_menu


def main() -> None:
    longitude, latitude, delta = [input() for _ in range(3)]
    type_map = 'map'
    pt_type = None
    map_file = get_map_file(longitude, latitude, delta)

    pygame.init()
    pygame.display.set_caption('Большая задача')
    screen = pygame.display.set_mode((600, 450))
    manager = create_manager()
    create_drop_down_menu(manager)
    create_text_entry_line(manager)

    running = True

    step_for_delta = 0.5
    step_for_lon_lat = 0.2

    old_delta = delta
    old_longitude = longitude
    old_latitude = latitude
    old_type_map = type_map

    clock = pygame.time.Clock()

    while running:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    type_map = event.text

                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    toponym_to_find = '+'.join(event.text.split())

                    response = get_response_from_geocoder_api(toponym_to_find)
                    lon, lat = get_lon_lat_from_geocoder_response(response)

                    longitude = lon
                    latitude = lat
                    pt_type = f'{lon},{lat},pmpnl'

            manager.process_events(event)

            if event.type == pygame.KEYDOWN:

                if event.key == KEY_PG_UP:
                    delta = str(min(float(delta) * step_for_delta, 50))

                elif event.key == KEY_PG_DOWN:
                    delta = str(max(float(delta) / step_for_delta, 0.0001))

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

        changes = something_has_changed_for_task_4(
            old_delta,
            delta,
            old_longitude,
            longitude,
            old_latitude,
            latitude,
            old_type_map,
            type_map
        )

        if changes:  # Хотя бы одно изменение было
            old_delta, old_longitude, old_latitude, old_type_map = changes
            map_file = get_map_file(
                longitude,
                latitude,
                delta,
                type_map,
                pt_type
            )

        manager.update(time_delta)
        screen.blit(pygame.image.load(map_file), (0, 0))
        manager.draw_ui(screen)
        pygame.display.update()

    pygame.quit()
    map_file.unlink()


if __name__ == '__main__':
    main()
