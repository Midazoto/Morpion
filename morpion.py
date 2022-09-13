import pygame
img=pygame.image.load("morpio10.jpg")
egalite=pygame.image.load("egalite.png")
victoire_rond=pygame.image.load("v_rond.png")
victoire_croix=pygame.image.load("v_croix.png")
def morpion(joueur1,joueur2=None):
    surf=pygame.display.set_mode((800,800))
    run=True
    surf.fill((100,100,100))
    surf.blit(img,(250,250))
    case1=0
    case2=0
    case3=0
    case4=0
    case5=0
    case6=0
    case7=0
    case8=0
    case9=0
    joueur=0
    victoire=0
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    case1=0
                    case2=0
                    case3=0
                    case4=0
                    case5=0
                    case6=0
                    case7=0
                    case8=0
                    case9=0
                    joueur=0
                    victoire=0
                    surf.fill((100,100,100))
                    surf.blit(img,(250,250))
            if victoire==0:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()==(1,0,0):

                        if (pos[1]>250)and(pos[1]<350): #Ligne 1

                            if(pos[0]>250)and(pos[0]<350): #Case 1
                                if case1==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(250,250),(350,350),5)
                                        pygame.draw.line(surf,(0,0,0),(350,250),(250,350),5)
                                        case1=1
                                        if (case2==1) and (case3==1):
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(250,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(550,250),(450,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case5==1) and (case9==1):
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(250,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,550),(550,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case4==1) and (case7==1):
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(250,350),5)
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,550),(350,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(300,300),50,5)
                                        case1=2
                                        if (case2==2) and (case3==2):
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case5==2) and (case9==2):
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case4==2) and (case7==2):
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))

                            if (pos[0]>350)and(pos[0]<450): #Case 2
                                if case2==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(350,250),(450,350),5)
                                        pygame.draw.line(surf,(0,0,0),(450,250),(350,350),5)
                                        case2=1
                                        if (case1==1) and (case3==1):
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(250,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(550,250),(450,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case5==1) and (case8==1):
                                            pygame.draw.line(surf,(255,0,0),(350,250),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,550),(450,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(400,300),50,5)
                                        case2=2
                                        if (case1==2) and (case3==2):
                                            pygame.draw.circle(surf,(255,0,0),(400,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case5==2) and (case8==2):
                                            pygame.draw.circle(surf,(255,0,0),(400,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))

                            if (pos[0]>450)and(pos[0]<550): #Case 3
                                if case3==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(450,250),(550,350),5)
                                        pygame.draw.line(surf,(0,0,0),(550,250),(450,350),5)
                                        case3=1
                                        if (case1==1) and (case2==1):
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(250,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(550,250),(450,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case5==1) and (case7==1):
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,250),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,550),(350,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case6==1) and (case9==1):
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,250),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,550),(550,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(500,300),50,5)
                                        case3=2
                                        if (case2==2) and (case1==2):
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,300),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case5==2) and (case7==2):
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case6==2) and (case9==2):
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))

                        if(pos[1]>350)and(pos[1]<450): #Ligne 2
                            if (pos[0]>250)and(pos[0]<350): #Case 4
                                if case4==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(250,350),(350,450),5)
                                        pygame.draw.line(surf,(0,0,0),(350,350),(250,450),5)
                                        case4=1
                                        if (case1==1) and (case7==1):
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(250,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,250),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,550),(350,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case5==1) and (case6==1):
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(250,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(300,400),50,5)
                                        case4=2
                                        if (case1==2) and (case7==2):
                                            pygame.draw.circle(surf,(255,0,0),(300,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case5==2) and (case6==2):
                                            pygame.draw.circle(surf,(255,0,0),(300,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,400),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))

                            if (pos[0]>350)and(pos[0]<450): #Case 5
                                if case5==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(350,350),(450,450),5)
                                        pygame.draw.line(surf,(0,0,0),(450,350),(350,450),5)
                                        case5=1
                                        if (case1==1) and (case9==1):
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,250),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,550),(550,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case3==1) and (case7==1):
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,550),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,250),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case2==1) and (case8==1):
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,250),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,550),(450,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case4==1) and (case6==1):
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(400,400),50,5)
                                        case5=2
                                        if (case1==2) and (case9==2):
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case3==2) and (case7==2):
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case2==2) and (case8==2):
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case4==2) and (case6==2):
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,400),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))

                            if (pos[0]>450)and(pos[0]<550): #Case 6
                                if case6==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(450,350),(550,450),5)
                                        pygame.draw.line(surf,(0,0,0),(550,350),(450,450),5)
                                        case6=1
                                        if (case3==1) and (case9==1):
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,450),5)
                                            pygame.draw.line(surf,(255,0,0),(550,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,250),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,550),(550,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case4==1) and (case5==1):
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,450),5)
                                            pygame.draw.line(surf,(255,0,0),(550,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(500,400),50,5)
                                        case6=2
                                        if (case3==2) and (case9==2):
                                            pygame.draw.circle(surf,(255,0,0),(500,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case4==2) and (case5==2):
                                            pygame.draw.circle(surf,(255,0,0),(500,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,400),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))

                        if(pos[1]>450)and(pos[1]<550): #Ligne 3
                            if (pos[0]>250)and(pos[0]<350):#Case 7
                                if case7==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(250,450),(350,550),5)
                                        pygame.draw.line(surf,(0,0,0),(350,450),(250,550),5)
                                        case7=1
                                        if (case1==1) and (case4==1):
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(250,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,250),5)
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case3==1) and (case5==1):
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(250,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,250),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case8==1) and (case9==1):
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(250,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,550),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,550),(550,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(300,500),50,5)
                                        case7=2
                                        if (case1==2) and (case4==2):
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,400),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case3==2) and (case5==2):
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case8==2) and (case9==2):
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))

                            if (pos[0]>350)and(pos[0]<450): #Case 8
                                if case8==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(350,450),(450,550),5)
                                        pygame.draw.line(surf,(0,0,0),(450,450),(350,550),5)
                                        case8=1
                                        if (case7==1) and (case9==1):
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,550),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,550),(550,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case2==1) and (case5==1):
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,250),(450,350),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,250),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(400,500),50,5)
                                        case8=2
                                        if (case7==2) and (case9==2):
                                            pygame.draw.circle(surf,(255,0,0),(400,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case2==2) and (case5==2):
                                            pygame.draw.circle(surf,(255,0,0),(400,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))

                            if (pos[0]>450)and(pos[0]<550): #Case 9
                                if case9==0:
                                    if joueur == 0:
                                        pygame.draw.line(surf,(0,0,0),(450,450),(550,550),5)
                                        pygame.draw.line(surf,(0,0,0),(550,450),(450,550),5)
                                        case9=1
                                        if (case3==1) and (case6==1):
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(550,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(450,250),(550,350),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,250),5)
                                            pygame.draw.line(surf,(255,0,0),(450,350),(550,450),5)
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case1==1) and (case5==1):
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(550,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,250),(350,350),5)
                                            pygame.draw.line(surf,(255,0,0),(250,350),(350,250),5)
                                            pygame.draw.line(surf,(255,0,0),(350,350),(450,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,350),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        if (case7==1) and (case8==1):
                                            pygame.draw.line(surf,(255,0,0),(450,450),(550,550),5)
                                            pygame.draw.line(surf,(255,0,0),(550,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,450),(350,550),5)
                                            pygame.draw.line(surf,(255,0,0),(250,550),(350,450),5)
                                            pygame.draw.line(surf,(255,0,0),(350,450),(450,550),5)
                                            pygame.draw.line(surf,(255,0,0),(350,550),(450,450),5)
                                            victoire=1
                                            surf.blit(victoire_croix,(100,100))
                                        joueur=1
                                    else:
                                        pygame.draw.circle(surf,(0,0,0),(500,500),50,5)
                                        case9=2
                                        if (case3==2) and (case6==2):
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(500,400),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case1==2) and (case5==2):
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,300),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,400),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        if (case7==2) and (case8==2):
                                            pygame.draw.circle(surf,(255,0,0),(500,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(400,500),50,5)
                                            pygame.draw.circle(surf,(255,0,0),(300,500),50,5)
                                            victoire=1
                                            surf.blit(victoire_rond,(100,100))
                                        joueur=0
                                    if (victoire==0) and (case1!=0) and (case2!=0) and (case3!=0) and (case4!=0) and (case5!=0) and (case6!=0) and (case7!=0) and (case8!=0) and (case9!=0):
                                        surf.blit(egalite,(100,100))
            if event.type==pygame.QUIT:
                run=False

        pygame.display.flip()
    pygame.quit()
morpion("Nathan")