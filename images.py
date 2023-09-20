import pygame as pg
pg.init()
#background
bg_images = []
for i in range (1,5):
    bg_image = pg.transform.scale(pg.image.load(f"./assets/sprites/plx-{i}.png"), (1024,768))
    bg_images.append(bg_image)

frame_img = pg.transform.scale(pg.image.load(f"./assets/sprites/frame.png"), (64,64))
player_img =  pg.transform.scale(pg.image.load(f"./assets/sprites/player.png"), (32,32))

#vegetables
tomato_img = pg.transform.scale(pg.image.load(f"./assets/sprites/tomato.png"), (64,64))
strawberry_img = pg.transform.scale(pg.image.load(f"./assets/sprites/strawberry.png"), (64,64))
pear_img = pg.transform.scale(pg.image.load(f"./assets/sprites/pear.png"), (64,64))
blueberry_img = pg.transform.scale(pg.image.load(f"./assets/sprites/blueberry.png"), (64,64))
banana_img = pg.transform.scale(pg.image.load(f"./assets/sprites/banana.png"), (64,64))
orange_img = pg.transform.scale(pg.image.load(f"./assets/sprites/orange.png"), (64,64))
skull_img = pg.transform.scale(pg.image.load(f"./assets/sprites/skull.png"), (64,64))
powerup_img = pg.transform.scale(pg.image.load(f"./assets/sprites/powerup.png"), (64,64))

wood_img = pg.image.load(f"./assets/sprites/wood.png")
