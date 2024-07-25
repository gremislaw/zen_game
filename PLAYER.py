import pygame as pg
import pygame.gfxdraw as gfx
from help import *

class Player(pg.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.move_image = img_convert(
            pg.image.load('data/zen/zenitsu.png').convert_alpha(),
            pg.image.load('data/zen/zenitsu2.png').convert_alpha(),
            pg.image.load('data/zen/zenitsu3.png').convert_alpha(),
            pg.image.load('data/zen/zenitsu4.png').convert_alpha()
                                      )
        self.direction = pg.math.Vector2(0, 0)
        self.speed = int(SIZE.current_w * 0.0042)
        self.gravity = int(SIZE.current_h * 0.00741) / 10
        self.jump_speed = -int(SIZE.current_h * 0.019)
        self.jumped_image = img_convert(
            pg.image.load('data/zen/zenitsuJUMP.png').convert_alpha(screen),
            pg.image.load('data/zen/zenitsuJUMP2.png').convert_alpha(screen),
            pg.image.load('data/zen/zenitsuJUMP3.png').convert_alpha(screen),
            pg.image.load('data/zen/zenitsuJUMP4.png').convert_alpha(screen),
            pg.image.load('data/zen/zenitsuJUMP5.png').convert_alpha(screen)
        )
        self.afk_image = img_convert(
            pg.image.load('data/zen/zenitsuAFK.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK2.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK3.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK4.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK5.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK6.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK7.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK8.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK9.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK10.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK11.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK12.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK13.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK14.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK15.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK16.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK17.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK18.png').convert_alpha(),
            pg.image.load('data/zen/zenitsuAFK19.png').convert_alpha()
                                     )
        self.agr_image = img_convert_slash(
            pg.image.load('data/zen/zenitsu_agr.png').convert_alpha(),
            pg.image.load('data/zen/zenitsu_agr2.png').convert_alpha(),
            pg.image.load('data/zen/zenitsu_agr3.png').convert_alpha()
        )
        self.died_image = img_convert_slash(
            pg.image.load('data/zen/zenitsuDIED.png'),
            pg.image.load('data/zen/zenitsuDIED2.png'),
            pg.image.load('data/zen/zenitsuDIED3.png'),
            pg.image.load('data/zen/zenitsuDIED4.png')
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
        self.damaged = (False, 0)
        self.effect_timer = 0
        self.afk = 0
        self.last_direction = 1
        self.jump_index = 0
        self.jump_index2 = 0
        self.hp = 3
        self.max_hp = 3
        self.brumen1, self.brumen2 = 0, 0
        self.player_after_damaged = 0

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
                self.afk = 0
            elif keys[pg.K_RIGHT]:
                self.direction.x = 1
                self.image = self.move_image[self.run]
                self.last_direction = 1
                self.afk = 0
            else:
                self.direction.x = 0
                if self.last_direction < 0:
                    self.image = pg.transform.flip(self.afk_image[self.afk], True, False)
                else:
                    self.image = self.afk_image[self.afk]
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
            if self.effect_timer > 50:
                self.effect_timer = 0
                self.ability_flag = False

    def slash(self, enemies, shift, died_mas):
        slash_sound = pg.mixer.Sound('data/zen/zenitsu_slash.mp3')
        slash_sound.set_volume(0.3)
        killed_slash_sound = pg.mixer.Sound('data/zen/zenitsu_killed_slash.mp3')
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
        self.afk = 0

    def jump(self):
        if self.on_ground:
            self.direction.y = self.jump_speed
            self.afk = 0

    def draw_hp(self):
        pg.draw.rect(self.screen, (150, 20, 20), (
            (self.rect.x, self.rect.y * 0.97), (self.rect.width * self.hp // self.max_hp, self.rect.height * 0.1)))
        pg.draw.rect(self.screen, pg.Color('orange'),
                     ((self.rect.x, self.rect.y * 0.97), (self.rect.width, self.rect.height * 0.1)), 1)
        if self.damaged[0] and self.hp > 0:
            self.player_after_damaged += 1
            if self.player_after_damaged < 60:
                if self.damaged[1] > 0:
                    self.image = pg.transform.flip(self.died_image[self.brumen2], True, False)
                    self.rect.x += 1
                else:
                    self.image = self.died_image[self.brumen2]
                    self.rect.x -= 1
                self.brumen1 += 1
                if self.brumen1 == 15:
                    self.brumen1 = 0
                    self.brumen2 += 1
                    if self.brumen2 == 4:
                        self.brumen2 = 0
            elif self.player_after_damaged == 60:
                self.brumen1 = 0
                self.brumen2 = 0
            elif self.player_after_damaged < 120:
                if self.damaged[1] > 0:
                    self.image = pg.transform.flip(self.died_image[3 - self.brumen2], True, False)
                else:
                    self.image = self.died_image[3 - self.brumen2]
                self.brumen1 += 1
                if self.brumen1 == 15:
                    self.brumen1 = 0
                    self.brumen2 += 1
                    if self.brumen2 == 4:
                        self.brumen2 = 0
                gfx.aacircle(self.screen, self.rect.centerx, self.rect.centery, self.rect.width,
                                    pg.Color(255, 255, 255, 255 - 50 * (4 - self.brumen2)))
            if self.player_after_damaged == 120:
                self.can_move = True
            if 120 < self.player_after_damaged < 400:
                if 400 > self.player_after_damaged > 300:
                    if self.player_after_damaged % 4 == 0:
                        a = 200
                    elif self.player_after_damaged % 4 == 1:
                        a = 150
                    elif self.player_after_damaged % 4 == 2:
                        a = 100
                    elif self.player_after_damaged % 4 == 3:
                        a = 50
                    gfx.filled_circle(self.screen, self.rect.centerx, self.rect.centery, self.rect.width,
                                      pg.Color(255, 255, 255, 50 - 10 * (self.player_after_damaged % 4)))
                    gfx.aacircle(self.screen, self.rect.centerx, self.rect.centery, self.rect.width,
                                        pg.Color(255, 255, 255, a))
                else:
                    gfx.filled_circle(self.screen, self.rect.centerx, self.rect.centery, self.rect.width,
                                        pg.Color(255, 255, 255, 50))
                    gfx.aacircle(self.screen, self.rect.centerx, self.rect.centery, self.rect.width,
                                        pg.Color('white'))

            elif self.player_after_damaged == 400:
                self.player_after_damaged = 0
                self.brumen1 = 0
                self.brumen2 = 0
                self.damaged = (False, 0)

        if self.hp <= 0:
            self.player_after_damaged += 1
            if self.player_after_damaged < 60:
                if self.damaged[1] > 0:
                    self.image = pg.transform.flip(self.died_image[self.brumen2], True, False)
                else:
                    self.image = self.died_image[self.brumen2]
                self.brumen1 += 1
                if self.brumen1 == 15:
                    self.brumen1 = 0
                    self.brumen2 += 1
                    if self.brumen2 == 4:
                        self.brumen2 = 0
            if self.player_after_damaged > 120:
                self.player_after_damaged = 0
                self.brumen1 = 0
                self.brumen2 = 0
                self.damaged = (False, 0)

    def check_player_normal_attack(self, background, gorizontal_platforms, enemies, died_mas):
        if pg.key.get_pressed()[pg.K_DOWN] and self.cooldown == 0 and self.can_move:
            shift = int(SIZE.current_w * 0.078125)
            if self.last_direction > 0:
                x_last = self.rect.left
            elif self.last_direction < 0:
                x_last = self.rect.left
            self.rect.x += shift * self.last_direction
            for i in gorizontal_platforms:
                if i.rect.colliderect(self.rect):
                    if self.last_direction < 0 and self.rect.left <= i.rect.right:
                        self.rect.left = i.rect.right
                        shift = x_last - self.rect.left
                    elif self.last_direction > 0 and self.rect.right >= i.rect.left:
                        self.rect.right = i.rect.left
                        shift = self.rect.left - x_last
            self.slash(enemies, shift, died_mas)
            background.after_slash(self, shift, enemies, gorizontal_platforms, died_mas)
            self.kd = True
        if self.kd:
            self.cooldown += 1
            if self.cooldown == 1:
                if self.last_direction < 0:
                    self.image = pg.transform.flip(self.agr_image[0], True, False)
                else:
                    self.image = self.agr_image[0]
            if self.cooldown == 10:
                if self.last_direction < 0:
                    self.image = pg.transform.flip(self.agr_image[1], True, False)
                else:
                    self.image = self.agr_image[1]
            if self.cooldown == 50:
                if self.player_after_damaged > 0:
                    if self.player_after_damaged > 120:
                        self.can_move = True
                else:
                    self.can_move = True
            if self.cooldown == 30:
                if self.last_direction < 0:
                    self.image = pg.transform.flip(self.agr_image[2], True, False)
                else:
                    self.image = self.agr_image[2]
            if self.cooldown > 60:
                self.cooldown = 0
                self.kd = False

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
        self.draw_hp()