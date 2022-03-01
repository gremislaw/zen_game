import pygame as pg
from help import *
SIZE = get_size()

class Map:
    def __init__(self, screen):
        self.trees = pg.image.load('data/trees.png').convert_alpha(screen)
        self.trees = pg.transform.scale(self.trees, (SIZE.current_w, SIZE.current_h))
        self.rect = self.trees.get_rect()
        self.screen = screen
        self.shift = 0

    def move(self, player):
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SIZE.current_w // 4 and direction_x < 0:
            self.shift = int(SIZE.current_w * 0.0042)
            player.speed = 0
        elif player_x > SIZE.current_w - (SIZE.current_w // 4) and direction_x > 0:
            self.shift = -int(SIZE.current_w * 0.0042)
            player.speed = 0
        else:
            self.shift = 0
            player.speed = int(SIZE.current_w * 0.0042)

    def after_slash(self, player, shift, en, pl, de):
        player_x = player.rect.centerx
        direction_x = player.last_direction
        if player_x < SIZE.current_w // 4 and direction_x < 0:
            self.rect.x += shift
            player.rect.x += shift
            for i in en:
                i.rect.x += shift
                i.spawn[0] += shift
            for i in pl:
                i.rect.x += shift
            for i in de:
                i.rect.x += shift
        elif player_x > SIZE.current_w - (SIZE.current_w // 4) and direction_x > 0:
            self.rect.x -= shift
            player.rect.x -= shift
            for i in en:
                i.rect.x -= shift
                i.spawn[0] -= shift
            for i in pl:
                i.rect.x -= shift
            for i in de:
                i.rect.x -= shift

    def update(self, player):
        self.rect.x += self.shift
        rel_x = self.rect.x % self.rect.width
        self.move(player)
        self.screen.blit(self.trees, (rel_x - self.rect.width, 0))
        if rel_x < SIZE.current_w:
            self.screen.blit(self.trees, (rel_x, 0))

