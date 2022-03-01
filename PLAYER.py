import pygame as pg
from help import *


class Player(pg.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.move_image = img_convert(
            pg.image.load('data/zenitsu.png').convert_alpha(),
            pg.image.load('data/zenitsu2.png').convert_alpha(),
            pg.image.load('data/zenitsu3.png').convert_alpha(),
            pg.image.load('data/zenitsu4.png').convert_alpha()
                                      )
        self.direction = pg.math.Vector2(0, 0)
        self.speed = int(SIZE.current_w * 0.0042)
        self.gravity = int(SIZE.current_h * 0.00741) / 10
        self.jump_speed = -int(SIZE.current_h * 0.019)
        self.jumped_image = img_convert(
            pg.image.load('data/zenitsuJUMP.png').convert_alpha(screen),
            pg.image.load('data/zenitsuJUMP2.png').convert_alpha(screen),
            pg.image.load('data/zenitsuJUMP3.png').convert_alpha(screen),
            pg.image.load('data/zenitsuJUMP4.png').convert_alpha(screen),
            pg.image.load('data/zenitsuJUMP5.png').convert_alpha(screen)
        )
        self.afk_image = img_convert(
            pg.image.load('data/zenitsuAFK.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK2.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK3.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK4.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK5.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK6.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK7.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK8.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK9.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK10.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK11.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK12.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK13.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK14.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK15.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK16.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK17.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK18.png').convert_alpha(),
            pg.image.load('data/zenitsuAFK19.png').convert_alpha()
                                     )
        self.agr_image = img_convert_slash(
            pg.image.load('data/zenitsu_agr.png').convert_alpha(),
            pg.image.load('data/zenitsu_agr2.png').convert_alpha(),
            pg.image.load('data/zenitsu_agr3.png').convert_alpha()
        )
        self.died_image = img_convert_slash(
            pg.image.load('data/zenitsuDIED.png'),
            pg.image.load('data/zenitsuDIED2.png'),
            pg.image.load('data/zenitsuDIED3.png'),
            pg.image.load('data/zenitsuDIED4.png')
        )
        self.rect = self.afk_image[0].get_rect()
        self.rect.x = get_size().current_w * 0.5
        self.image = self.afk_image[0]
        self.run = 0
        self.anim = 0
        self.on_ground = False
        self.cooldown = 0
        self.kd = False
        self.ability_flag = False
        self.sleep = False
        self.can_move = True
        self.effect_timer = 0
        self.afk = 0
        self.last_direction = 1
        self.jump_index = 0
        self.jump_index2 = 0

    def f_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def move(self):
        if self.can_move:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.direction.x = -1
                self.image = pg.transform.flip(self.move_image[self.run], True, False)
                self.last_direction = -1
            elif keys[pg.K_RIGHT]:
                self.direction.x = 1
                self.image = pg.transform.flip(self.move_image[self.run], False, False)
                self.last_direction = 1
            else:
                self.direction.x = 0
                if self.last_direction < 0:
                    self.image = pg.transform.flip(self.afk_image[self.afk], True, False)
                else:
                    self.image = pg.transform.flip(self.afk_image[self.afk], False, False)
            self.anim += 1
            if self.anim == 15:
                self.afk += 1
                self.run += 1
                if self.run == 4:
                    self.run = 0
                if self.afk == 19:
                    self.afk = 0
                self.anim = 0
            if keys[pg.K_UP]:
                self.jump()

    def ability_effect(self):
        if self.ability_flag:
            self.effect_timer += 1
            self.actual_move_image = self.agr_image
            if self.effect_timer > 50:
                self.effect_timer = 0
                self.ability_flag = False

    def slash(self, enemies, shift, died_mas):
        slash_sound = pg.mixer.Sound('data/zenitsu_slash.mp3')
        slash_sound.set_volume(0.3)
        killed_slash_sound = pg.mixer.Sound('data/zenitsu_killed_slash.mp3')
        killed_slash_sound.set_volume(0.3)
        right = self.rect.right
        bottom = self.rect.bottom
        top = self.rect.top
        left = self.rect.left
        to_remove = []
        for enemy in enemies:
            if self.last_direction > 0:
                if enemy.rect.right > left - shift and enemy.rect.left <= right and enemy.rect.top <= bottom and enemy.rect.bottom >= top:
                    killed_slash_sound.play()
                    to_remove.append(enemy)
                self.ability_flag = True
            elif self.last_direction < 0:
                if enemy.rect.left < right + shift and enemy.rect.right > left and enemy.rect.top <= bottom and enemy.rect.bottom >= top:
                    killed_slash_sound.play()
                    to_remove.append(enemy)
                self.ability_flag = True
        for enemy in to_remove:
            enemies.remove(enemy)
            died_mas.append(enemy)

        if to_remove == []:
            slash_sound.play()
        self.can_move = False
        self.direction.x = 0

    def jump(self):
        if self.on_ground:
            self.direction.y = self.jump_speed

    def update(self):
        self.move()
        if not self.on_ground and self.can_move:
            if self.last_direction > 0:
                self.image = self.jumped_image[self.jump_index]
            else:
                self.image = pg.transform.flip(self.jumped_image[self.jump_index], True, False)
            self.jump_index2 += 1
            if self.jump_index2 == 10:
                self.jump_index2 = 0
                self.jump_index += 1
                if self.jump_index == 5:
                    self.jump_index = 0
        self.ability_effect()
        self.screen.blit(self.image, self.rect)