import pygame


interfaceinvent=pygame.image.load("menu/inventory/interface_inventaire_objets.png").convert_alpha()
ouverture = pygame.mixer.Sound("son/Sound/Menu_Open.wav")
fermeture = pygame.mixer.Sound("son/Sound/Menu_Close.wav")
sounditem = pygame.mixer.Sound("son/Sound/Item_1.wav")
emplacementperso0=pygame.image.load("menu/inventory/emplacementperso0.png").convert_alpha()
emplacementperso1=pygame.image.load("menu/inventory/emplacementperso1.png").convert_alpha()
emplacementperso2=pygame.image.load("menu/inventory/emplacementperso2.png").convert_alpha()
perso0=pygame.image.load("perso/N-Ship/F1.png").convert_alpha()
stuff_actuel=pygame.image.load("menu/inventory/stuff_actuel.png").convert_alpha()
curseur=pygame.image.load("menu/inventory/curseur.png").convert_alpha()
test = pygame.image.load("launcher/pixelgitan.png").convert_alpha()
testrect=test.get_rect()
curseurrect=curseur.get_rect()
testmask=pygame.mask.from_surface(test)
curseurmask=pygame.mask.from_surface(curseur)

police=pygame.font.SysFont("monospace", 15)
objetinventairerect = []
listechiffre = []
taillechiffre= []
for i in range (10):
    listechiffre.append(pygame.image.load("menu/inventory/chiffre/chiffre0"+str(i)+".png").convert_alpha())
    taillechiffre.append(listechiffre[i].get_size())
consommable=["pomme","nbsoin", "mana", "nbresurect"]

ongletli=[]
for i in range(3):
    ongletli.append(pygame.image.load("menu/inventory/onglet"+str(i)+".png").convert_alpha())
onglet=ongletli[0]
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet=list(alphabet)
inventaireimage = pygame.image.load("menu/inventory/objetinventaire.png").convert_alpha()