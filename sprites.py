import pygame as pg
from settings import *
import time
from images import *
import random

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = player_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.powerup = 0
        self.speed = 500
        self.last_pressed = 0

    def get_keys(self):
        self.vx, self.vy = 0,0
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vx = -self.speed
        if keys[pg.K_d]:
            self.vx = self.speed


    def update(self):
        self.get_keys()
        if self.x + (self.vx * self.game.dt) > 0 and self.x + (self.vx * self.game.dt) < 992:
            self.x += self.vx * self.game.dt
            self.rect.topleft = (self.x, self.y)

class powerup(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = powerup_img
        self.rect = self.image.get_rect()
        self.x = random.randrange(32, WIDTH - 32)
        self.y = random.randrange(-5000,-32)
        self.speed = 5

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > HEIGHT:
            self.y = self.y = random.randrange(-20000,-10000)


class skull(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = skull_img
        self.rect = self.image.get_rect()
        self.x = random.randrange(32, WIDTH - 32)
        self.y = random.randrange(-5000,-32)
        self.speed = 10

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > HEIGHT:
            self.y = self.y = random.randrange(-5000,-500)


class tomato(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = tomato_img
        self.rect = self.image.get_rect()
        self.x = random.randrange(32, WIDTH - 32)
        self.y = random.randrange(-5000,-32)
        self.speed = 7

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > HEIGHT:
            self.y = self.y = random.randrange(-5000,-500)

class strawberry(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = strawberry_img
        self.rect = self.image.get_rect()
        self.x = random.randrange(32, WIDTH - 32)
        self.y = random.randrange(-5000,-32)
        self.speed = 7

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > HEIGHT:
            self.y = self.y = random.randrange(-5000,-500)

class blueberry(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = blueberry_img
        self.rect = self.image.get_rect()
        self.x = random.randrange(32, WIDTH - 32)
        self.y = random.randrange(-5000,-32)
        self.speed = 7

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > HEIGHT:
            self.y = self.y = random.randrange(-5000,-500)

class banana(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = banana_img
        self.rect = self.image.get_rect()
        self.x = random.randrange(32, WIDTH - 32)
        self.y = random.randrange(-5000,-32)
        self.speed = 7

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > HEIGHT:
            self.y = self.y = random.randrange(-5000,-500)

class orange(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = orange_img
        self.rect = self.image.get_rect()
        self.x = random.randrange(32, WIDTH - 32)
        self.y = random.randrange(-5000,-32)
        self.speed = 7

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > HEIGHT:
            self.y = self.y = random.randrange(-5000,-500)

class pear(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pear_img
        self.rect = self.image.get_rect()
        self.x = random.randrange(32, WIDTH - 32)
        self.y = random.randrange(-5000,-32)
        self.speed = 7

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > HEIGHT:
            self.y = self.y = random.randrange(-5000,-500)







        


