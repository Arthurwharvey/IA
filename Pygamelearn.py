import pygame
from random import randint
import time 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
boundary = pygame.Rect(0, 100, 800, 500)

WHITE = (0, 0, 0)
BLACK = (86, 179, 20)
playerleft = True
playerdown = True
playerright = True
playerup = True
enemyleft = True
enemydown = True
enemyright = True
enemyup = True
playerturn = True 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def drawGrid():
    blockSize = 50
    for x in range(0, SCREEN_WIDTH, blockSize):
        for y in range(0, SCREEN_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

move_dist = 50
movenum = 5
enemymovenum = 10
turnnum = 0


player = pygame.Rect(500, 250, 50, 50)
gui = pygame.Rect(0, 600, 800, 200)
topgui = pygame.Rect(0, 0, 800, 100)
movegui = pygame.Rect(50, 650, 200, 100)
attackgui = pygame.Rect(300, 650, 200, 100)
endturngui = pygame.Rect(550, 650, 200, 100)
font = pygame.font.Font('freesansbold.ttf', 32)
movetext = font.render('Move:', True, (0,0,0))
movenumdisplay = font.render(str(movenum), True, (255,0,0))
attacktext = font.render('Attack', True, (0,0,0))
endturntext = font.render('End Turn', True, (0,0,0))
turntext = font.render('Turn:', True, (255,255,255))
turnnumdisplay = font.render(str(turnnum), True, (255,0,0))
uwintext = font.render('You Win!', True, (0,0,0))



enemy = pygame.Rect(50 * randint(0, 15), 50 * randint(0, 11), 50, 50)

def enemyMove():
    global enemymovenum
    direction = randint(1, 4)
    if direction == 1 and enemyleft:
        enemy.move_ip(-50, 0)
        enemymovenum -= 1
    if direction == 2 and enemyright:
        enemy.move_ip(50, 0)
        enemymovenum -= 1
    if direction == 3 and enemyup:
        enemy.move_ip(0, -50)
        enemymovenum -= 1
    if direction == 4 and enemydown:
        enemy.move_ip(0, 50)
        enemymovenum -= 1
    time.sleep(0.1)
    
def playerCollide():
    global playerleft 
    global playerdown 
    global playerright 
    global playerup 
    player.move_ip(-move_dist, 0)
    if player.collidelist(stones)!= -1:
        playerleft = False
    else:
        playerleft = True
    player.move_ip(move_dist, 0)

    player.move_ip(move_dist, 0)
    if player.collidelist(stones)!= -1:
        playerdown = False
    else:
        playerdown = True
    player.move_ip(-move_dist, 0)

    player.move_ip(0, -move_dist)
    if player.collidelist(stones)!= -1:
        playerup = False
    else:
        playerup = True
    player.move_ip(0, move_dist)

    player.move_ip(0, move_dist)
    if player.collidelist(stones)!= -1:
        playerright = False
    else:
        playerright = True
    player.move_ip(0, -move_dist)

def enemyCollide():
    global enemyleft 
    global enemydown 
    global enemyright 
    global enemyup 
    
    enemy.move_ip(-move_dist, 0)
    if enemy.collidelist(stones)!= -1:
        enemyleft = False
    else:
        enemyleft = True
    enemy.move_ip(move_dist, 0)

    enemy.move_ip(move_dist, 0)
    if enemy.collidelist(stones)!= -1:
        enemyright = False
    else:
        enemyright = True
    enemy.move_ip(-move_dist, 0)

    enemy.move_ip(0, -move_dist)
    if enemy.collidelist(stones)!= -1:
        enemyup = False
    else:
        enemyup = True
    enemy.move_ip(0, move_dist)

    enemy.move_ip(0, move_dist)
    if enemy.collidelist(stones)!= -1:
        enemydown = False
    else:
        enemydown = True
    enemy.move_ip(0, -move_dist)

stones = []
for _ in range(randint(30,50)):
    x = 50 * randint(0, 15)
    y = 50 * randint(0, 11)
    stones.append(pygame.Rect(x, y, 50, 50))

run = True

while run:
    movenumdisplay = font.render(str(movenum), True, (255,0,0))
    turnnumdisplay = font.render(str(turnnum), True, (255,0,0))
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(BLACK)
    playerCollide()
    enemyCollide()

    for stone in stones:
        pygame.draw.rect(screen, (159, 161, 159), stone)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if playerturn:  
    
            if event.type == pygame.KEYDOWN:
                if movenum > 0:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if playerleft:
                            player.move_ip(-move_dist, 0)
                            movenum -= 1
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if playerdown:
                            player.move_ip(move_dist, 0)
                            movenum -= 1
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if playerup:
                            player.move_ip(0, -move_dist)
                            movenum -= 1
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if playerright:
                            player.move_ip(0, move_dist)
                            movenum -= 1
            if event.type == pygame.MOUSEBUTTONDOWN and endturngui.collidepoint(event.pos):
                if event.button == 1:
                    playerturn = False
    if not playerturn:
        
        if enemymovenum > 0:
            enemyMove()
        else:
            playerturn = True
            movenum = 5
            enemymovenum = 10
            turnnum += 1
    if player.colliderect(enemy):
        screen.blit(uwintext, (400,400))
    
        

    player.clamp_ip(boundary)
    enemy.clamp_ip(boundary)

    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.draw.rect(screen, (0, 255, 0), player)
    drawGrid()
    pygame.draw.rect(screen, (0, 0, 0), topgui)
    pygame.draw.rect(screen, (0, 0, 0), gui)
    pygame.draw.rect(screen, (159, 161, 159), movegui)
    pygame.draw.rect(screen, (159, 161, 159), attackgui)
    pygame.draw.rect(screen, (159, 161, 159), endturngui)
    if endturngui.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (200, 200, 200), endturngui)

    if movegui.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (200, 200, 200), movegui)

    if attackgui.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (200, 200, 200), attackgui)
    screen.blit(movetext, (75,685))
    screen.blit(movenumdisplay, (195,689))
    screen.blit(attacktext, (350,685))
    screen.blit(endturntext, (580,685))
    screen.blit(turntext, (25,35))
    screen.blit(turnnumdisplay, (125,35))
    
    
    

    pygame.display.update()

pygame.quit()