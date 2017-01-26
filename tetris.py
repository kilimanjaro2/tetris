#! /usr/bin/env python
#Arun H Garimella
#201564134
from block import O
from block import I
from block import S
from block import Z
from block import L
from block import J
from block import T
from block import X
from block import M
import sys
from random import choice
import pygame
from pygame.locals import *
CURRENT_SCORE = "Your Current Score Is "
SCORE = 0
SCORE_TEXT = "Your Score is "
GREAT_JOB = "Great Job! "
NOT_SO_GOOD = "Not So Good. "
mn = 1
cle = 0
class blockOther():
    def draw(self,grid, pos=None):
        if not pos: # 6x5
            screen.fill((135,220,120))
            for i, occupied in abc.checke(grid):
                if occupied:
                    c = eval(grid[i]+".color")
                    screen.fill(c, (i%30*16, i/30*16, 16, 16))
            
        else: # all
            s = pos - 3 - 60 # upper left position
            for p in xrange(0, 5):
                q = s + p * 30
                for i in xrange(q, q+6):
                    if -1 < i < 960:
                        c = eval(grid[i]+".color") if grid[i] else (135,220,120)
                        screen.fill(c, (i%30*16, i/30*16, 16, 16))
        pygame.display.flip()

class gamePlay():
    def updateScore(self, mm , val):
        if val == 1:
            #print mm + 10
            return mm + 10
        else: 
            #print mm + 100
            return mm + 100       

    def selectPiece(self):
        if cle < 2:
            return choice([O, I, S, Z, L, J, T])()
        elif cle < 5 :    
            return choice([X, O, I, S, Z, L, J, T])()   
        else:    
            return choice([M, X, O, I, S, Z, L, J, T])()   

    def updateSpeed(self, ij):    
        return speed-100
          
    def paused(self):

        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        while pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            button("Continue",150,450,100,50,green,bright_green,unpause)
            button("Quit",550,450,100,50,red,bright_red,quitgame)

            pygame.display.update()
            clock.tick(15)                     
class absoluteChecker():
    
    def merge(self,grid1, grid2):
        grid = grid1[:]
        for i,c in abc.checke(grid2):
            if c:
                grid[i] = c
        return grid

    def complete(self,grid):
        n = 0
        i = 30
        #for i in range(0, 960, 30):
        while i < 931:   
            if not None in grid[i:i+30]:
                grid = 30*[None] + grid[:i] + grid[i+30:]
                n += 1
            i +=30    
        return grid, n

    def max_pos(self,grid, block, pos):
        while not False:
            grid_block = block.grid(pos+30)
            if grid_block and find(grid, grid_block, pos+30):
                pos += 30
            else:
                return pos

    def checke(self,sequence, start=0):
        n = start
        for elem in sequence:
            yield n, elem
            n += 1   
def find(grid1, grid2, pos): # 4x4
    s = pos - 32 # upper left position
    p = 0
    #for p in xrange(0, 4):
    while p < 4:
        q = s + p * 30
        i = q
    #for i in range(q, q+4):
        while i < q + 4:
            try:
                if grid1[i] and grid2[i]:    
                    return 0
            except:
                pass
            i+=1
        p+=1        
    return 1
                 

pygame.init()
pygame.event.set_blocked(None)
pygame.event.set_allowed((KEYDOWN, QUIT))
pygame.key.set_repeat(75, 0)
pygame.display.set_caption('Arun 201564134 Tetris')
screen = pygame.display.set_mode((480,512))
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 15)
zx=1
while zx==1: # start(restart) game
    lol = gamePlay()
    oth = blockOther()
    abc=absoluteChecker()
    grid = [None] * 960
    speed = 1000
    screen.fill((135,220,120))
    while True: # spawn a block
        SCORE = lol.updateScore(SCORE,1)
        block = lol.selectPiece()
        pos = 15
        if not find(grid, block.grid(pos), pos):
            if(SCORE > 910):
                print GREAT_JOB
            else:
                print NOT_SO_GOOD
            print SCORE_TEXT , SCORE 
            zx=2
            break # you lose
        pygame.time.set_timer(KEYDOWN, speed)
        while True: # move the block
            #
            oth.draw(abc.merge(grid, block.grid(pos)), pos)
            event = pygame.event.wait()
            if event.type == QUIT: sys.exit()
            try:
                aim = {
                    K_UNKNOWN: 30+pos,
                    K_s: pos,
                    K_DOWN: pos+30,
                    K_a: pos-1 ,
                    K_d: pos+1,
                    K_SPACE: None,
                    K_p: None,
                }[event.key]
            except KeyError:
                continue
            qq = event.key  
            if qq == K_p:
                    pause = True
                    lol.paused()
            if zx == 1 and qq == K_s:
                block.rotate()
            if zx == 1 and qq in (K_a, K_d) and pos / 30 != aim / 30:
                continue
            if zx == 1 and qq == K_SPACE:
                pos_old = pos
                pos = abc.max_pos(grid, block, pos)
                #
                oth.draw(grid, pos_old)
                oth.draw(abc.merge(grid, block.grid(pos)), pos)
                break
            if zx == 1:
                grid_aim = block.grid(aim)
            if grid_aim and find(grid, grid_aim, aim):
                pos = aim
            else:
                if qq == K_s:
                    block.rotate(times=7)
                elif not qq in (K_a, K_d):
                    break            
        grid = abc.merge(grid, block.grid(pos))
        grid, n = abc.complete(grid)
        print CURRENT_SCORE, SCORE
        if n:
            cle += 1
            SCORE += 100
            #CORE = lol.updateScore(SCORE,2)
            mn = 2
            #
            oth.draw(grid)
            speed = lol.updateSpeed(speed)
            #speed -= 250 * n #5*n
            if speed <= 199: speed = 200
