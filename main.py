import pygame as pg
import sys
import os
from settings import *
from sprites import *
from images import *
from sounds import *

#1 = tomato, 2 = blueberry, 3 = banana, 4 = strawberries,  5 = orange, 6 = pear
tomatoes = pg.sprite.Group()
strawberries = pg.sprite.Group()
blueberries = pg.sprite.Group()
bananas = pg.sprite.Group()
oranges = pg.sprite.Group()
pears = pg.sprite.Group()
skulls = pg.sprite.Group()
powerups = pg.sprite.Group()

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(100, 100)

    def draw_bg(self):
        for i in bg_images:
            self.screen.blit(i,(0,0))

    def powerup(self):
        self.power = 1
        self.points_earned = self.points_earned * 2
        self.power_time = pg.time.get_ticks()

    def new(self):
        # initialize all variables and do all the setup for a new game

        print(self.high_score)
        self.diff = 0
        self.lasthit = 0
        self.combo_score = 0
        self.consecutive = 0
        self.power = 0
        self.combo = []
        self.points_earned = 50
        for x in range(6):
            self.combo.append(random.randrange(1,7))

        print(self.combo)
        self.all_sprites = pg.sprite.Group()
        self.score = 0
        self.player = Player(self, 512, 704)

        #Intitialize fruits/vegetables
        for i in range (10):
            p = powerup(self)
            powerups.add(p)
        for i in range (4):
            t = skull(self)
            skulls.add(t)
        for i in range (9):
            t = tomato(self)
            tomatoes.add(t)
        for i in range (9):
            s = strawberry(self)
            strawberries.add(s)  
        for i in range (9):
            b = blueberry(self)
            blueberries.add(b)
        for i in range (9):
            b = banana(self)
            bananas.add(b)
        for i in range (9):
            b = orange(self)
            oranges.add(b)
        for i in range (9):
            b = pear(self)
            pears.add(b)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self): 
        pg.quit()
        sys.exit()

    def update(self):

        # update portion of the game loop
        self.all_sprites.update()
        tomatohits = pg.sprite.spritecollide(self.player,tomatoes,True)
        strawberryhits = pg.sprite.spritecollide(self.player,strawberries,True)
        blueberryhits = pg.sprite.spritecollide(self.player,blueberries,True)
        bananahits = pg.sprite.spritecollide(self.player,bananas,True)
        orangehits = pg.sprite.spritecollide(self.player,oranges,True)
        pearhits = pg.sprite.spritecollide(self.player,pears,True)
        skullhits = pg.sprite.spritecollide(self.player,skulls,True)
        poweruphits = pg.sprite.spritecollide(self.player, powerups,True)

        if self.power == 1 and pg.time.get_ticks() - self.power_time > 5000:
            self.points_earned = 50
            self.power = 0

        if self.score > 50000 and self.diff == 0:
            for i in range(3):
                s = skull(self)
                skulls.add(s)
            self.diff = 1

        
        if self.score > 100000 and self.diff == 1:
            for i in range(5):
                s = skull(self)
                skulls.add(s)
            self.diff = 2

        if self.score > 500000 and self.diff == 1:
            for i in range(8):
                s = skull(self)
                skulls.add(s)
            self.diff = 2

        if skullhits:
            death_sound.play()
            self.playing = False
            if self.score > self.high_score:
                self.high_score = self.score
            with open('highscore.txt', 'w') as file:
                file.write(str(self.high_score))

        if poweruphits:
            pwr_sound.play()
            self.powerup()
            for hit in poweruphits:
                t = powerup(self)
                powerups.add(t)

        if tomatohits:
            munch_sound.play()
            self.lasthit = 1
            self.score += self.points_earned
            for hit in tomatohits:
                t = tomato(self)
                tomatoes.add(t)
            self.check_combo()

        if strawberryhits:
            munch_sound.play()
            self.lasthit = 4
            self.score += self.points_earned
            for hit in strawberryhits:
                s = strawberry(self)
                strawberries.add(s)
            self.check_combo()

        if blueberryhits:
            munch_sound.play()
            self.lasthit = 2
            self.score += self.points_earned
            for hit in blueberryhits:
                b = blueberry(self)
                blueberries.add(b)
            self.check_combo()
            
        if  bananahits:
            munch_sound.play()
            self.lasthit = 3
            self.score += self.points_earned
            for hit in bananahits:
                b = banana(self)
                bananas.add(b)
            self.check_combo()
        if  orangehits:
            munch_sound.play()
            self.lasthit = 5
            self.score += self.points_earned
            for hit in orangehits:
                b = orange(self)
                oranges.add(b)
            self.check_combo()
        if  pearhits:
            munch_sound.play()
            self.lasthit = 6
            self.score += self.points_earned
            for hit in pearhits:
                b = pear(self)
                pears.add(b)
            self.check_combo()

    def check_combo(self):
     
        if self.lasthit == self.combo[self.combo_score]:
            self.combo_score +=1
            if self.combo_score == 1:
                combo1_sound.set_volume(0.5)
                combo1_sound.play()
            if self.combo_score == 2:
                combo2_sound.set_volume(0.5)
                combo2_sound.play()
            if self.combo_score == 3:
                combo3_sound.set_volume(0.5)
                combo3_sound.play()
            if self.combo_score == 4:
                combo4_sound.set_volume(0.5)
                combo4_sound.play()
            if self.combo_score == 5:
                combo5_sound.set_volume(0.5)
                combo5_sound.play()
        else:
            if self.combo_score > 1:
                combo_sound.play()
                print(self.combo_score * self.points_earned *5)
                self.score += self.combo_score * self.points_earned *5
            self.combo_score = 0
            self.lasthit = 0
            self.consecutive = 0
            
        if self.combo_score == 6:
            self.consecutive += 1
            fullcombo_sound.play()
            self.score += pow(2,self.consecutive) * self.points_earned
            self.combo_score = 0
            self.lasthit = 0
            self.combo.clear()
            for x in range(6):
                self.combo.append(random.randrange(1,7))

    def draw(self):
        self.draw_bg()
        self.screen.blit(wood_img, (0, 60))
        self.draw_text(self.screen, "SCORE:",50,90,60,ORANGE)
        self.draw_text(self.screen,str(self.score),50,300,60, ORANGE)
        self.draw_text(self.screen,"FRUIT SALADS:",50,170,100, ORANGE)
        self.draw_text(self.screen,str(self.consecutive),50,350,100, ORANGE)
        self.draw_combo_list()
        if self.power == 1:
            self.draw_text(self.screen,"DOUBLE 5s:",50,120,180, GREEN)
            self.draw_text(self.screen, str((pg.time.get_ticks() - self.power_time )/ 1000), 50, 340, 180, GREEN)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def draw_text(self,surf, text,size,x, y, color):
        font_name = pg.font.Font('./assets/sprites/masaki.otf', size)
        text_surface = font_name.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
    
    def draw_combo_list(self):

        self.combo_imgs = [tomato_img, blueberry_img, banana_img, strawberry_img, orange_img, pear_img]
        counter = 0
        for i in self.combo:
            self.screen.blit(self.combo_imgs[i-1], (64*counter, 0))
            counter +=1
        self.screen.blit(frame_img, (64*self.combo_score, 0))

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.score > self.high_score:
                    self.high_score = self.score
                with open('highscore.txt', 'w') as file:
                    file.write(str(self.high_score))
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
        
    def show_start_screen(self):
        if os.path.exists('highscore.txt'):
            with open('highscore.txt', 'r') as file:
                self.high_score = int(file.read())
        else:
            self.high_score = 0

        self.draw_bg()
        self.draw_text(self.screen, "Fructus", 150, 500,250, ORANGE)
        self.draw_text(self.screen, "Press space to start.", 50, 500,500, ORANGE)
        self.draw_text(self.screen, "High Score:", 50, 420,600, YELLOW)
        self.draw_text(self.screen, str(self.high_score), 50, 660,600, YELLOW)
        self.screen.blit(orange_img, (700,300))
        self.screen.blit(banana_img, (200,300))
        pg.display.flip()
        self.wait_for_key()

    def show_end_screen(self):
        self.draw_bg()
        self.draw_text(self.screen, "Game Over",150, 500,300, ORANGE)
        self.draw_text(self.screen, "Press space to restart.", 50, 500,500, ORANGE)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        waiting = False

# create the game object

g = Game()
g.show_start_screen()
pg.mixer.music.load("./assets/sound/bg_music.wav")
pg.mixer.music.play(-1)
while True:
    g.new()
    g.run()
    g.show_end_screen()