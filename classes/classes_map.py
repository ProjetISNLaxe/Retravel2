import pygame, quete, os
from classes.perso_classes import *
from menu.dialogue import dialogue
from mapimage import *
from battle.combatV3 import tourpartour


class classmapbasique():
    def __init__(self, nom):
        listefi = os.listdir("map/" + nom)
        self.image = map[nom]
        self.image_obstacle = map[nom+"_obstacle"]
        self.mask = pygame.mask.from_surface(self.image_obstacle)
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        rectf = open("save1/posmap/posmap" + nom, "r")
        carect = rectf.read()
        rectf.close()
        lirect = carect.split(",")
        if carect == "":
            rectf = open("map/" + nom + "/spawn" + nom, "r")
            carect = rectf.read().split(";")
            rectf.close()
            lirect = carect[0].split(",")


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
        if ("pnj"+nom) in listefi:
            self.pnj = True
        else: self.pnj = False
        if self.pnj :
            pnji = open("map/" + nom + "/pnj" + nom, "r")
            pnj = pnji.read()
            pnji.close()
            self.pnjli = pnj.split(",")
            self.imagepnj = []
            self.maskpnj = []
            for i in range(len(self.pnjli)):
                self.imagepnj.append(
                    pygame.image.load("map/" + nom + "/" + nom + "_" + self.pnjli[i] + ".png"))
                self.maskpnj.append(pygame.mask.from_surface(self.imagepnj[i]))
        self.myfont = pygame.font.SysFont("monospace", 20)

        if ("mob"+nom) in  listefi:
            self.mob=True
        else : self.mob = False
        if self.mob:
            mobi = open("map/"+nom+"/mob"+nom, "r")
            mob = mobi.read()
            mobi.close()
            self.mobli = mob.split(",")
            self.imagemob = []
            self.maskmob = []

            for i in range(len(self.mobli)):
                self.imagemob.append(pygame.image.load("map/"+nom+"/"+nom+"_" + self.mobli[i] + ".png"))
                self.maskmob.append(pygame.mask.from_surface(self.imagemob[i]))
    def interaction(self, perso, fenetre):
        tkey = pygame.key.get_pressed()
        for i in range(len(self.transili)):
            if self.masktransi[i].overlap(perso.mask, (perso.rect.x - self.rect.x, perso.rect.y - self.rect.y)):
                self.affichetext = True
                break
            else:
                self.affichetext = False
        if self.pnj:
            for i in range(len(self.pnjli)):
                if tkey[K_f]:
                    if self.maskpnj[i].overlap(perso.mask, (perso.rect.x - self.rect.x, perso.rect.y - self.rect.y)):
                        quete.quetes(fenetre)  # vérifie si il fait partie d'une quête
                        dialogue(fenetre, self.pnjli[i])  # lance dialogue pnj
        if self.mob:
            for i in range (len(self.mobli)):
                if tkey[K_f]:
                    if self.maskmob[i].overlap(perso.mask, (perso.rect.x - self.rect.x, perso.rect.y- self.rect.y)):
                        fichier = open("menu/quetes/mobmort", "w")
                        fichier.write(self.mobli[i])
                        fichier.close()
                        tourpartour()
    def affichage(self, fenetre, perso):
        fenetre.blit(self.image, self.rect)
        if self.pnj:
            for i in range(len(self.pnjli)):
                fenetre.blit(self.imagepnj[i], self.rect)
        if self.mob:
            for i in range (len(self.mobli)):
                fenetre.blit(self.imagemob[i], self.rect)
        fenetre.blit(perso.imageperso, perso.rect)
        if self.affichetext:
            fenetre.blit(self.myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))



