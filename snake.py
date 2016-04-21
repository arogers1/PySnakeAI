import pygame
import random
import sys
from pygame.locals import *
from ai import AI

class SnakeGame(object):
    """ Snake Game adapted from site: http://pygame.org/project-Snake+in+35+lines-818-.html
        Requires pygame to work
    """

    def __init__(self, human_player=True):
        self.human_player = human_player
        self.surface_img_path = 'surface.png'
        self.xs = [290, 290, 290, 290, 290]
        self.ys = [290, 280, 270, 260, 250]
        self.dirs = 0
        self.score = 0
        self.applepos = (random.randint(20, 570), random.randint(20, 570))
        pygame.init()
        self.s = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Snake')
        self.appleimage = pygame.Surface((10, 10))
        self.appleimage.fill((0, 255, 0))
        self.walls = [pygame.Surface((590,10)),pygame.Surface((10,590)),pygame.Surface((590,10)),pygame.Surface((10,590))]
        self.wall_positions = [(0,0),(590,0),(0,590),(0,0)]
        for w in self.walls:
            w.fill((0,0,0))
        self.img = pygame.Surface((10, 10))
        self.img.fill((255, 0, 0))
        self.f = pygame.font.SysFont('Arial', 20)
        self.clock = pygame.time.Clock()


    def collide(self, x1, x2, y1, y2, w1, w2, h1, h2):
        if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
            return True
        else:
            return False


    def die(self, screen, score):
        self.f = pygame.font.SysFont('Arial', 30)
        t = self.f.render('Your score was: ' + str(score), True, (0, 0, 0))
        screen.blit(t, (10, 270))
        pygame.display.update()
        pygame.time.wait(2000)
        sys.exit(0)



    def get_input(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            elif e.type == KEYDOWN:
                if e.key == K_UP and self.dirs != 0:
                    self.dirs = 2
                elif e.key == K_DOWN and self.dirs != 2:
                    self.dirs = 0
                elif e.key == K_LEFT and self.dirs != 1:
                    self.dirs = 3
                elif e.key == K_RIGHT and self.dirs != 3:
                    self.dirs = 1


    def check_collision(self):
        i = len(self.xs) - 1
        while i >= 2:
            if self.collide(self.xs[0], self.xs[i], self.ys[0], self.ys[i], 10, 10, 10, 10):
                self.die(self.s, self.score)
            i -= 1
        if self.collide(self.xs[0], self.applepos[0], self.ys[0], self.applepos[1], 10, 10, 10, 10):
            self.score += 1
            self.xs.append(700)
            self.ys.append(700)
            self.applepos = (random.randint(20, 570), random.randint(20, 570))
        if self.xs[0] < 20 or self.xs[0] > 580 or self.ys[0] < 20 or self.ys[0] > 580:
            self.die(self.s, self.score)


    def move_snake(self):
        i = len(self.xs) - 1
        while i >= 1:
            self.xs[i] = self.xs[i - 1]
            self.ys[i] = self.ys[i - 1]
            i -= 1
        if self.dirs == 0:
            self.ys[0] += 10
        elif self.dirs == 1:
            self.xs[0] += 10
        elif self.dirs == 2:
            self.ys[0] -= 10
        elif self.dirs == 3:
            self.xs[0] -= 10


    def update_screen(self):
        self.s.fill((255, 255, 255))
        for i in range(0, len(self.xs)):
            self.s.blit(self.img, (self.xs[i], self.ys[i]))
        for i in range(len(self.walls)):
            self.s.blit(self.walls[i], self.wall_positions[i])
        self.s.blit(self.appleimage, self.applepos)
        t = self.f.render(str(self.score), True, (0, 0, 0))
        self.s.blit(t, (10, 10))
        pygame.display.update()
        pygame.image.save(self.s, self.surface_img_path)

    def next_step(self, ai=None):
        if self.human_player:
            self.clock.tick(10)
            self.get_input()
        else:
            self.get_input()            
            ai.get_input()
        self.check_collision()
        self.move_snake()
        self.update_screen()

    def run(self, ai=None):
        self.update_screen
        while True:
            self.next_step(ai)


if __name__ == "__main__":
    human = True
    if len(sys.argv) > 1:
        human = False
    sg = SnakeGame(human_player=human)
    if not human:
        ai = AI(sg)
        print ai
        sg.run(ai)
    else:
        sg.run()
