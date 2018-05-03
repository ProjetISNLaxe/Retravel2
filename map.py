
import sys

import pygame, sys, combatV3, shop, quete, time, printinvent, dialogue, classes_map, closemenu
from pygame.locals import *
from perso_classes import *

listequetefi = open("menu/quetes/liste", "r")
listequete = listequetefi.read().split("\'")  # Charger la liste des quêtes
listequetefi.close()


def selecmap(fenetre):
    """Selection de la map active"""
    pygame.mixer.music.load("son/Sound/day.mp3")
    pygame.mixer.music.queue("son/Sound/RPG.mp3")
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play()
    chargement()
    fichier = open("save1/map", "r")
    mapactive = fichier.read()  # On ouvre le fichier de sauvegarde
    fichier.close()
    if mapactive == "capitale":
        capitale(fenetre)
    if mapactive == "maison_1":
        maison_1(fenetre)
    if mapactive == "maison_2":
        maison_2(fenetre)
    if mapactive == "auberge_1F":
        auberge_1F(fenetre)
    if mapactive == "auberge_2F":
        auberge_2F(fenetre)
    if mapactive == "chateau_1F":
        chateau_1F(fenetre)
    if mapactive == "chateau_2F":
        chateau_2F(fenetre)
    if mapactive == "chateau_3F":
        chateau_3F(fenetre)
    if mapactive == "mapdepart":
        mapdepart(fenetre)
    if mapactive == "cheminfjord":
        cheminfjord(fenetre)


def chargement():
    global capitaleload
    capitaleload = False
    global auberge_1Fload
    auberge_1Fload = False
    global chateau_1Fload
    chateau_1Fload = False
    global chateau_2Fload
    chateau_2Fload = False


def save(perso, mapcl, i):
    maptransi = open("save1/map", "w")
    maptransi.write(mapcl.transili[i])
    maptransi.close()
    pospeso = open("save1/pospeso/pospesomaison_1", "w")
    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
    pospeso.close()
    posmap = open("save1/posmap/posmapmaison_1", "w")
    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
    posmap.close()


def capitale(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("voleur")
    fichier.close()
    global capitaleload
    capitaleload = True
    mapcl = classes_map.classmapbasique("capitale")
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    rectpersoactif = str("save1/pospeso/pospesocapitale")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    testtime = time.time()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesocapitale", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapcapitale", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesocapitale", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapcapitale", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()

        mapcl.interaction(perso, fenetre)
        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(mapcl.transili)):
                if mapcl.masktransi[i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(mapcl.transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesocapitale", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapcapitale", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(mapcl.transili[i])
                    litransifi.close()
                    quete.quetes(fenetre)
                    if mapcl.transili[i] == "maison_1":
                        maison_1(fenetre)
                        testtime = time.time()
                        break
                    if mapcl.transili[i] == "maison_2":
                        maison_2(fenetre)
                        testtime = time.time()
                        break
                    if mapcl.transili[i] == "auberge_1F":
                        auberge_1F(fenetre)
                        testtime = time.time()
                        break
                    if mapcl.transili[i] == "chateau_1F":
                        chateau_1F(fenetre)
                        testtime = time.time()
                        break
        mapcl.affichage(fenetre, perso)
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def maison_1(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    mapcl = classes_map.classmapbasique("maison_1")
    rectpersoactif = str("save1/pospeso/pospesomaison_1")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesomaison_1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmaison_1", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomaison_1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_1", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
                if event.key == K_p:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    shop.shop(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e]:
            for i in range(len(mapcl.transili)):
                if mapcl.masktransi[i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    save(perso, mapcl, i)
                    quete.quetes(fenetre)
                    fenetre.fill((0, 0, 0))
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    global capitaleload
                    if mapcl.transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
        mapcl.affichage(fenetre, perso)
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def maison_2(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/maison_2/maison_2.png").convert_alpha()
    image_obstacles = pygame.image.load("map/maison_2/maison_2_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("map/maison_2/maison_2_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    mapactives = str("save1/posmap/posmapmaison_2")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("map/maison_2/spawnmaison_2")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1/pospeso/pospesomaison_2")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("map/maison_2/transimaison_2", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/maison_2/maison_2_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("map/maison_2/pnjmaison_2", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("map/maison_2/maison_2_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesomaison_2", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmaison_2", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomaison_2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_2", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1/invent/cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)
        fenetre.blit(perso.imageperso, perso.rect)
        for i in range(len(pnjli)):
            fenetre.blit(imagepnj[i], position)
            if tkey[K_f]:

                if maskpnj[i].overlap(perso.mask,
                                      (perso.rect.x - position.x, perso.rect.y - position.y)):
                    quete.quetes(fenetre)
                    dialogue.dialogue(fenetre, pnjli[i])

        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e]:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesomaison_2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_2", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes(fenetre)
                    global capitaleload
                    if transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def auberge_1F(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global auberge_1Fload
    auberge_1Fload = True
    mapcl = classes_map.classmapbasique("auberge_1F")
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    testtime = time.time()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    affichetext = False
    myfont = pygame.font.SysFont("monospace", 20)
    rectpersoactif = str("save1/pospeso/pospesoauberge_1F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)
    onstairs = True
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesoauberge_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapauberge_1F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesoauberge_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapauberge_1F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        for i in range(len(mapcl.pnjli)):
            if mapcl.maskpnj[i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                affichetext = True
            else:
                affichetext = False
        if tkey[K_e] and time.time() - testtime > 0.5:

            if mapcl.masktransi[0].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                maptransi = open("save1/map", "w")
                maptransi.write(mapcl.transili[0])
                maptransi.close()
                pospeso = open("save1/pospeso/pospesoauberge_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapauberge_1F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write(mapcl.transili[0])
                litransifi.close()
                quete.quetes(fenetre)
                global capitaleload
                if capitaleload:
                    return
                    break
                else:
                    capitale(fenetre)
                    break
        if mapcl.masktransi[1].overlap(perso.mask,
                                       (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and not onstairs:
            maptransi = open("save1/map", "w")
            maptransi.write("auberge_2F")
            maptransi.close()
            pospeso = open("save1/pospeso/pospesoauberge_1F", "w")
            pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
            pospeso.close()
            posmap = open("save1/posmap/posmapauberge_1F", "w")
            posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
            posmap.close()
            fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
            pygame.display.flip()
            litransifi = open("menu/quetes/visitelieu", "w")
            litransifi.write("auberge_2F")
            litransifi.close()
            auberge_2F(fenetre)
            onstairs = True
        elif not mapcl.masktransi[1].overlap(perso.mask,
                                             (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and onstairs:
            onstairs = False
        mapcl.affichage(fenetre, perso)
        if affichetext:
            fenetre.blit(myfont.render("PRESS F", False, (1, 44, 166)), (perso.rect.x - 100, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def auberge_2F(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    mapcl = classes_map.classmapbasique("auberge_2F")
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    rectpersoactif = str("save1/pospeso/pospesoauberge_2F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)
    onstairs = True
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesoauberge_2F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapauberge_2F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesoauberge_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapauberge_2F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)
        if mapcl.masktransi[0].overlap(perso.mask,
                                       (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and not onstairs:
            maptransi = open("save1/map", "w")
            maptransi.write("auberge_1F")
            maptransi.close()
            pospeso = open("save1/pospeso/pospesoauberge_2F", "w")
            pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
            pospeso.close()
            posmap = open("save1/posmap/posmapauberge_2F", "w")
            posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
            posmap.close()
            fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
            pygame.display.flip()
            litransifi = open("menu/quetes/visitelieu", "w")
            litransifi.write("auberge_1F")
            litransifi.close()
            global auberge_1Fload
            if not auberge_1Fload:
                auberge_1F(fenetre)
                onstairs = True
            else:
                return
        elif not mapcl.masktransi[0].overlap(perso.mask,
                                             (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and onstairs:
            onstairs = False
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_1F(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global chateau_1Fload
    chateau_1Fload = True

    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/chateau_1F/chateau_1F.png").convert_alpha()
    image_obstacles = pygame.image.load("map/chateau_1F/chateau_1F_obstacle.png").convert_alpha()
    # image_dessus = pygame.image.load("map/chateau_1F/chateau_1F_dessus.png").convert_alpha()
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    mapactives = str("save1/posmap/posmapchateau_1F")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("map/chateau_1F/spawnchateau_1F")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1/pospeso/pospesochateau_1F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("map/chateau_1F/transichateau_1F", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/chateau_1F/chateau_1F_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("map/chateau_1F/pnjchateau_1F", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("map/chateau_1F/chateau_1F_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_1F", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_1F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1/invent/cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:

                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):
                        quete.quetes(fenetre)
                        dialogue(fenetre, pnjli[i])
        except:
            None

        # fenetre.blit(image_dessus, position)

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_1F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes(fenetre)
                    global capitaleload
                    if transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
                    if transili[i] == "chateau_2F":
                        chateau_2F(fenetre)
                        testtime = time.time()
                        break
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_2F(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global chateau_2Fload
    chateau_2Fload = True

    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/chateau_2F/chateau_2F.png").convert_alpha()
    image_obstacles = pygame.image.load("map/chateau_2F/chateau_2F_obstacle.png").convert_alpha()
    image_dessus = pygame.image.load("map/chateau_2F/chateau_2F_dessus.png").convert_alpha()
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    mapactives = str("save1/posmap/posmapchateau_2F")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("map/chateau_2F/spawnchateau_2F")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1/pospeso/pospesochateau_2F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("map/chateau_2F/transichateau_2F", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/chateau_2F/chateau_2F_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("map/chateau_2F/pnjchateau_2F", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("map/chateau_2F/chateau_2F_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_2F", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_2F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1/invent/cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:

                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):
                        quete.quetes(fenetre)
                        dialogue(fenetre, pnjli[i])
        except:
            None

        fenetre.blit(image_dessus, position)

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_2F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes(fenetre)
                    global chateau_1Fload
                    if transili[i] == "chateau_1F":
                        if chateau_1Fload:
                            return
                        else:
                            chateau_1F(fenetre)
                    if transili[i] == "chateau_3F":
                        chateau_3F(fenetre)
                        testtime = time.time()
                        break
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_3F(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/chateau_3F/chateau_3F.png").convert_alpha()
    image_obstacles = pygame.image.load("map/chateau_3F/chateau_3F_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("map/chateau_3F/chateau_3F_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    mapactives = str("save1/posmap/posmapchateau_3F")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("map/chateau_3F/spawnchateau_3F")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1/pospeso/pospesochateau_3F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("map/chateau_3F/transichateau_3F", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/chateau_3F/chateau_3F_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))

    pnji = open("map/chateau_3F/pnjchateau_3F", "r")
    pnj = pnji.read()
    pnji.close()
    pnjli = pnj.split(",")
    imagepnj = []
    maskpnj = []

    for i in range(len(pnjli)):
        imagepnj.append(
            pygame.image.load("map/chateau_3F/chateau_3F_" + pnjli[i] + ".png"))
        maskpnj.append(pygame.mask.from_surface(imagepnj[i]))

    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_3F", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_3F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/screenshot.jpg")
                    printinvent.printinvent(fenetre)
                if event.type == KEYUP:
                    if event.key == K_DOWN:
                        perso.imageperso = perso.F1
                    if event.key == K_UP:
                        perso.imageperso = perso.B1
                    if event.key == K_RIGHT:
                        perso.imageperso = perso.R1
                    if event.key == K_LEFT:
                        perso.imageperso = perso.L1
        perso.eventkeytest(position, masque, taille, maskpnj)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1/invent/cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)
        for i in range(len(pnjli)):
            fenetre.blit(imagepnj[i], position)
        fenetre.blit(perso.imageperso, perso.rect)

        for i in range(len(pnjli)):
            if tkey[K_f]:

                if maskpnj[i].overlap(perso.mask,
                                      (perso.rect.x - position.x, perso.rect.y - position.y)):
                    quete.quetes(fenetre)
                    dialogue(fenetre, pnjli[i])

        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e]:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_3F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes(fenetre)
                    global chateau_2Fload
                    if transili[i] == "chateau_2F":
                        if chateau_2Fload:
                            return
                        else:
                            chateau_2F(fenetre)
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def mapdepart(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global mapdepartload
    mapdepartload = True
    jeanmacl = David()
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/mapdepart/mapdepart.png").convert_alpha()
    image_obstacles = pygame.image.load("map/mapdepart/mapdepart_obstacle.png").convert_alpha()
    image_ship = pygame.image.load("map/mapdepart/mapdepart_ship.png").convert_alpha()
    # image_dessus = pygame.image.load("map/mapdepart/mapdepart_dessus.png").convert_alpha()
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    mapactives = str("save1/posmap/posmapmapdepart")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("map/mapdepart/spawnmapdepart")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])
    jeanmafi = open("menu/quetes/jeanma/jeanma", "r")
    jeanma = jeanmafi.read()
    jeanmafi.close()

    rectpersoactif = str("save1/pospeso/pospesomapdepart")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("map/mapdepart/transimapdepart", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/mapdepart/mapdepart_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("map/mapdepart/pnjmapdepart", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("map/mapdepart/mapdepart_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None

    mobi = open("map/mapdepart/mobmapdepart", "r")
    mob = mobi.read()
    mobi.close()
    mobli = mob.split(",")
    imagemob = []
    maskmob = []

    for i in range(len(mobli)):
        imagemob.append(
            pygame.image.load("map/mapdepart/mapdepart_" + mobli[i] + ".png"))
        maskmob.append(pygame.mask.from_surface(imagemob[i]))

    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesomapdepart", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmapdepart", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomapdepart", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmapdepart", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        transf = open("save1/histoire/transibateau", "r")
        transitionre = bool(int(transf.read()))
        transf.read()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask,
                                     (perso.rect.x - position.x, perso.rect.y - position.y)) and transitionre:
                affichetext = True
                break
            else:
                affichetext = False
        fenetre.blit(image, position)
        if transitionre:
            jeanmacl.move()
            fenetre.blit(image_ship, position)
        fenetre.blit(perso.imageperso, perso.rect)
        fenetre.blit(jeanmacl.image, (jeanmacl.rect.x + position.x, jeanmacl.rect.y + position.y))
        for i in range(len(mobli)):
            loupfi = open("menu/quetes/jeanma/loup", "r")
            loup = bool(int(loupfi.read()))
            loupfi.close()
            if not loup:
                fenetre.blit(imagemob[i], position)
            if tkey[K_f]:
                if maskmob[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                    mobfi = open("menu/quetes/mobmort", "w")
                    mobfi.write(mobli[i])
                    mobfi.close()
                    quete.quetes(fenetre)

        if perso.rect.colliderect(
                Rect(jeanmacl.rect.x + position.x, jeanmacl.rect.y + position.y, jeanmacl.rect[2], jeanmacl.rect[3])):
            affichetext2 = True
            if tkey[K_f]:
                if jeanma == "1":
                    dialogue.dialogue(fenetre, "jeanma")
                    quete.quetes(fenetre)

                else:
                    dialogue.jeanmadia(fenetre)
                    quete.quetes(fenetre)
                    jeanma = "1"
        else:
            affichetext2 = False

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(transili)):
                if transitionre and masktransi[i].overlap(perso.mask,
                                                          (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesomapdepart", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmapdepart", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes(fenetre)

                    global capitaleload
                    if transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
        if affichetext:
            fenetre.blit(myfont.render("Travel", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if affichetext2:
            fenetre.blit(myfont.render("PRESS F", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def cheminfjord(fenetre):
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close()
    mapcl = classes_map.classmapbasique("cheminfjord")
    rectpersoactif = str("save1/pospeso/pospesocheminfjord")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesocheminfjord", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapcheminfjord", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesocheminfjord", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapcheminfjord", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent(fenetre)
                if event.key == K_p:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    shop.shop(fenetre)
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    perso.imageperso = perso.F1
                if event.key == K_UP:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e]:
            for i in range(len(mapcl.transili)):
                if mapcl.masktransi[i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    save(perso, mapcl, i)
                    quete.quetes(fenetre)
                    fenetre.fill((0, 0, 0))
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    global capitaleload
                    if mapcl.transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
        mapcl.affichage(fenetre, perso)
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS
