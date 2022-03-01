import pygame as pg
from help import *

SIZE = get_size()
PLATFORM_WIDTH = SIZE.current_w * 0.3125
PLATFORM_HEIGHT = SIZE.current_h * 0.1
SMALLPLATFORM_WIDTH = SIZE.current_w * 0.05
SMALLPLATFORM_HEIGHT = SIZE.current_h * 0.1
PLATFORM_COLOR = "#FF6262"
WALL_WIDTH = SIZE.current_h * 0.1
WALL_HEIGHT = SIZE.current_h * 10


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, color=PLATFORM_COLOR):
        pg.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pg.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT - 40))
        if color == None:
            self.image = pg.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT), pg.SRCALPHA)
        else:
            self.image = pg.image.load('data/platform1.png').convert_alpha(self.image)
            self.image = pg.transform.scale(self.image, (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = self.image.get_rect(center=(x, y))
        self.shift = 0
        self.timer = 0
        self.i = 1

    def move(self, player):
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SIZE.current_w / 4 and direction_x < 0:
            self.shift = int(SIZE.current_w * 0.0042)
            player.speed = 0
        elif player_x > SIZE.current_w - (SIZE.current_w / 4) and direction_x > 0:
            self.shift = -int(SIZE.current_w * 0.0042)
            player.speed = 0
        else:
            self.shift = 0
            player.speed = int(SIZE.current_w * 0.0042)

    def update(self, screen, player):
        self.timer += 1
        if self.timer == 60:
            self.timer = 0
            self.i += 1
            if self.i == 4:
                self.i = 0
        self.move(player)
        self.rect.x += self.shift
        screen.blit(self.image, self.rect)


class ThinPlatform(Platform):
    def __init__(self, x, y, color=PLATFORM_COLOR):
        pg.sprite.Sprite.__init__(self)
        Platform.__init__(self, x, y, color)
        self.image = pg.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT - 40))
        if color == None:
            self.image = pg.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT - 40))
        else:
            self.image = pg.image.load('data/platform2.png').convert_alpha()
            self.image = pg.transform.scale(self.image, (PLATFORM_WIDTH, PLATFORM_HEIGHT - 40))
        self.rect = self.image.get_rect(center=(x, y))
        self.shift = 0

class SmallPlatform(Platform):
    def __init__(self, x, y, color=PLATFORM_COLOR):
        pg.sprite.Sprite.__init__(self)
        Platform.__init__(self, x, y, color)
        self.image = pg.Surface((SMALLPLATFORM_WIDTH, SMALLPLATFORM_HEIGHT))
        if color == None:
            self.image = pg.Surface((SMALLPLATFORM_WIDTH, SMALLPLATFORM_HEIGHT))
        else:
            self.image = pg.image.load('data/platform3.png').convert_alpha()
            self.image = pg.transform.scale(self.image, (SMALLPLATFORM_WIDTH, SMALLPLATFORM_HEIGHT))
        self.rect = self.image.get_rect(center=(x, y))
        self.shift = 0


class Wall(Platform):
    def __init__(self, x, y, color=PLATFORM_COLOR):
        pg.sprite.Sprite.__init__(self)
        Platform.__init__(self, x, y, color)
        self.image = pg.Surface((WALL_WIDTH, WALL_HEIGHT), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.shift = 0


class Ground(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((SIZE.current_w, PLATFORM_HEIGHT))
        self.rect = self.image.get_rect(center=(SIZE.current_w // 2, SIZE.current_h // 1.07))

    def draw(self, a, b):
        pass