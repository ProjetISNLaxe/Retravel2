import pygame
from perso_classes import *
import quete
from dialogue import dialogue


class classmapbasique():
    def __init__(self, nom):
        self.image = pygame.image.load("map/" + nom + "/" + nom + ".png").convert_alpha()
        self.image_obstacle = pygame.image.load("map/" + nom + "/" + nom + "_obstacle.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image_obstacle)
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        rectf = open("save1/posmap/posmap" + nom, "r")
        carect = rectf.read()
        rectf.close()
        if carect == "":
            rectf = open("map/" + nom + "/spawn" + nom, "r")
            carect = rectf.read()
            rectf.close()
        lirect = carect.split(",")
        self.rect.x = int(lirect[0])
        self.rect.y = int(lirect[1])
        transi = open("map/" + nom + "/transi" + nom, "r")
        transition = transi.read()
        transi.close()
        self.transili = transition.split(",")
        self.imagetransi = []
        self.masktransi = []
        for i in range(len(self.transili)):
            self.imagetransi.append(
                pygame.image.load("map/" + nom + "/" + nom + "_" + self.transili[i] + ".png"))
            self.masktransi.append(pygame.mask.from_surface(self.imagetransi[i]))
        self.affichetext = False
        pnji = open("map/" + nom + "/pnj" + nom, "r")
        pnj = pnji.read()
        pnji.close()
        self.pnjli = pnj.split(",")
        self.imagepnj = []
        self.maskpnj = []
        if self.pnjli[0] != "":
            for i in range(len(self.pnjli)):
                self.imagepnj.append(
                    pygame.image.load("map/" + nom + "/" + nom + "_" + self.pnjli[i] + ".png"))
                self.maskpnj.append(pygame.mask.from_surface(self.imagepnj[i]))
        self.myfont = pygame.font.SysFont("monospace", 20)

    def interaction(self, perso, fenetre):
        tkey = pygame.key.get_pressed()
        for i in range(len(self.transili)):
            if self.masktransi[i].overlap(perso.mask, (perso.rect.x - self.rect.x, perso.rect.y - self.rect.y)):
                self.affichetext = True
                break
            else:
                self.affichetext = False
        if self.pnjli[0] != "":
            for i in range(len(self.pnjli)):
                if tkey[K_f]:
                    if self.maskpnj[i].overlap(perso.mask, (perso.rect.x - self.rect.x, perso.rect.y - self.rect.y)):
                        quete.quetes(fenetre)  # vérifie si il fait partie d'une quête
                        dialogue(fenetre, self.pnjli[i])  # lance dialogue pnj

    def affichage(self, fenetre, perso):
        fenetre.blit(self.image, self.rect)
        if self.pnjli[0] != "":
            for i in range(len(self.pnjli)):
                fenetre.blit(self.imagepnj[i], self.rect)
        fenetre.blit(perso.imageperso, perso.rect)
        if self.affichetext:
            fenetre.blit(self.myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))



