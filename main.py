import pygame as pg
from Button_ import *
from Level import *


menu = True
game = False
pg.init()
SIZE = get_size()
screen = pg.display.set_mode((SIZE.current_w, SIZE.current_h))
pg.display.set_caption('1000 - 7')
BUTTON = Button(SIZE.current_w * 0.15, SIZE.current_h * 0.065)
miniBUTTON = Button(SIZE.current_w * 0.0725, SIZE.current_h * 0.037)
clock = pg.time.Clock()
fps = 75
running = True
gameAbout = False
gameControls = False
music_play = True
small = SIZE.current_h * 0.15, SIZE.current_h * 0.04
timer = 0


def show_main_menu(screen):
    global gameControls
    global gameAbout
    global music_play
    image = pg.image.load('data/main_menu.png').convert()
    image = pg.transform.scale(image, (SIZE.current_w, SIZE.current_h))
    screen.blit(image, image.get_rect())
    BUTTON.draw(SIZE.current_w / 5, SIZE.current_h / 2, "START", game_start, screen, pressed)
    btn_about = BUTTON.draw((SIZE.current_w * 2) / 5, SIZE.current_h / 2, "ABOUT", nothing, screen, pressed)
    btn_controls = BUTTON.draw((SIZE.current_w * 3) / 5, SIZE.current_h / 2, "CONTROLS", nothing, screen, pressed)
    BUTTON.draw((SIZE.current_w * 4) / 5, SIZE.current_h / 2, "EXIT", game_exit, screen, pressed)
    if music_play:
        Button(small[0], small[1]).draw(SIZE.current_w - 100, 50, 'MUSIC ON', music_off, screen, pressed)
    else:
        Button(small[0], small[1]).draw(SIZE.current_w - 100, 50, 'MUSIC OFF', music_off, screen, pressed)
    if btn_controls:
        gameControls = True
    if gameControls:
        game_controls(screen)
    if btn_about:
        gameAbout = True
    if gameAbout:
        game_about(screen)

def nothing(s):
    pass


def music_off(s):
    global music_play
    if music_play:
        pg.mixer.music.pause()
        music_play = False
    else:
        pg.mixer.music.unpause()
        music_play = True


def game_about(screen):
    info = pg.Surface(size=(SIZE.current_h // 2, SIZE.current_h // 2))
    rect = info.get_rect()
    rect.center = SIZE.current_w // 2, SIZE.current_h // 2
    info.fill((30, 0, 60))
    pg.draw.rect(info, pg.Color('orange'), info.get_rect(), 5)
    screen.blit(info, rect)
    s = int(SIZE.current_w * 0.01)
    fs = [pg.font.SysFont('franklingothicmedium', s).render(
        'Когда Зеницу был моложе, он был влюблён в девушку,', True, pg.Color('orange')),
         pg.font.SysFont('franklingothicmedium', s).render(
        'которая обманом заставила его собирать деньги,', True, pg.Color('orange')),
         pg.font.SysFont('franklingothicmedium', s).render(
        'чтобы сбежать со своим возлюбленным. Из-за того, что', True, pg.Color('orange')),
         pg.font.SysFont('franklingothicmedium', s - 2).render(
        'девушка была по уши в долгах, у Зеницу появились проблемы,', True, pg.Color('orange')),
         pg.font.SysFont('franklingothicmedium', s).render(
        'но его спас бывший столп грома Джигоро Куваджима.', True, pg.Color('orange')),
         pg.font.SysFont('franklingothicmedium', s).render(
        'Чтобы вернуть ему долг, Зеницу пришлось пройти', True, pg.Color('orange')),
         pg.font.SysFont('franklingothicmedium', s).render(
        'через адские тренировки и стать истребителем демонов.', True, pg.Color('orange'))]

    x = SIZE.current_w // 2.7
    val = 0.3
    y = SIZE.current_h
    for f in fs:
        ff = f.get_rect(x=x, y=y * val)
        screen.blit(f, ff)
        val += 0.05
    f8 = pg.font.SysFont('franklingothicmedium', s + 20, bold=True).render(
        'Победи всех врагов!', True, (140, 0, 0))
    ff8 = f8.get_rect(center=(SIZE.current_w // 2, SIZE.current_h // 1.5))
    screen.blit(f8, ff8)
    small = round(SIZE.current_h * 0.025)
    Button(small, small).draw(rect.x + rect.width, rect.y, 'x', close_about, screen, pressed)


def close_about(screen):
    global gameAbout
    gameAbout = False

def game_exit(a):
    pg.quit()
    exit()


def game_controls(screen):
    wasd = pg.Surface(size=(SIZE.current_h // 2, SIZE.current_h // 2))
    rect = wasd.get_rect()
    rect.center = SIZE.current_w // 2, SIZE.current_h // 2
    wasd.fill((30, 0, 60))
    pg.draw.rect(wasd, (pg.Color('orange')), wasd.get_rect(), 5)
    screen.blit(wasd, rect)
    s = int(SIZE.current_w * 0.031)
    fs = [
        pg.font.SysFont('arial', s).render('"→" - go to right', True, pg.Color('orange')),
        pg.font.SysFont('arial', s).render('"←" - go to left', True, pg.Color('orange')),
        pg.font.SysFont('arial', s).render('"↑" - jump', True, pg.Color('orange')),
        pg.font.SysFont('arial', s).render('"↓" - slash', True, pg.Color('orange'))
    ]
    for f in fs:
        x = SIZE.current_w // 2.6
    val = 0.3
    y = SIZE.current_h
    for f in fs:
        ff = f.get_rect(x=x, y=y * val)
        screen.blit(f, ff)
        val += 0.1
    small = SIZE.current_h * 0.025, SIZE.current_h * 0.025
    Button(small[0], small[1]).draw(rect.x + rect.width, rect.y, 'x', close_controls, screen, pressed)


def close_controls(screen):
    global gameControls
    gameControls = False


def die_action(screen, BUTTON):
    global press
    press = False
    screen.fill((0, 0, 0))
    sound = pg.mixer.Sound('data/NOOO.mp3')
    sound.set_volume(0.5)
    sound.play()
    for i in range(300):
        died(screen, BUTTON, 1, i)
        pg.time.delay(1)
        pg.display.flip()
    pg.time.delay(1000)
    run = True
    while run:
        press = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    press = True
        died(screen, BUTTON, 2)
        pg.display.flip()
        if died(screen, BUTTON, 2):
            run = False


def died(screen, BUTTON, type, size=None):
    if type == 1:
        screen.fill((0, 0, 0))
        font = pg.font.SysFont('centaur', size // 2, italic=True)
        text = font.render(
            "YOU DIED...", True, (100, 0, 0))
        place = text.get_rect(
            center=(SIZE.current_w // 2, SIZE.current_h // 2))
        screen.blit(text, place)
    else:
        image = pg.image.load('data/died_menu.jpg').convert()
        image = pg.transform.scale(image, (SIZE.current_w, SIZE.current_h))
        screen.blit(image, image.get_rect())
        btn_menu = BUTTON.draw(SIZE.current_w / 2, SIZE.current_h / 2.5, 'MAIN MENU', vacant, screen, press)
        btn_exit = BUTTON.draw(SIZE.current_w / 2, SIZE.current_h / 2, "EXIT", game_exit, screen, press)
        btn_restart = BUTTON.draw(SIZE.current_w / 2, SIZE.current_h / 3.3, "RESTART", game_restart, screen, press)
        if btn_menu or btn_restart:
            return True

def game_restart(screen):
    game_start(screen)


def vacant(screen):
    global menu, game
    menu = True
    game = False


def game_start(screen):
    global game, menu, background, gplatforms, gorizontal_platforms, player, enemies, GROUND, died_mas
    game, menu, background, gplatforms, gorizontal_platforms, player, enemies, GROUND, died_mas = start(screen)


def g_begin():
    if pg.key.get_pressed()[pg.K_DOWN] and player.cooldown == 0:
        shift = int(SIZE.current_w * 0.078125)
        if player.last_direction > 0:
            x_last = player.rect.left
        elif player.last_direction < 0:
            x_last = player.rect.left
        player.rect.x += shift * player.last_direction
        for i in gorizontal_platforms:
            if i.rect.colliderect(player.rect):
                if player.last_direction < 0 and player.rect.left <= i.rect.right:
                    player.rect.left = i.rect.right
                    shift = x_last - player.rect.left
                elif player.last_direction > 0 and player.rect.right >= i.rect.left:
                    player.rect.right = i.rect.left
                    shift = player.rect.left - x_last
        player.slash(enemies, shift, died_mas)
        background.after_slash(player, shift, enemies, gplatforms, died_mas)
        player.kd = True
    if player.kd:
        player.cooldown += 1
        if player.cooldown == 1:
            if player.last_direction < 0:
                player.image = pg.transform.flip(player.agr_image[0], True, False)
            else:
                player.image = pg.transform.flip(player.agr_image[0], False, False)
        if player.cooldown == 10:
            if player.last_direction < 0:
                player.image = pg.transform.flip(player.agr_image[1], True, False)
            else:
                player.image = pg.transform.flip(player.agr_image[1], False, False)
        if player.cooldown == 50:
            if player.last_direction < 0:
                player.image = pg.transform.flip(player.agr_image[2], True, False)
            else:
                player.image = pg.transform.flip(player.agr_image[2], False, False)
        if player.cooldown > 80:
            player.cooldown = 0
            player.kd = False
            player.can_move = True

    background.update(player)
    for i in gorizontal_platforms:
        i.update(screen, player)
    for enemy in enemies:
        if enemy.rect.colliderect(player.rect):
            player.rect.y += 5
            for i in range(len(player.died_image)):
                if player.last_direction > 0:
                    player.image = player.died_image[i]
                else:
                    player.image = pg.transform.flip(player.died_image[i], True, False)
                background.update(player)
                for j in gorizontal_platforms:
                    j.update(screen, player)
                for j in enemies:
                    j.update(player)
                for j in died_mas:
                    j.update(player)
                screen.blit(player.image, player.rect)
                pg.display.flip()
                pg.time.delay(100)
            pg.time.delay(1000)
            die_action(screen, BUTTON)
        enemy.update(player)
    for enemy in died_mas:
        enemy.died_moment(died_mas, player)

    player.rect.x += player.direction.x * player.speed
    for i in gorizontal_platforms:
        if i.rect.colliderect(player.rect):
            if player.direction.x < 0 and player.rect.left <= i.rect.right:
                player.rect.left = i.rect.right
            elif player.direction.x > 0 and player.rect.right >= i.rect.left:
                player.rect.right = i.rect.left

    player.f_gravity()
    if GROUND.rect.colliderect(player.rect):
        if player.direction.y > 0:
            player.rect.bottom = GROUND.rect.top
            player.direction.y = 0
            player.on_ground = True
    for i in gorizontal_platforms:
        if i.rect.colliderect(player.rect):
            if player.direction.y > 0 and player.rect.bottom < i.rect.top + i.rect.width:
                player.rect.bottom = i.rect.top
                player.direction.y = 0
                player.on_ground = True
            elif player.direction.y < 0 and player.rect.top > i.rect.bottom - i.rect.width:
                player.rect.top = i.rect.bottom
                player.direction.y = 0

    if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
        player.on_ground = False

    player.update()
    mini_menu(screen)
    enemies_count(screen, len(enemies))

    if enemies == []:
        you_win()


def enemies_count(screen, count):
    win = pg.Surface(size=(SIZE.current_h // 5, SIZE.current_h // 10))
    rect = win.get_rect()
    rect.center = SIZE.current_w // 2, round(SIZE.current_h * 0.06)
    win.fill((30, 0, 60))
    pg.draw.rect(win, (pg.Color('orange')), win.get_rect(), 5)
    screen.blit(win, rect)
    s = int(SIZE.current_w * 0.02)
    f1 = pg.font.SysFont('arial', s).render(f'Осталось:{count}', True, pg.Color('orange'))
    ff1 = f1.get_rect(center=(SIZE.current_w // 2, SIZE.current_h * 0.06))
    screen.blit(f1, ff1)


def mini_menu(screen):
    sw = int(SIZE.current_w * 0.078125)
    sh = int(SIZE.current_h * 0.139)

    pg.draw.rect(screen, (30, 0, 60), ((0, 0), (sw, sh)))
    pg.draw.rect(screen, (pg.Color('orange')), ((0, 0), (sw, sh)), 5)
    miniBUTTON.draw(sw * 0.5, SIZE.current_h * 0.02315, "EXIT", game_exit, screen, pressed)
    miniBUTTON.draw(sw * 0.5, SIZE.current_h * 0.0645, "RESTART", game_restart, screen, pressed)
    miniBUTTON.draw(sw * 0.5, SIZE.current_h * 0.1065, 'MAIN MENU', vacant, screen, pressed)



def you_win():
    global timer
    sound = pg.mixer.Sound('data/winner_sound.mp3')
    sound.set_volume(0.3)
    sound.play()
    win = pg.Surface(size=(SIZE.current_h // 2, SIZE.current_h // 6))
    rect = win.get_rect()
    rect.center = SIZE.current_w // 2, SIZE.current_h // 2
    win.fill((30, 0, 60))
    pg.draw.rect(win, (pg.Color('orange')), win.get_rect(), 5)
    screen.blit(win, rect)

    f1 = pg.font.SysFont('arial', int(SIZE.current_w * 0.03125), bold=True).render('YOU WIN', True, pg.Color('red'))
    ff1 = f1.get_rect(center=(SIZE.current_w // 2, SIZE.current_h // 2))
    screen.blit(f1, ff1)
    timer += 1
    if timer > 500:
        timer = 0
        vacant(screen)


if __name__ == '__main__':
    running = True
    pg.mixer.music.load('data/gurenge_8_bit.mp3')
    pg.mixer.music.set_volume(0.4)
    pg.mixer.music.play(-1)
    elapsed = 0
    while running:
        pressed = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    pressed = True
        if menu:
            show_main_menu(screen)
        if game:
            g_begin()
        clock.tick(fps)
        pg.display.update()
    pg.quit()