import all_actions as aa
AL = aa.AllActions()
if __name__ == '__main__'   :
    running = True
    # песня в главном меню
    aa.pg.mixer.music.load('data/musics/zankyou_8_bit.mp3')
    aa.pg.mixer.music.set_volume(0.4)
    aa.pg.mixer.music.play(-1)
    # главный цикл
    while running:
        is_pressed = False
        for event in aa.pg.event.get():
            if event.type == aa.pg.QUIT:
                running = False
            if event.type == aa.pg.KEYDOWN:
                if event.key == aa.pg.K_ESCAPE:
                    running = False
                if event.key == aa.pg.K_p:
                    # PAUSE
                    paused = True
                    while paused:
                        for semon in aa.pg.event.get():
                            if semon.type == aa.pg.QUIT:
                                aa.pg.quit()
                                exit()
                            if semon.type == aa.pg.KEYDOWN:
                                if semon.key == aa.pg.K_ESCAPE:
                                    paused = False
                                if semon.key == aa.pg.K_p:
                                    paused = False
            if event.type == aa.pg.MOUSEBUTTONUP:
                if event.button == 1:
                    # нажали ли на какую либо игровую кнопку (начать, выйти...)
                    is_pressed = True
        # меню ли сейчас?
        if AL.menu:
            AL.show_main_menu(aa.screen)
        # идет ли игра?
        if AL.game:
            AL.g_begin()
        if AL.die_menu:
            AL.died(aa.screen, 0, is_pressed, None)
        aa.pressed = is_pressed  # передаем то, что какая-то кнопка была нажата
        aa.clock.tick(aa.fps)
        aa.pg.display.update()
    aa.pg.quit()