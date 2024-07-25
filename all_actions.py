import pygame as pg
from Button_ import *
from Level import *



pg.init()
SIZE = get_size()
screen = pg.display.set_mode((SIZE.current_w, SIZE.current_h))
pg.display.set_caption('1000 - 7')
clock = pg.time.Clock()
fps = 75
running = True
gameAbout = [False]
gameControls = [False]
music_play = [True]
small = SIZE.current_h * 0.075, SIZE.current_h * 0.02
timer = 0
kd_line_coef = 0
pressed = False


class AllActions:
    def __init__(self):
        self.kd_line_coef = 0
        self.die_menu = False
        self.menu = True
        self.game = False
        self.have_intersect = False
        self.have_intersect_close = False
        self.gameAboutClosed = True
        self.gameControlsClosed = True
        self.create_buttons()
        self.menu_update()

    def create_buttons(self):
        BigBtnSize = SIZE.current_w * 0.08, SIZE.current_h * 0.04
        MiniBtnX, MiniBtnY = int(SIZE.current_w * 0.078125), int(SIZE.current_h * 0.139)
        MiniBtnSize = SIZE.current_w * 0.03125, SIZE.current_h * 0.0185
        CloseBtnSize = SIZE.current_w * 0.01, SIZE.current_h * 0.017
        wasd = pg.Surface(size=(SIZE.current_h // 2, SIZE.current_h // 2))
        rect = wasd.get_rect()
        rect.center = SIZE.current_w // 2, SIZE.current_h // 2
        self.btn_start = Button(*BigBtnSize, SIZE.current_w / 5, SIZE.current_h / 1.9, self.game_start, screen)
        self.btn_about = Button(*BigBtnSize, (SIZE.current_w * 2) / 5, SIZE.current_h / 1.9, self.change_flag, screen)
        self.btn_controls = Button(*BigBtnSize, (SIZE.current_w * 3) / 5, SIZE.current_h / 1.9, self.change_flag, screen)
        self.btn_exit = Button(*BigBtnSize, (SIZE.current_w * 4) / 5, SIZE.current_h / 1.9, self.game_exit, screen)
        self.btn_music_off = Button(small[0], small[1], SIZE.current_w - 100, 50, self.change_flag, screen)
        self.btn_menu = Button(*BigBtnSize, SIZE.current_w / 2, SIZE.current_h / 2.5, self.main_menu_start, screen)
        self.btn_die_exit = Button(*BigBtnSize, SIZE.current_w / 2, SIZE.current_h / 2, self.game_exit, screen)
        self.btn_restart = Button(*BigBtnSize, SIZE.current_w / 2, SIZE.current_h / 3.3, self.game_restart, screen)
        self.mini_btn_exit = Button(*MiniBtnSize, MiniBtnX * 0.5, SIZE.current_h * 0.02315, self.game_exit, screen)
        self.mini_btn_restart = Button(*MiniBtnSize, MiniBtnX * 0.5, SIZE.current_h * 0.0645, self.game_restart, screen)
        self.mini_btn_menu = Button(*MiniBtnSize, MiniBtnX * 0.5, SIZE.current_h * 0.1065, self.main_menu_start, screen)
        self.btn_close_controls = Button(*CloseBtnSize, rect.x + rect.width * 0.98, rect.y * 1.02, self.close_controls, screen)
        self.btn_close_about = Button(*CloseBtnSize, rect.x + rect.width * 0.98, rect.y * 1.02, self.close_about, screen)

    def change_flag(self, s, flag):
        if flag[0]:
            flag[0] = False
        else:
            flag[0] = True

    def change_action(self, flag):
        for i in range(3):
            if flag == 'die_menu':
                self.die_menu = True
                self.menu = False
                self.game = False
            elif flag == 'main_menu':
                self.die_menu = False
                self.menu = True
                self.game = False
            elif flag == 'game':
                self.die_menu = False
                self.menu = False
                self.game = True

    def game_about(self, screen):
        info = pg.Surface(size=(SIZE.current_h // 2, SIZE.current_h // 2))
        rect = info.get_rect()
        rect.center = SIZE.current_w // 2, SIZE.current_h // 2
        info.fill((30, 0, 60))
        pg.draw.rect(info, pg.Color('orange'), info.get_rect(), 5)
        screen.blit(info, rect)
        s = int(SIZE.current_w * 0.01)
        fs = [
            'Когда Зеницу был моложе, он был влюблён в девушку,',
            'которая обманом заставила его собирать деньги,',
            'чтобы сбежать со своим возлюбленным. Из-за того, что',
            'девушка была по уши в долгах, у Зеницу появились проблемы,',
            'но его спас бывший столп грома Джигоро Куваджима.',
            'Чтобы вернуть ему долг, Зеницу пришлось пройти',
            'через адские тренировки и стать истребителем демонов.',
        ]
        x = SIZE.current_w // 2.7
        val = 0.3
        y = SIZE.current_h
        for i in range(len(fs)):
            f = pg.font.SysFont('franklingothicmedium', s).render(
                fs[i], True, pg.Color('orange'))
            ff = f.get_rect(x=x, y=y * val)
            screen.blit(f, ff)
            val += 0.05
        f8 = pg.font.SysFont('franklingothicmedium', s + 20, bold=True).render(
            'Победи всех врагов!', True, (140, 0, 0))
        ff8 = f8.get_rect(center=(SIZE.current_w // 2, SIZE.current_h // 1.5))
        screen.blit(f8, ff8)
        self.btn_close_about.draw('x', pressed)

    def close_about(self, screen):
        self.gameAboutClosed = True
        self.menu_update()

    def game_exit(self, a):
        pg.quit()
        exit()

    def game_controls(self, screen):
        wasd = pg.Surface(size=(SIZE.current_h // 2, SIZE.current_h // 2))
        rect = wasd.get_rect()
        rect.center = SIZE.current_w // 2, SIZE.current_h // 2
        wasd.fill((30, 0, 60))
        pg.draw.rect(wasd, (pg.Color('orange')), wasd.get_rect(), 5)
        screen.blit(wasd, rect)
        s = int(SIZE.current_w * 0.031)
        fs = [
            '"→" - go to right',
            '"←" - go to left',
            '"↑" - jump',
            '"↓" - slash'
        ]
        x = SIZE.current_w // 2.6
        val = 0.3
        y = SIZE.current_h
        for i in range(len(fs)):
            f = pg.font.SysFont('arial', s).render(fs[i], True, pg.Color('orange'))
            ff = f.get_rect(x=x, y=y * val)
            screen.blit(f, ff)
            val += 0.1
        self.btn_close_controls.draw('x', pressed)

    def close_controls(self, screen):
        self.gameControlsClosed = True
        self.menu_update()

    def die_action(self, screen):
        press = False
        screen.fill((0, 0, 0))
        sound = pg.mixer.Sound('data/musics/NOOO.mp3')
        sound.set_volume(0.5)
        sound.play()
        for i in range(300):
            self.died(screen, 1, press, i)
            pg.time.delay(1)
            pg.display.flip()
        self.change_action('die_menu')

    def died(self, screen, type, press, size=None):
        if type == 1:
            screen.fill((0, 0, 0))
            font = pg.font.SysFont('centaur', size // 2, italic=True)
            text = font.render(
                "YOU DIED...", True, (100, 0, 0))
            place = text.get_rect(
                center=(SIZE.current_w // 2, SIZE.current_h // 2))
            screen.blit(text, place)
        else:
            image = pg.image.load('data/imgs/died_menu.jpg').convert()
            image = pg.transform.scale(image, (SIZE.current_w, SIZE.current_h))
            screen.blit(image, image.get_rect())
            self.btn_menu.draw('MAIN MENU', press)
            self.btn_die_exit.draw("EXIT", press)
            self.btn_restart.draw("RESTART", press)

    def game_restart(self, screen):
        self.game_start(screen)

    def main_menu_start(self, screen):
        if music_play:
            pg.mixer.music.load('data/musics/zankyou_8_bit.mp3')
            pg.mixer.music.set_volume(0.4)
            pg.mixer.music.play(-1)
        self.change_action('main_menu')

    def game_start(self, screen):
        global background, gplatforms, gorizontal_platforms, player, enemies, GROUND, died_mas
        background, gplatforms, gorizontal_platforms, player, enemies, GROUND, died_mas = start(screen, music_play)
        self.change_action('game')

    def draw_objects(self):
        background.update(player)
        for i in gorizontal_platforms:
            i.update(screen, player)
        for enemy in enemies:
            if enemy.rect.colliderect(player.rect):
                if not player.damaged[0]:
                    player.hp -= 1
                    player.damaged = (True, enemy.direction.x)
                    player.direction.x = 0
                    player.can_move = False
            enemy.update(player)
        for enemy in died_mas:
            enemy.died_moment(died_mas, player)
        player.update()

    def check_hero_intersect(self):
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

    def draw_slash_cooldown(self):
        sw, sh = int(SIZE.current_w * 0.2), int(SIZE.current_h * 0.015)
        xy = int(SIZE.current_w * 0.5) - sw * 0.5, int(SIZE.current_h * 0.95)
        if player.kd:
            self.kd_line_coef += sw / 60
            pg.draw.rect(screen, (90, 60, 120), (xy, (self.kd_line_coef, sh)))
            pg.draw.rect(screen, pg.Color('orange'), (xy, (sw, sh)), 1)
        else:
            self.kd_line_coef = 0
            pg.draw.rect(screen, (90, 60, 120), (xy, (sw, sh)))
            pg.draw.rect(screen, pg.Color('orange'), (xy, (sw, sh)), 1)

    def enemies_count(self, screen, count):
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

    def mini_menu(self, screen):
        sw = int(SIZE.current_w * 0.078125)
        sh = int(SIZE.current_h * 0.139)
        pg.draw.rect(screen, (30, 0, 60), ((0, 0), (sw, sh)))
        pg.draw.rect(screen, (pg.Color('orange')), ((0, 0), (sw, sh)), 5)
        self.mini_btn_exit.draw("EXIT", pressed)
        self.mini_btn_restart.draw("RESTART", pressed)
        self.mini_btn_menu.draw('MAIN MENU', pressed)

    def you_win(self):
        global timer
        sound = pg.mixer.Sound('data/musics/winner_sound.mp3')
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
            self.main_menu_start(screen)

    def draw_interface(self):
        self.mini_menu(screen)
        self.enemies_count(screen, len(enemies))
        self.draw_slash_cooldown()
        # победил?
        if enemies == []:
            self.you_win()

    def menu_update(self):
        image = pg.image.load('data/imgs/main_menu.png').convert_alpha()
        image = pg.transform.scale(image, (SIZE.current_w, SIZE.current_h))
        screen.blit(image, image.get_rect())
        self.btn_start.draw("START", pressed)
        self.btn_about.draw("ABOUT", pressed, gameAbout)
        self.btn_controls.draw("CONTROLS", pressed, gameControls)
        self.btn_exit.draw("EXIT", pressed)
        if music_play[0]:
            self.btn_music_off.draw('MUSIC ON', pressed, music_play)
            pg.mixer.music.unpause()
        else:
            self.btn_music_off.draw('MUSIC OFF', pressed, music_play)
            pg.mixer.music.pause()

    def intersect_with_btns(self):
        if self.gameControlsClosed and self.gameAboutClosed:
            if self.btn_start.check_intersect() or self.btn_about.check_intersect() or self.btn_controls.check_intersect() \
                    or self.btn_exit.check_intersect() or self.btn_music_off.check_intersect():
                    self.menu_update()
                    self.have_intersect = True
            elif self.have_intersect:
                self.have_intersect = False
                self.menu_update()

    def intersect_with_close_btns(self):
        if self.btn_close_controls.check_intersect() and not self.gameControlsClosed:
            self.btn_close_controls.draw('x', pressed)
            self.have_intersect_close = True
        elif self.have_intersect_close and not self.gameControlsClosed:
            self.have_intersect_close = False
            self.btn_close_controls.draw('x', pressed)

        if self.btn_close_about.check_intersect() and not self.gameAboutClosed:
            self.btn_close_about.draw('x', pressed)
            self.have_intersect_close = True
        elif self.have_intersect_close and not self.gameAboutClosed:
            self.have_intersect_close = False
            self.btn_close_about.draw('x', pressed)


    def show_main_menu(self, screen):
        self.intersect_with_btns()
        self.intersect_with_close_btns()
        # Нажата кнопка About
        if gameAbout[0]:
            self.game_about(screen)
            gameAbout[0] = False
            self.gameAboutClosed = False
        # Нажата кнопка Controls
        if gameControls[0]:
            self.game_controls(screen)
            gameControls[0] = False
            self.gameControlsClosed = False

    def g_begin(self):
        # ударил ли герой
        player.check_player_normal_attack(background, gorizontal_platforms, enemies, died_mas)
        # рисуем все
        self.draw_objects()
        # интерфейс
        self.draw_interface()
        # проверяем умер ли наш герой
        if player.hp <= 0 and player.player_after_damaged >= 120:
            self.die_action(screen)
        # физика
        self.check_hero_intersect()
