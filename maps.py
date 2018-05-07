import pygame, sys, quete, time
from pygame.locals import *
from classes.perso_classes import *
import menu.closemenu as closemenu, menu.printinvent as printinvent, menu.dialogue as dialogue, menu.shop as shop
import battle.combatV3
import classes.classes_map as classes_map

with open("menu/quetes/liste", "r") as listequetefi:
    listequete = listequetefi.read().split("\'")


def selecmap(fenetre):
    """Selection de la map active"""
    pygame.mixer.music.load("son/Sound/day.mp3")
    pygame.mixer.music.queue("son/Sound/RPG.mp3")
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1)
    chargement()
    with open("save1/map", "r") as fichier:
        mapactive = fichier.read()
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
    if mapactive == "fjordglasrdc":
        fjordglasrdc(fenetre)
    if mapactive == "fjordglas-1":
        fjordglas_1(fenetre)
    if mapactive == "fjordglas1":
        fjordglas1(fenetre)


def chargement():
    global capitaleload
    capitaleload = False
    global auberge_1Fload
    auberge_1Fload = False
    global chateau_1Fload
    chateau_1Fload = False
    global chateau_2Fload
    chateau_2Fload = False
    global cheminfjordload
    cheminfjordload = False
    global fjordglasrdcload
    fjordglasrdcload = False


def capitale(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("voleur")
    fichier.close()
    global capitaleload
    capitaleload = True
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("capitale")
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("capitale")
    persof.close()
    rectpersoactif = str("save1/pospeso/pospesocapitale")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    testtime = time.time()
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
        perso = persobase("maison_1")
    persof.close()
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("maison_1")
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
                    with open("save1/map", "w") as maptransi:
                        maptransi.write(mapcl.transili[i])
                    with open("save1/pospeso/pospesomaison_1", "w") as pospeso:
                        pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    with open("save1/posmap/posmapmaison_1", "w") as posmap:
                        posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
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

    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    quete.quetes(fenetre)
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    mapcl = classes_map.classmapbasique("maison_2")
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("maison_2")
    persof.close()

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
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomaison_2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_2", "w")
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
        if tkey[K_e]:
            for i in range(len(mapcl.transili)):
                if mapcl.masktransi[i].overlap(perso.mask,
                                               (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(mapcl.transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesomaison_2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_2", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(mapcl.transili[i])
                    litransifi.close()
                    quete.quetes(fenetre)
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


def auberge_1F(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global auberge_1Fload
    auberge_1Fload = True
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("auberge_1F")
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    testtime = time.time()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("auberge_1F")
    persof.close()
    affichetext = False
    myfont = pygame.font.SysFont("monospace", 20)
    rectpersoactif = str("save1/pospeso/pospesoauberge_1F")
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
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("auberge_2F")
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("auberge_2F")
    persof.close()
    rectpersoactif = str("save1/pospeso/pospesoauberge_2F")
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
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("chateau_1F")
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("chateau_1F")
    persof.close()

    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_1F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_1F", "w")
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

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(mapcl.transili)):
                if mapcl.masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(mapcl.transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_1F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    quete.quetes(fenetre)
                    global capitaleload
                    if mapcl.transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
                    if mapcl.transili[i] == "chateau_2F":
                        chateau_2F(fenetre)
                        testtime = time.time()
                        break
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
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("chateau_2F")
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("chateau_2F")
    persof.close()

    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_2F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_2F", "w")
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

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(mapcl.transili)):
                if mapcl.masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(mapcl.transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_2F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    quete.quetes(fenetre)
                    global chateau_1Fload
                    if mapcl.transili[i] == "chateau_1F":
                        if chateau_1Fload:
                            return
                        else:
                            chateau_1F(fenetre)
                    if mapcl.transili[i] == "chateau_3F":
                        chateau_3F(fenetre)
                        testtime = time.time()
                        break
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_3F(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("chateau_3F")
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("chateau_3F")
    persof.close()

    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_3F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_3F", "w")
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
        perso.eventkeytest(mapcl.rect, mapcl.mask, mapcl.size, mapcl.maskpnj)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(mapcl.transili)):
                if mapcl.masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(mapcl.transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_3F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    quete.quetes(fenetre)
                    global chateau_2Fload
                    if mapcl.transili[i] == "chateau_2F":
                        if chateau_2Fload:
                            return
                        else:
                            chateau_2F(fenetre)
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
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("mapdepart")
    image_ship = pygame.image.load("map/mapdepart/mapdepart_ship.png").convert_alpha()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("mapdepart")
    persof.close()
    jeanmafi = open("menu/quetes/jeanma/jeanma", "r")
    jeanma = jeanmafi.read()
    jeanmafi.close()

    imagemob = pygame.image.load("map/mapdepart/mapdepart_loup.png")
    maskmob = pygame.mask.from_surface(imagemob)

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
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomapdepart", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmapdepart", "w")
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
        fenetre.blit(jeanmacl.image, (jeanmacl.rect.x + mapcl.rect.x, jeanmacl.rect.y + mapcl.rect.y))
        transf = open("save1/histoire/transibateau", "r")
        transitionre = bool(int(transf.read()))
        transf.read()
        if transitionre:
            jeanmacl.move()
            fenetre.blit(image_ship, mapcl.rect)
        loupfi = open("menu/quetes/jeanma/loup", "r")
        loup = bool(int(loupfi.read()))
        loupfi.close()
        if not loup:
            fenetre.blit(imagemob, mapcl.rect)
        if tkey[K_f]:
            if maskmob.overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                mobfi = open("menu/quetes/mobmort", "w")
                mobfi.write("loup")
                mobfi.close()
                quete.quetes(fenetre)

        if perso.rect.colliderect(
                Rect(jeanmacl.rect.x + mapcl.rect.x, jeanmacl.rect.y + mapcl.rect.y, jeanmacl.rect[2],
                     jeanmacl.rect[3])):
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
            if transitionre and mapcl.masktransi[0].overlap(perso.mask,
                                                           (perso.rect.x - mapcl.rect.x,
                                                            perso.rect.y - mapcl.rect.y)):
                maptransi = open("save1/map", "w")
                maptransi.write("capitale")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesomapdepart", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmapdepart", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write("capitale")
                litransifi.close()
                quete.quetes(fenetre)
                global capitaleload

                if capitaleload:
                    return
                else:
                    capitale(fenetre)
        if affichetext2:
            fenetre.blit(myfont.render("PRESS F", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS



def cheminfjord(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global cheminfjordload
    cheminfjordload = True
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("cheminfjord")
    persof.close()
    quete.quetes(fenetre)
    mapcl = classes_map.classmapbasique("cheminfjord")
    rectpersoactif = str("save1/pospeso/pospesocheminfjord")
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)
    with open("save1/activation/perso3", "r") as sinatra:
        sinatra=bool(int(sinatra.read()))
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
                    maptransi = open("save1/map", "w")
                    maptransi.write(mapcl.transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesocheminfjord", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapcheminfjord", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    quete.quetes(fenetre)
                    fenetre.fill((0, 0, 0))
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    if mapcl.transili[i] == "capitale":
                        capitale(fenetre)
                    if mapcl.transili[i] == "fjordglasrdc" and sinatra:
                        fjordglasrdc(fenetre)
        mapcl.affichage(fenetre, perso)
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def fjordglasrdc(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()

    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/fjordglasrdc/fjordglasrdc.png").convert_alpha()
    image_obstacles = pygame.image.load("map/fjordglasrdc/fjordglasrdc_obstacle.png").convert_alpha()
    image_dessus = pygame.image.load("map/fjordglasrdc/fjordglasrdc_dessus.png").convert_alpha()
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("fjordglasrdc")
    persof.close()
    mapactives = str("save1/posmap/posmapfjordglasrdc")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    lirect = carect.split(",")
    if carect == "":
        mapactives = str("map/fjordglasrdc/spawnfjordglasrdc")
        rectf = open(mapactives, "r")
        carect = rectf.read().split(";")
        rectf.close()
        lirect = carect[0].split(",")

    position.x = int(lirect[0])
    position.y = int(lirect[1])
    glace = pygame.image.load("map/fjordglasrdc/glace.png").convert_alpha()
    glacemask = pygame.mask.from_surface(glace)
    rectpersoactif = str("save1/pospeso/pospesofjordglasrdc")
    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("map/fjordglasrdc/transifjordglasrdc", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/fjordglasrdc/fjordglasrdc_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("map/fjordglasrdc/pnjfjordglasrdc", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("map/fjordglasrdc/fjordglasrdc_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)
    onstairs = True

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
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

        if not perso.mask.overlap(glacemask, (position.x - perso.rect.x, position.y - perso.rect.y)):
            perso.glissright = False
            perso.glissleft = False
            perso.glisstop = False
            perso.glissdown = False
            perso.eventkey(position, masque, taille)
        else:
            perso.glisse(position, masque, taille)
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

                if masktransi[0].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes(fenetre)
                    global cheminfjordload
                    cheminfjord(fenetre)
        for i in range(1, 5):
            if masktransi[i].overlap(perso.mask,
                                     (perso.rect.x - position.x, perso.rect.y - position.y)) and not onstairs:

                pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                if i == 1:
                    maptransi = open("save1/map", "w")
                    maptransi.write("fjordglas-1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                    pospeso.write("398,272")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas-1", "w")
                    posmap.write("-432,-172")
                    posmap.close()
                    fjordglas_1(fenetre)
                if i == 2:
                    maptransi = open("save1/map", "w")
                    maptransi.write("fjordglas-1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                    pospeso.write("396,207")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas-1", "w")
                    posmap.write("-288,-616")
                    posmap.close()
                    fjordglas_1(fenetre)
                if i == 3:
                    maptransi = open("save1/map", "w")
                    maptransi.write("fjordglas1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                    pospeso.write("394,258")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas1", "w")
                    posmap.write("-531,-470")
                    posmap.close()
                    fjordglas1(fenetre)
                if i == 4:
                    maptransi = open("save1/map", "w")
                    maptransi.write("fjordglas1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                    pospeso.write("399,200")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas1", "w")
                    posmap.write("-339,-1091")
                    posmap.close()
                    fjordglas1(fenetre)

                onstairs = True

            elif not masktransi[1].overlap(perso.mask,
                                           (perso.rect.x - position.x, perso.rect.y - position.y)) and onstairs:
                onstairs = False

        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def fjordglas_1(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()

    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/fjordglas-1/fjordglas-1.png").convert_alpha()
    image_obstacles = pygame.image.load("map/fjordglas-1/fjordglas-1_obstacle.png").convert_alpha()
    # image_dessus = pygame.image.load("map/fjordglas-1/fjordglas-1_dessus.png").convert_alpha()
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("fjordglas-1")
    persof.close()
    mapactives = str("save1/posmap/posmapfjordglas-1")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    lirect = carect.split(",")
    if carect == "":
        mapactives = str("map/fjordglas-1/spawnfjordglas-1")
        rectf = open(mapactives, "r")
        carect = rectf.read().split(";")
        rectf.close()
        lirect = carect[0].split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])
    rectpersoactif = str("save1/pospeso/pospesofjordglas-1")
    

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("map/fjordglas-1/transifjordglas-1", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/fjordglas-1/fjordglas-1_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("map/fjordglas-1/pnjfjordglas-1", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("map/fjordglas-1/fjordglas-1_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)
    onstairs = True
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglas-1", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas-1", "w")
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
        fenetre.blit(image, position)
        fenetre.blit(perso.imageperso, perso.rect)

        # fenetre.blit(image_dessus, position)
        for i in range(2):
            if masktransi[i].overlap(perso.mask,
                                     (perso.rect.x - position.x, perso.rect.y - position.y)) and not onstairs:
                maptransi = open("save1/map", "w")
                maptransi.write("fjordglasrdc")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglas-1", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write("fjordglasrdc")
                litransifi.close()
                quete.quetes(fenetre)
                if i == 0:
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write("408,309")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write("-315,-180")
                    posmap.close()
                if i == 1:
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write("397,200")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write("-288,-635")
                    posmap.close()
                fjordglasrdc(fenetre)
                onstairs = True


            elif not masktransi[0].overlap(perso.mask,
                                           (perso.rect.x - position.x, perso.rect.y - position.y)) and onstairs:
                onstairs = False

        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def fjordglas1(fenetre):
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()

    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/fjordglas1/fjordglas1.png").convert_alpha()
    image_obstacles = pygame.image.load("map/fjordglas1/fjordglas1_obstacle.png").convert_alpha()
    # image_dessus = pygame.image.load("map/fjordglas1/fjordglas1_dessus.png").convert_alpha()
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("fjordglas1")
    persof.close()
    mapactives = str("save1/posmap/posmapfjordglas1")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    lirect = carect.split(",")
    if carect == "":
        mapactives = str("map/fjordglas1/spawnfjordglas1")
        rectf = open(mapactives, "r")
        carect = rectf.read().split(";")
        rectf.close()
        lirect = carect[0].split(",")

    position.x = int(lirect[0])
    position.y = int(lirect[1])
    rectpersoactif = str("save1/pospeso/pospesofjordglas1")
    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()
    malarich=pygame.image.load("map/fjordglas1/malarich.png").convert_alpha()
    malarichmask=pygame.mask.from_surface(malarich)
    transi = open("map/fjordglas1/transifjordglas1", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/fjordglas1/fjordglas1_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("map/fjordglas1/pnjfjordglas1", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("map/fjordglas1/fjordglas1_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("map/map.png").convert_alpha()
    pygame.mixer.music.set_volume(0.1)
    onstairs = True
    with open("save1/histoire/malarich", "r") as malarichfi:
        malarichwin=bool(int(malarichfi.read()))
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglas1", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu(fenetre)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas1", "w")
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
        if not malarichwin:
            fenetre.blit(malarich, position)
        if malarichmask.overlap(perso.mask, (perso.rect.x-position.x, perso.rect.y-position.y)) and not malarichwin :
            fichier = open("menu/quetes/mobmort", "w")
            fichier.write("malarich")
            fichier.close()
            tourpartour()
        # fenetre.blit(image_dessus, position)
        for i in range(2):
            if masktransi[i].overlap(perso.mask,
                                     (perso.rect.x - position.x, perso.rect.y - position.y)) and not onstairs:
                maptransi = open("save1/map", "w")
                maptransi.write("fjordglasrdc")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglas1", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write("fjordglasrdc")
                litransifi.close()
                quete.quetes(fenetre)
                if i == 0:
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write("397,200")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write("-416,-545")
                    posmap.close()
                if i == 1:
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write("390,228")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write("-348,-1076")
                    posmap.close()
                fjordglasrdc(fenetre)
                onstairs = True


            elif not masktransi[0].overlap(perso.mask,
                                           (perso.rect.x - position.x, perso.rect.y - position.y)) and onstairs:
                onstairs = False

        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS
