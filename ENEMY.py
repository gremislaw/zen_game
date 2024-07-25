import random

import pygame as pg
from help import *

SIZE = get_size()


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, type, screen):
        super().__init__()
        self.screen = screen
        self.type = type
        self.direction = pg.math.Vector2(0, 0)
        if self.type == 'normal1':
            self.speed = int(SIZE.current_w * 0.0021)
            self.move_image = demon2_convert(
                pg.image.load('data/demon2/demon.png').convert_alpha(screen),
                pg.image.load('data/demon2/demon2.png').convert_alpha(screen)
            )
            self.died_image = demon2_died_convert(
                pg.image.load('data/demon2/demon_died.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died2.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died3.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died4.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died5.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died6.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died7.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died8.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died9.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died10.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died11.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died12.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died13.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died14.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died15.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died16.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died17.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died18.png').convert_alpha()
            )
        elif self.type == 'normal2':
            self.speed = int(SIZE.current_w * 0.00105)
            self.move_image = demon2_convert(
                pg.image.load('data/demon2/demon.png').convert_alpha(screen),
                pg.image.load('data/demon2/demon2.png').convert_alpha(screen)
            )
            self.died_image = demon2_died_convert(
                pg.image.load('data/demon2/demon_died.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died2.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died3.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died4.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died5.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died6.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died7.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died8.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died9.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died10.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died11.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died12.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died13.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died14.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died15.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died16.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died17.png').convert_alpha(),
                pg.image.load('data/demon2/demon_died18.png').convert_alpha()
            )
        self.rect = self.move_image[0].get_rect()
        self.rect.midbottom = x, y
        self.spawn = [x, y]
        self.image = self.move_image[0]
        self.i = 0
        self.shift = 0
        self.napr = 'left'
        self.frame = 0
        self.anim = 0
        self.die_anim = 0


    def move(self, player):
        if self.type == 'normal1' or self.type == 'normal2':
            if self.napr == 'left':
                self.direction.x = -1
                self.image = pg.transform.flip(self.move_image[self.frame], False, False)
            elif self.napr == 'right':
                self.direction.x = 1
                self.image = pg.transform.flip(self.move_image[self.frame], True, False)
            self.i += 1
            if self.i == 20:
                self.i = 0
                self.frame += 1
                if self.frame == 2:
                    self.frame = 0
            self.check_napr()

    def check_napr(self):
        if self.type == 'normal1' or self.type == 'normal2':
            if self.rect.centerx <= self.spawn[0] - random.randint(70, 300):
                self.napr = 'right'
            elif self.rect.centerx >= self.spawn[0] + random.randint(70, 300):
                self.napr = 'left'


    def died_moment(self, died_mas, player):
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < SIZE.current_w // 4 and direction_x < 0:
            self.shift = int(SIZE.current_w * 0.0042)
            self.spawn[0] += int(SIZE.current_w * 0.0042)
            player.speed = 0
        elif player_x > SIZE.current_w - (SIZE.current_w // 4) and direction_x > 0:
            self.shift = -int(SIZE.current_w * 0.0042)
            self.spawn[0] -= int(SIZE.current_w * 0.0042)
            player.speed = 0
        else:
            self.shift = 0
            player.speed = int(SIZE.current_w * 0.0042)
        self.rect.x += self.shift

        if self.napr == 'left':
            self.image = self.died_image[self.die_anim]
        else:
            self.image = pg.transform.flip(self.died_image[self.die_anim], True, False)
        self.anim += 1
        if self.anim == 7:
            self.die_anim += 1
            self.anim = 0
            if self.die_anim == 18:
                died_mas.remove(self)
        self.screen.blit(self.image, self.rect)

    def update(self, player):
        self.move(player)
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < SIZE.current_w // 4 and direction_x < 0:
            self.shift = int(SIZE.current_w * 0.0042)
            self.spawn[0] += int(SIZE.current_w * 0.0042)
            player.speed = 0
        elif player_x > SIZE.current_w - (SIZE.current_w // 4) and direction_x > 0:
            self.shift = -int(SIZE.current_w * 0.0042)
            self.spawn[0] -= int(SIZE.current_w * 0.0042)
            player.speed = 0
        else:
            self.shift = 0
            player.speed = int(SIZE.current_w * 0.0042)

        self.rect.x += self.shift
        self.rect.x += self.direction.x * self.speed
        self.screen.blit(self.image, self.rect)