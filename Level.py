from ENEMY import *
from PLAYER import *
from BACKGROUND import *
from PLATFORMS import *


def start(screen, music_play):
    if music_play:
        pg.mixer.music.load('data/musics/gurenge_8_bit.mp3')
        pg.mixer.music.play(-1, 0.0)
        pg.mixer.music.set_volume(0.4)
    background = Map(screen)
    GROUND = Ground()
    gplatforms = [
        ThinPlatform(SIZE.current_w // 1.23, SIZE.current_h // 1.7),  # 0
        Platform(SIZE.current_w * 1.2, SIZE.current_h // 1.35),  # 1
        ThinPlatform(SIZE.current_w * 1.5, SIZE.current_h // 1.35),  # 2
        Platform(SIZE.current_w * 1.5, SIZE.current_h // 1.07, None),  # 3
        Platform(SIZE.current_w * 2, SIZE.current_h // 1.7),  # 4
        ThinPlatform(SIZE.current_w * 2.65, SIZE.current_h // 1.7),  # 5
        Platform(SIZE.current_w * 2.8, SIZE.current_h // 1.7),  # 6
        Platform(SIZE.current_w * 3.2, SIZE.current_h // 1.5),  # 7
        SmallPlatform(SIZE.current_w * 3.55, SIZE.current_h // 1.2),  # 8
        Platform(SIZE.current_w * 3.75, SIZE.current_h // 1.07, None),  # 9
        ThinPlatform(SIZE.current_w * 2.7, SIZE.current_h // 3),  # 10
        ThinPlatform(SIZE.current_w * 3.2, SIZE.current_h // 2.8),  # 11
        Platform(SIZE.current_w * 2.2, SIZE.current_h // 3.1),  # 12
        ThinPlatform(SIZE.current_w * 1.7, SIZE.current_h // 3),  # 13
        Platform(SIZE.current_w * 3.65, SIZE.current_h // 3.4),  # 14
        Platform(SIZE.current_w * 2.2, SIZE.current_h // 1.07, None),  # 15
        Platform(SIZE.current_w * 2.8, SIZE.current_h // 1.07, None),  # 16
        Platform(SIZE.current_w * 1.2, SIZE.current_h // 3.15),  # 17
        Platform(SIZE.current_w * 0.75, SIZE.current_h // 3.4),  # 18
        SmallPlatform(SIZE.current_w * 0.615, SIZE.current_h // 8),  # 19*
        SmallPlatform(SIZE.current_w * 0.615, SIZE.current_h // 5),  # 20*
        Wall(0, SIZE.current_h // 2),
        Wall(SIZE.current_w * 4, SIZE.current_h // 2)
    ]
    enemies = [Enemy(*gplatforms[0].rect.midtop, 'normal1', screen),
               Enemy(*gplatforms[2].rect.midtop, 'normal1', screen),
               Enemy(*gplatforms[3].rect.midtop, 'normal2', screen),
               Enemy(*gplatforms[4].rect.midtop, 'normal1', screen),
               Enemy(*gplatforms[6].rect.midtop, 'normal2', screen),
               Enemy(*gplatforms[9].rect.midtop, 'normal2', screen),
               Enemy(*gplatforms[11].rect.midtop, 'normal2', screen),
               Enemy(*gplatforms[12].rect.midtop, 'normal1', screen),
               Enemy(*gplatforms[13].rect.midtop, 'normal2', screen),
               Enemy(*gplatforms[14].rect.midtop, 'normal1', screen),
               Enemy(*gplatforms[14].rect.midtop, 'normal1', screen),
               Enemy(*gplatforms[15].rect.midtop, 'normal1', screen),
               Enemy(*gplatforms[16].rect.midtop, 'normal2', screen),
               Enemy(*gplatforms[17].rect.midtop, 'normal2', screen),
               Enemy(*gplatforms[18].rect.midtop, 'normal1', screen),
               Enemy(*gplatforms[18].rect.midtop, 'normal2', screen)
        ]
    player = Player(screen)
    gorizontal_platforms = pg.sprite.Group(gplatforms)
    died_mas = []
    return background, gplatforms, gorizontal_platforms, player, enemies, GROUND, died_mas