﻿import pygame
from pygame.locals import *
from random import *
import time
from classes.classes_tpt import *
from battle.save import *
import menu.closemenu

pygame.init()

fenetre = pygame.display.set_mode((800, 600))

def attaqued(d,nomennemie):
    if nomennemie == "loup":
        loup.vie -= (d)
        if loup.vie <= 0:
            loup.vie = 150
            perso_joueur.xp += 50
            david.xp+=50
            if sinatra.active:
                sinatra.xp+=50
            savetpt()
            combat.etat = "victoire"
    if nomennemie == "soldat":
        if soldatpt.vie <= 0:
            soldatpt.vie = 300
            perso_joueur.xp += 50
            david.xp += 50
            if sinatra.active:
                sinatra.xp += 50
            savetpt()
            combat.etat = "victoire"
    if nomennemie == "malarich":
        malarich.vie -= d
        if malarich.vie <= 0:
            perso_joueur.xp += 150
            david.xp += 150
            sinatra.xp += 150
            savetpt()
            combat.etat = "victoire"
    if nomennemie == "avalogne":
        avalogne.vie -= d
        if avalogne.vie <= 0:
            avalogne.vie = 200
            perso_joueur.xp += 50
            david.xp += 50
            if sinatra.active:
                sinatra.xp += 50
            savetpt()
            combat.etat = "victoire"
    if nomennemie == "voleur":
        voleur.vie -= d
        if voleur.vie <= 0:
            voleur.vie = 120
            voleur.poison = 0
            perso_joueur.xp += 50
            david.xp += 50
            savetpt()
            combat.etat = "victoire"
    if nomennemie == "hornet":
        hornet.vie -= d
        if hornet.vie <= 0:
            hornet.vie = 200
            perso_joueur.xp += 50
            david.xp += 50
            if sinatra.active:
                sinatra.xp += 50
            savetpt()
            combat.etat = "victoire"
    if nomennemie == "goddess":
        goddess.vie -= d
        if goddess.vie <= 0:
            perso_joueur.xp += 2000
            david.xp += 2000
            sinatra.xp += 2000
            savetpt()
            combat.etat = "victoire"



def menubase(choix, c):
    if choix == 1 and c:
        attaque.menu_ = 1
        base.menu_ = 0
        c = False
    elif choix == 2 and c:
        objet.menu_ = 1
        base.menu_ = 0
        c = False
        choix = 1
    elif choix == 3 and c:
        combat.etat = "fuite"
    return choix, c


def menuobjet(choix, a, c):
    if choix == 4 and c:
        c = False
        base.menu_ = 1
        objet.menu_ = 0
        choix=1

    if choix == 3 and c:
        if combat.tour == 1:
            mana.quantite -= 1
            c = False
            base.menu_ = 1
            objet.menu_ = 0
            a = 1
            combat.anim = 6

        else:
            c = False
            base.menu_ = 1
            objet.menu_ = 0
            attaque.menu_ = 0
    elif choix == 2 and soin.quantite > 0 and a == 0 and c:
        if david.ingame:
            david.vie += 50
            if david.viemax<david.vie:
                david.vie=david.viemax
        elif perso_joueur.ingame:
            perso_joueur.vie += 50
            if perso_joueur.viemax<perso_joueur.vie:
                perso_joueur.vie=perso_joueur.viemax
        elif sinatra.ingame:
            sinatra.vie += 50
            if sinatra.viemax<sinatra.vie:
                sinatra.vie=sinatra.viemax
        soin.quantite -= 1
        c = False
        base.menu_ = 1
        objet.menu_ = 0
        a = 1
        combat.anim = 7
    elif choix == 2 and soin.quantite == 0 and a == 0 and c:
        c = False
    elif choix == 1 and resurection.quantite > 0 and a == 0 and c:
        if david.ingame:
            if sinatra.active and sinatra.vie == 0:
                sinatra.vie = 50
                sinatra.alive = True
            if perso_joueur.vie == 0:
                perso_joueur.vie = 75
                perso_joueur.alive = True
        elif perso_joueur.ingame:
            if sinatra.active and sinatra.vie == 0:
                sinatra.vie = 50
                sinatra.alive = True
            if david.vie == 0:
                david.vie = 100
                david.alive = True
        elif sinatra.ingame:
            if david.vie == 0:
                david.vie = 100
                david.alive = True
            if perso_joueur.vie == 0:
                perso_joueur.vie = 75
                perso_joueur.alive = True

        resurection.quantite -= 1
        c = False
        base.menu_ = 1
        objet.menu_ = 0
        a = 1
        combat.anim = 8
    elif choix == 2 and resurection.quantite == 0 and a == 0 and c:
        c = False
    return choix, a, c


def tourpartour(): # fonction principale avec variables
    fichier = open("menu/quetes/mobmort", "r")
    nomennemie = fichier.read()
    fichier.close()
    if nomennemie=="":
        return

    chargementsauvegarde()
    action = ["attaque", "objet", "fuite", ""]
    perso_joueur.ingame = True

    armure = "cuir"

    choix = 1  # le choix de l'action
    c = False  # la validation du choix
    d = 0

    a = 0  # une variable de validation de fin de combat.tour

    combat.tour = 1  # combat.tour=1=combat.tourperso   combat.tour=0=combat.tourennemi combat.tourperso2=combat.tour=2 etc

    pygame.key.set_repeat(200, 200)
    clock = pygame.time.Clock()
    if armure == "cuir":
        perso_joueur.armure = 2
    if armure == "chevalier":
        perso_joueur.armure = 8
    if armure == "r":
        perso_joueur.armure = 0
    if armure == "magique":
        perso_joueur.armure = 7
        perso_joueur.bonusmagique = 10

    base.menu_ = 1
    sinatra.active = False
    perso_joueur.sortdefeu = False
    combat.etat="combatencour"

    while combat.etat == "combatencour":  # la boucle principal
        for event in pygame.event.get():
            if event.type == QUIT:  # pour pouvoir quitter le jeux
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:  # les deplacements
                if event.key == K_DOWN:
                    choix += 1
                    if choix == 5:
                        choix = 1
                    if choix == 4 and (base.menu_ == 1 or objet.menu_ == 1 and not perso_joueur.ingame):
                        choix = 1
                if event.key == K_UP:
                    choix -= 1
                    if choix == 0:
                        if attaque.menu_ == 0:
                            choix = 3
                        else:
                            choix = 4
                if event.key == K_SPACE:
                    c = True

        if combat.tour == 1:
            perso_joueur.ingame = True
            david.ingame = False
            sinatra.ingame = False
            if c:
                if choix == 4 and attaque.menu_ == 1 and c:
                    attaque.menu_ = 0
                    base.menu_ = 1
                    choix = 1
                    c = False
                if choix == 1 and attaque.menu_ == 1 and c:
                    d = randint(1, 5) + 10+(perso_joueur.ptforce*2)
                    a = 1
                    c = False
                    attaque.menu_ = 0
                    base.menu_ = 1
                if choix == 3 and attaque.menu_ == 1 and c:
                    if perso_joueur.sortdefeu == True and perso_joueur.mana > 14:
                        d = 15 + perso_joueur.bonusmagique+(perso_joueur.ptforce*1)
                        perso_joueur.mana -= 15
                        a = 1
                        c = False
                        choix = 1
                        attaque.menu_ = 0
                        base.menu_ = 1
                        combat.anim = 1
                    elif perso_joueur.sortdefeu == True and perso_joueur.mana < 15:
                        c = False
                        choix = 1
                        attaque.menu_ = 0
                        base.menu_ = 1
                        a = 1
                        combat.anim = 2
                        perso_joueur.mana = 0
                    else:
                        c = False
                        choix = 1
                        attaque.menu_ = 0
                        base.menu_ = 1
                        a = 1
                        combat.anim = 2
                        perso_joueur.mana -= 15

                if choix == 2 and attaque.menu_ == 1 and c and perso_joueur.fleche > 0:
                    d = 13+(perso_joueur.ptforce*2)
                    perso_joueur.fleche -= 1
                    a = 1
                    c = False
                    choix = 1
                    attaque.menu_ = 0
                    base.menu_ = 1
                    combat.anim = 3

                if choix == 2 and attaque.menu_ == 1 and c and perso_joueur.fleche == 0:
                    c = False
                    choix = 1
                    attaque.menu_ = 0
                    base.menu_ = 1
                if objet.menu_ == 1:
                    choix, a, c = menuobjet(choix, a, c)
                elif base.menu_ == 1:
                    choix, c = menubase(choix, c)
            attaqued(d,nomennemie)

            if a == 1:
                affichage.affichageanim(d)
                combat.anim = 0
                d = 0
                if not david.alive:
                    if sinatra.alive and sinatra.active:
                        combat.tour = 3
                    else:
                        combat.tour = 0
                else:
                    combat.tour = 2
                c = False
                a = 0
                if perso_joueur.empoisoner>0:
                    perso_joueur.empoisoner-=1
                    perso_joueur.vie-=10

            if attaque.menu_ == 1:
                if perso_joueur.sortdefeu:
                    action = ["l'epee", "arc", "sort de feu", "retour"]
                else:
                    action = ["l'epee", "arc", "Vous ne savez pas lancer de sort", "retour"]

            elif base.menu_ == 1:
                action = ["attaque", "objet", "fuite", ""]
            elif objet.menu_ == 1:
                action = ["resurection", "potion de soin", "pôtion de mana", "retour"]
            combat.anim = 0


        elif combat.tour == 2:
            perso_joueur.ingame = False
            david.ingame = True
            sinatra.ingame = False
            david.immortal = False
            if c and david.taunt == 0:
                if choix == 4 and attaque.menu_ == 1 and c:
                    attaque.menu_ = 0
                    base.menu_ = 1
                    choix = 1
                    c = False
                if choix == 3 and attaque.menu_ == 1 and c:
                    a = 1
                    c = False
                    attaque.menu_ = 0
                    base.menu_ = 1
                    david.immortal = True
                    combat.anim = 5
                if choix == 1 and attaque.menu_ == 1 and c:
                    d = randint(10, 20)+(david.ptforce*2)
                    a = 1
                    c = False
                    attaque.menu_ = 0
                    base.menu_ = 1
                if choix == 2 and attaque.menu_ == 1 and c:
                    david.taunt = 3
                    a = 1
                    c = False
                    choix = 1
                    attaque.menu_ = 0
                    base.menu_ = 1
                    combat.anim = 4
                if objet.menu_ == 1:
                    choix, a, c = menuobjet(choix, a, c)
                elif base.menu_ == 1:
                    choix, c = menubase(choix, c)
            attaqued(d, nomennemie)
            if a == 1 or david.taunt > 0:
                if a == 1:
                    affichage.affichageanim(d)
                    d = 0
                if sinatra.alive and sinatra.active:
                    combat.tour = 3
                else :
                    combat.tour = 0
                c = False
                a = 0
                if david.taunt > 0:
                    david.taunt -= 1
                if david.empoisoner>0:
                    david.empoisoner-=1
                    david.vie-=10
            if attaque.menu_ == 1:
                action = ["tatane de faurins", "insulte", "defense", "retour"]
            elif base.menu_ == 1:
                action = ["attaque", "objet", "fuite", ""]
            elif objet.menu_ == 1:
                action = ["resurection", "potion de soin", "retour", ""]
            combat.anim = 0

        elif combat.tour == 3:
            perso_joueur.ingame = False
            david.ingame = False
            sinatra.ingame = True
            if c:
                if choix == 3 and attaque.menu_ == 1 and c:
                    attaque.menu_ = 0
                    base.menu_ = 1
                    choix = 1
                    c = False
                if choix == 1 and attaque.menu_ == 1 and c:
                    d = 20+(sinatra.ptforce*2)
                    a = 1
                    c = False
                    attaque.menu_ = 0
                    base.menu_ = 1
                if choix == 2 and attaque.menu_ == 1 and c:
                    sinatra.poison = True
                    a = 1
                    c = False
                    choix = 1
                    attaque.menu_ = 0
                    base.menu_ = 1
                if objet.menu_ == 1:
                    choix, a, c = menuobjet(choix, a, c)
                elif base.menu_ == 1:
                    choix, c = menubase(choix, c)
            attaqued(d, nomennemie)
            if a == 1:
                affichage.affichageanim(d)
                d = 0
                combat.tour = 0
                c = False
                a = 0
            if attaque.menu_ == 1:
                action = ["attaque furtive", "empoisonnement", "retour", ""]
            elif base.menu_ == 1:
                action = ["attaque", "objet", "fuite", ""]
            elif objet.menu_ == 1:
                action = ["resurection", "potion de soin", "retour", ""]
            combat.anim = 0


        elif combat.tour == 0:
            if nomennemie == "loup":
                if sinatra.poison:
                    loup.vie -= 10
                loup.attaque()
            elif nomennemie == "soldat":
                if sinatra.poison:
                    soldatpt.vie -= 10
                soldatpt.attaque()
            elif nomennemie == "malarich":
                if sinatra.poison:
                    malarich.vie -= 10
                malarich.attaque()
            elif nomennemie == "avalogne":
                if sinatra.poison:
                    avalogne.vie -= 10
                avalogne.attaque()
            elif nomennemie == "voleur":
                if sinatra.poison:
                    voleur.vie -= 10
                voleur.attaque()
            elif nomennemie == "hornet":
                if sinatra.poison:
                    hornet.vie -= 10
                hornet.attaque()
            elif nomennemie == "goddess":
                if sinatra.poison:
                    goddess.vie -= 10
                goddess.attaque()
            if not perso_joueur.alive:
                combat.tour = 2
            elif not david.alive and sinatra.active:
                combat.tour = 3
            else:
                combat.tour = 1

            if goddess.malediction > 0:
                perso_joueur.vie -= 10
                david.vie -= 10
                sinatra.vie -= 10
                goddess.vie += 30
                goddess.malediction -= 1
                if perso_joueur.vie<0:
                    perso_joueur.vie=0
                if david.vie<0:
                    david.vie=0
                if sinatra.vie<0:
                    sinatra.vie=0
                fennemi.verification()

        if nomennemie == "loup":
            enemitipe.vie = loup.vie
            enemitipe.image = loup.image
        if nomennemie == "soldat":
            enemitipe.vie = soldatpt.vie
            enemitipe.image = soldatpt.image
        if nomennemie == "malarich":
            enemitipe.vie = malarich.vie
            enemitipe.image = malarich.image
        if nomennemie == "avalogne":
            enemitipe.vie = avalogne.vie
            enemitipe.image = avalogne.image
        if nomennemie == "voleur":
            enemitipe.vie = voleur.vie
            enemitipe.image = voleur.image
        if nomennemie == "hornet":
            enemitipe.vie = hornet.vie
            enemitipe.image = hornet.image
        if nomennemie == "goddess":
            enemitipe.vie = goddess.vie
            enemitipe.image = goddess.image


        affichage.affichage(action, choix)





        clock.tick(60)
    return combat.etat