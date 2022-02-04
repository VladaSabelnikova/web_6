import pygame
import pygame_gui

from checks import something_has_changed_for_task_7
from create_address_for_label import create_address_for_label
from get_map_file import get_map_file
from get_response import get_response_from_static_api, \
    get_response_from_search_api_geo
from gets import get_full_address_from_search_response_geo
from lon_lat_from_mouse_click import get_lon_lat_from_mouse_click
from pygame_gui_elements.create_manager import create_manager
from pygame_gui_elements.drop_down_menu import create_drop_down_menu
from pygame_gui_elements.full_address_label import create_full_address_label
from pygame_gui_elements.post_code import create_post_code_menu
from pygame_gui_elements.resetting_search_result import \
    create_resetting_search_result_button
from pygame_gui_elements.text_entry_line import create_text_entry_line
from settings import KEY_PG_UP, KEY_PG_DOWN, KEY_UP, KEY_DOWN, KEY_RIGHT, \
    KEY_LEFT, MOUSE_KEY_LEFT, MOUSE_KEY_RIGHT


def main() -> None:
    longitude, latitude, delta = [input() for _ in range(3)]
    type_map = 'map'
    pt_type = None
    map_file = get_map_file(longitude, latitude, delta)

    pygame.init()
    pygame.display.set_caption('Большая задача')
    screen = pygame.display.set_mode((600, 450))

    manager = create_manager()
    input_label = create_text_entry_line(manager)
    type_map_menu = create_drop_down_menu(manager)
    post_code_menu = create_post_code_menu(manager)
    address_label = create_full_address_label(manager)
    del_search_result_button = create_resetting_search_result_button(manager)

    running = True

    step_for_delta = 0.5
    step_for_lon_lat = 0.2

    old_delta = delta
    old_longitude = longitude
    old_latitude = latitude
    old_type_map = type_map
    old_pt_type = pt_type

    clock = pygame.time.Clock()

    while running:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT:  # GUI

                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    # Если нажали на кнопку "Сброс результата":
                    # 1. убираем метку
                    # 2. зачищаем address_label
                    if event.ui_element == del_search_result_button:
                        pt_type = None
                        address_label.set_text('')

                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    # Если выбираем тип карты:
                    # Назначаем выбранный тип в type_map
                    if event.ui_element == type_map_menu:
                        type_map = event.text

                    elif event.ui_element == post_code_menu:
                        # Если нажали переключатель почтового индекса
                        if input_label.text:  # если при этом адрес есть

                            # Разбираем адрес
                            toponym_to_find = '+'.join(input_label.text.split())

                            # Создаём текст для вставки в address_label
                            longitude, latitude, pt_type, address = \
                                create_address_for_label(
                                    toponym_to_find,
                                    post_code_menu
                                )

                            address_label.set_text(address)

                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    # Если ввели адрес через форму:
                    #   1. Разбираем адрес
                    #   2. Создаём текст для вставки в address_label

                    # Разбираем адрес
                    toponym_to_find = '+'.join(event.text.split())

                    # Создаём текст для вставки в address_label
                    longitude, latitude, pt_type, address = \
                        create_address_for_label(
                            toponym_to_find,
                            post_code_menu
                        )

                    address_label.set_text(address)
            manager.process_events(event)

            if event.type == pygame.KEYDOWN:  # Ввод с клавиатуры

                # В зависимости от того, что нажали — меняем масштаб

                if event.key == KEY_PG_UP:
                    delta = str(min(float(delta) / step_for_delta, 55))

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

            if event.type == pygame.MOUSEBUTTONDOWN:  # Нажали на мышку

                if event.button == MOUSE_KEY_LEFT:

                    # Если нажали на левую:
                    #   1. Вычисляем координату
                    #   2. Вычисляем адрес местности
                    #   3. Записываем адрес в address_label

                    # Вычисляем координату
                    longitude, latitude = get_lon_lat_from_mouse_click(
                        event.pos,
                        float(longitude),
                        float(latitude),
                        float(delta)
                    )

                    # Объект, из которого найдём адрес
                    response_search_api = get_response_from_search_api_geo(
                        longitude,
                        latitude
                    )

                    # Вычисляем адрес местности
                    toponym_to_find = get_full_address_from_search_response_geo(
                        response_search_api
                    )

                    # Записываем адрес в address_label
                    longitude, latitude, pt_type, address = \
                        create_address_for_label(
                            toponym_to_find,
                            post_code_menu
                        )
                    address_label.set_text(address)
                    # pass

                elif event.button == MOUSE_KEY_RIGHT:
                    # вычислить координату get_lon_lat_from_mouse_click

                    # выяснить на каком расстоянии находятся координаты друг
                    # относительно друга lonlat_distance

                    # если меньше 50 метров то:
                    #   address = get_full_address_from_search_response_biz
                    #   address_label.set_text(address)
                    pass

        changes = something_has_changed_for_task_7(
            old_delta,
            delta,
            old_longitude,
            longitude,
            old_latitude,
            latitude,
            old_type_map,
            type_map,
            old_pt_type,
            pt_type
        )

        if changes:  # Хотя бы одно изменение было
            old_delta, old_longitude, old_latitude, \
            old_type_map, old_pt_type = changes

            map_file = get_map_file(
                longitude,
                latitude,
                delta,
                type_map,
                pt_type
            )

        screen.blit(pygame.image.load(map_file), (0, 0))
        manager.draw_ui(screen)
        pygame.display.update()
        manager.update(time_delta)

    pygame.quit()
    map_file.unlink()


if __name__ == '__main__':
    main()
