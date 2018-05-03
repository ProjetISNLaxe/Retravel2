import pygame
from pygame.locals import *
import random, closemenu

class SpaceInvaders:
    def __init__(self, fenetre):
        pygame.mixer.music.load("son/Sound/spaceinvaders.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        self.score = 0
        self.lives = 10
        pygame.font.init()
        self.font = pygame.font.Font("minijeu/spaceinvaders/space_invaders.ttf", 15)
        barrierDesign = [[],[0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
                         [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                         [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                         [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                         [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
                         [1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
                         [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1],
                         [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1],
                         [1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1]]
        self.fenetre= fenetre
        self.enemieSprites = {
                0:[pygame.image.load("minijeu/spaceinvaders/a1_0.png").convert(), pygame.image.load("minijeu/spaceinvaders/a1_1.png").convert()],
                1:[pygame.image.load("minijeu/spaceinvaders/a2_0.png").convert(), pygame.image.load("minijeu/spaceinvaders/a2_1.png").convert()],
                2:[pygame.image.load("minijeu/spaceinvaders/a3_0.png").convert(), pygame.image.load("minijeu/spaceinvaders/a3_1.png").convert()],
                }
        self.joueur = pygame.image.load("minijeu/spaceinvaders/shooter.png").convert()
        self.animationOn = 0
        self.direction = 1
        self.enemieSpeed = 20
        self.lastEnemyMove = 0
        self.joueurX = 400
        self.joueurY = 550
        self.shoot = None
        self.shoots = []
        self.enemies = []
        self.barrierParticules = []
        startY = 50
        startX = 50
        for rows in range(6):
            out = []
            if rows < 2:
                enemie = 0
            elif rows < 4:
                enemie = 1
            else:
                enemie = 2
            for columns in range(10):
                out.append((enemie,pygame.Rect(startX * columns, startY * rows, 35, 35)))
            self.enemies.append(out)
        self.chance = 990

        barrierX = 50
        barrierY = 400
        space = 100

        for offset in range(1, 5):
            for b in barrierDesign:
                for b in b:
                    if b != 0:
                        self.barrierParticules.append(pygame.Rect(barrierX + space * offset, barrierY, 5,5))
                    barrierX += 5
                barrierX = 50 * offset
                barrierY += 3
            barrierY = 400

    def enemieUpdate(self):
        if not self.lastEnemyMove:
            for enemie in self.enemies:
                for enemie in enemie:
                    enemie = enemie[1]
                    if enemie.colliderect(pygame.Rect(self.joueurX, self.joueurY, self.joueur.get_width(), self.joueur.get_height())):
                        self.lives -= 1
                        self.resetPlayer()
                    enemie.x += self.enemieSpeed * self.direction
                    self.lastEnemyMove = 25
                    if enemie.x >= 750 or enemie.x <= 0:
                        self.moveEnemiesDown()
                        self.direction *= -1
                    
                    chance = random.randint(0, 1000)
                    if chance > self.chance:
                        self.shoots.append(pygame.Rect(enemie.x, enemie.y, 5, 10))
                        self.score += 5
            if self.animationOn:
                self.animationOn -= 1                                                                                                                                                        
            else:
                self.animationOn += 1
        else:
            self.lastEnemyMove -= 1
    
        
    def moveEnemiesDown(self):
        for enemie in self.enemies:
            for enemie in enemie:
                enemie = enemie[1]
                enemie.y += 20

    def joueurUpdate(self):
        key = pygame.key.get_pressed()
        if key[K_RIGHT] and self.joueurX < 800 - self.joueur.get_width():
            self.joueurX += 5
        elif key[K_LEFT] and self.joueurX > 0:
            self.joueurX -= 5
        if key[K_SPACE] and not self.shoot:
            self.shoot = pygame.Rect(self.joueurX + self.joueur.get_width() / 2- 2, self.joueurY - 15, 5, 10)

    def shootUpdate(self):
        for i, enemie in enumerate(self.enemies):
            for j, enemie in enumerate(enemie):
                enemie = enemie[1]
                if self.shoot and enemie.colliderect(self.shoot):
                    self.enemies[i].pop(j)
                    self.shoot = None
                    self.chance -= 1
                    self.score += 100

        if self.shoot:
            self.shoot.y -= 20
            if self.shoot.y < 0:
                self.shoot = None


        for x in self.shoots:
            x.y += 20
            if x.y > 600:
                self.shoots.remove(x)
            if x.colliderect(pygame.Rect(self.joueurX, self.joueurY, self.joueur.get_width(), self.joueur.get_height())):
                self.lives -= 1
                self.shoots.remove(x)
                self.resetPlayer()

        for b in self.barrierParticules:
            check = b.collidelist(self.shoots)
            if check != -1:
                self.barrierParticules.remove(b)
                self.shoots.pop(check)
                self.score += 10
            elif self.shoot and b.colliderect(self.shoot):
                self.barrierParticules.remove(b)
                self.shoot = None
                self.score += 10
    def resetPlayer(self):
        self.joueurX = 400

    def run(self):
        clock = pygame.time.Clock()
        for x in range(3):
            self.moveEnemiesDown()
        while True:
            
            clock.tick(60)
            self.fenetre.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    closemenu.closemenu(self.fenetre)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            for enemie in self.enemies:
                for enemie in enemie:
                    self.fenetre.blit(pygame.transform.scale(self.enemieSprites[enemie[0]][self.animationOn], (35,35)), (enemie[1].x, enemie[1].y))
            self.fenetre.blit(self.joueur, (self.joueurX, self.joueurY))
            if self.shoot:
                pygame.draw.rect(self.fenetre, (52, 255, 0), self.shoot)
            for shoot in self.shoots:
                pygame.draw.rect(self.fenetre, (255,255,255), shoot)
            for b in self.barrierParticules:
                pygame.draw.rect(self.fenetre, (52, 255, 0), b)
            if self.enemies == [[], [], [], [], [], []]:
                self.fenetre.blit(pygame.font.Font("minijeu/spaceinvaders/space_invaders.ttf", 100).render("Gagne !", -1, (52,255,0)), (100, 200))
            elif self.lives > 0:
                self.shootUpdate()
                self.enemieUpdate()
                self.joueurUpdate()
            elif self.lives == 0:
                self.fenetre.blit(pygame.font.Font("minijeu/spaceinvaders/space_invaders.ttf", 100).render("You Lose!", -1, (52,255,0)), (100, 200))
            self.fenetre.blit(self.font.render("Lives: " + str(self.lives), True, (255,255,255)), (20, 10))
            self.fenetre.blit(self.font.render("Score: " + str(self.score), True, (255,255,255)), (400, 10))
            pygame.display.flip()

