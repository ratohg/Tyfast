import pygame

def update(SCREEN_X, SCREEN_Y):
    input_box = pygame.image.load("assets/buttons/button-game/input-box.png")
    input_box_rect = input_box.get_rect(center=(SCREEN_X/2, SCREEN_Y/2))
    info_box_word = pygame.image.load("assets/windows/windows-game/info-word.png")
    info_box_word_rect = info_box_word.get_rect(center=(SCREEN_X/2 , SCREEN_Y/2- 100))
    button_retry = pygame.image.load("assets/buttons/button-game/button-retry.png")
    rect_button = button_retry.get_rect(center=(SCREEN_X/2, SCREEN_Y/2 + 90))
    window_lose = pygame.image.load("assets/windows/windows-game/lose-window.png")
    window_lose_rect = window_lose.get_rect(center=(SCREEN_X / 2 , SCREEN_Y / 2))
    bg_start = pygame.image.load("assets/backgrounds/background-menu/background.png")
    bg_start = pygame.transform.scale(bg_start, (SCREEN_X, SCREEN_Y))
    bg_start1 = pygame.image.load("assets/backgrounds/background-menu/background.png")
    bg_start1 = pygame.transform.scale(bg_start1, (SCREEN_X, SCREEN_Y))
    bg1 = pygame.image.load("assets/backgrounds/background-game/bg.png")
    bg1 = pygame.transform.scale(bg1, (SCREEN_X, SCREEN_Y))
    bg2 = pygame.image.load("assets/backgrounds/background-game/bg.png")
    bg2 = pygame.transform.scale(bg2, (SCREEN_X, SCREEN_Y))
    start_menu = pygame.image.load("assets/buttons/buttons-menu/button-start.png")
    rect_start_menu = start_menu.get_rect(center=(SCREEN_X/2 - int(start_menu.get_rect()[2]) + 100, SCREEN_Y/2 - 30))
    options_menu = pygame.image.load("assets/buttons/buttons-menu/button-options.png")
    rect_options_menu = options_menu.get_rect(center=(SCREEN_X/2 - int(start_menu.get_rect()[2]) + 100, SCREEN_Y/2 + 20))
    about_menu = pygame.image.load("assets/buttons/buttons-menu/button-about.png")
    rect_about_menu = about_menu.get_rect(center=(SCREEN_X/2 - int(start_menu.get_rect()[2]) + 100, SCREEN_Y/2 + 70))
    option_window = pygame.image.load("assets/windows/windows-menu/options-window.png")
    option_window_rect = option_window.get_rect(center=(SCREEN_X/2, SCREEN_Y/2))
    exit_option_window = pygame.image.load("assets/buttons/button-windows-options/exit-window-option.png")
    exit_option_window_rect = exit_option_window.get_rect(center=(option_window_rect.x + 100, option_window_rect.y + 60))
    option_button_box = pygame.image.load("assets/buttons/button-windows-options/box-transparent.png")
    option_button_box_easy = pygame.transform.scale(option_button_box, (40, 40))
    option_button_box_medium = pygame.transform.scale(option_button_box, (40, 40))
    option_button_box_hard = pygame.transform.scale(option_button_box, (40, 40))
    option_button_res_800 = pygame.transform.scale(option_button_box, (40, 40))
    option_button_res_1280 = pygame.transform.scale(option_button_box, (40, 40))
    option_button_res_1920 = pygame.transform.scale(option_button_box, (40, 40))
    option_button_res_800_rect = option_button_res_800.get_rect(center=(window_lose_rect.x + 228, window_lose_rect.y + 167))
    option_button_res_1280_rect = option_button_res_1280.get_rect(center=(window_lose_rect.x + 352, window_lose_rect.y + 167))
    option_button_res_1920_rect = option_button_res_1920.get_rect(center=(window_lose_rect.x + 480, window_lose_rect.y + 167))
    option_button_box_easy_rect = option_button_box_easy.get_rect(center=(window_lose_rect.x + 254, window_lose_rect.y + 97))
    option_button_box_medium_rect = option_button_box_medium.get_rect(center=(window_lose_rect.x + 380, window_lose_rect.y + 97))
    option_button_box_hard_rect = option_button_box_hard.get_rect(center=(window_lose_rect.x + 480, window_lose_rect.y + 97))
    bg_loading = pygame.image.load("assets/backgrounds/background-loading/bg-loading.png")
    bg_loading = pygame.transform.scale(bg_loading, (SCREEN_X, SCREEN_Y))
    bg_loading1 = pygame.image.load("assets/backgrounds/background-loading/bg-loading.png")
    bg_loading1 = pygame.transform.scale(bg_loading, (SCREEN_X, SCREEN_Y))
    button_exit = pygame.image.load("assets/buttons/button-game/button-exit.png")
    button_exit_rect = button_exit.get_rect(center=(80, 35))
    option_box_fullscreen = pygame.image.load("assets/buttons/button-windows-options/box-transparent.png")
    option_box_fullscreen = pygame.transform.scale(option_box_fullscreen, (40, 40))
    option_box_fullscreen_rect = option_box_fullscreen.get_rect(center=(window_lose_rect.x + 248, window_lose_rect.y + 218))
    about_window = pygame.image.load("assets/windows/windows-menu/about-window.png")
    about_window_rect = about_window.get_rect(center=(SCREEN_X/2, SCREEN_Y/2))
    option_box_bar_volume = pygame.image.load("assets/buttons/button-windows-options/bar-volume.png")
    option_box_bar_volume_scale = pygame.transform.scale(option_box_bar_volume, (350, 50))
    option_box_bar_volume_rect = option_box_bar_volume_scale.get_rect(center=(SCREEN_X/2 + 73, SCREEN_Y/2+ 140))
    button_bar_volume = pygame.image.load("assets//buttons/button-windows-options/button-volume.png")
    button_bar_volume_rect = button_bar_volume.get_rect(center=(option_box_bar_volume_rect.x, option_box_bar_volume_rect.y + 2))
    list_widgets = (input_box, input_box_rect, info_box_word, info_box_word_rect, button_retry, rect_button, window_lose, window_lose_rect, bg_start, bg_start1, bg1, bg2, start_menu, rect_start_menu, options_menu, rect_options_menu, about_menu, rect_about_menu, option_window, option_window_rect, exit_option_window, exit_option_window_rect, option_button_box, option_button_box_easy, option_button_box_medium, option_button_box_hard, option_button_res_800, option_button_res_1280, option_button_res_1920, option_button_res_800_rect, option_button_res_1280_rect, option_button_res_1920_rect, option_button_box_easy_rect, option_button_box_medium_rect, option_button_box_hard_rect, bg_loading, bg_loading1, button_exit, button_exit_rect, option_box_fullscreen, option_box_fullscreen_rect, about_window, about_window_rect, option_box_bar_volume, option_box_bar_volume_rect, button_bar_volume, button_bar_volume_rect)
    return (list_widgets)