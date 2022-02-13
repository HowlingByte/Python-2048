# Importation des bibliothèques
import random
import pygame
import tkinter
import mouvement

# Initialisation des variables
TableauJeu= \
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
nbDeplacement=0
perdu=False

COULEUR_JEU = "#92877d"

COULEUR_CASE_VIDE = "#9e948a"

COULEUR_CASE = {
    2: "#eee4da",
    4: "#eee4da",
    8: "#f2b179",
    16: "#f59563",
    32: "#f59563",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#3c3a32",
    1024: "#3c3a32",
    2048: "#3c3a32",
    4096: "#3c3a32",
    8192: "#3c3a32"
    }

COULEUR_CHIFFRE = {
    2: "#776e65",
    4: "#776e65",
    8: "#011c08",
    16: "#f9f6f2",
    32: "f9f6f2",
    64: "#f9f6f2",
    128: "#f9f6f2",
    256: "#f9f6f2",
    512: "#f9f6f2",
    1024: "#f9f6f2",
    2048: "#f9f6f2",
    4096: "f9f6f2",
    8192: "#f9f6f2"
    }

def TuileAléatoire():
    """
        TuileAléatoire()
        Sorties :
            Deux entiers au hasard entre 0 et 3
    """
    x=random.randint(0,3)
    y=random.randint(0,3)
    return x,y

def AfficherJeu():
    """
        AfficherJeu()
        Sortie :
            Affiche le tableau avec 4 lignes
    """
    print(" ")
    for i in range(4):
        print(TableauJeu[i])

def Appuyer(event):
    """
        Fonction utilisée en jeu
    """
    # Variables globales
    global perdu
    global nbDeplacement

    # Variables locales
    caseVide=False
    deplacement=False
    deplacementPossible=False

    # Test si case vide donc déplacement possible
    for i in range(0,4):
        for j in range(0,4):
            if TableauJeu[i][j]==0:
                caseVide=True
                deplacementPossible=True


    # Test si seulement déplacement possible
    TableauJeuTemp=[TableauJeu[0].copy(), TableauJeu[1].copy(), TableauJeu[2].copy(), TableauJeu[3].copy()]
    mouvement.gauche(TableauJeuTemp)
    if TableauJeuTemp!=TableauJeu:
        deplacementPossible=True

    TableauJeuTemp=[TableauJeu[0].copy(), TableauJeu[1].copy(), TableauJeu[2].copy(), TableauJeu[3].copy()]
    mouvement.haut(TableauJeuTemp)
    if TableauJeuTemp!=TableauJeu:
        deplacementPossible=True

    TableauJeuTemp=[TableauJeu[0].copy(), TableauJeu[1].copy(), TableauJeu[2].copy(), TableauJeu[3].copy()]
    mouvement.droite(TableauJeuTemp)
    if TableauJeuTemp!=TableauJeu:
        deplacementPossible=True

    TableauJeuTemp=[TableauJeu[0].copy(), TableauJeu[1].copy(), TableauJeu[2].copy(), TableauJeu[3].copy()]
    mouvement.bas(TableauJeuTemp)
    if TableauJeuTemp!=TableauJeu:
        deplacementPossible=True


    # Si déplacement impossible, perdu
    if not deplacementPossible and not perdu:
        perdu=True
        print("Game Over !")
        print("Nombre de déplacement", ":", nbDeplacement)

    elif deplacementPossible:

        # Récupérer keycode de la touche appuyée
        keycode=(event.keycode)

        # 37 Flèche auche
        # 81 Q
        # 100 Pavé numérique gauche
        if keycode==37 or keycode==81 or keycode==100:
            mouvement.gauche(TableauJeu)

        # 38 Flèche haut
        # 90 Z
        # 104 Pavé numérique haut
        elif keycode==38 or keycode==90 or keycode==104:
            mouvement.haut(TableauJeu)

        # 39 Flèche droite
        # 68 D
        # 102 Pavé numérique droite
        elif keycode==39 or keycode==68 or keycode==102:
            mouvement.droite(TableauJeu)

        # 40 Flèche bas
        # 83 S
        # 98 Pavé numérique bas
        elif keycode==40 or keycode==83 or keycode==98:
            mouvement.bas(TableauJeu)

    if caseVide:
        # Faire apparaître une nouvelle case de 2
        while not deplacement:
            x,y=TuileAléatoire()
            if TableauJeu[y][x]==0:
                TableauJeu[y][x]=2
                deplacement=True

        # Ajouter 1 au compteur d'étape
        nbDeplacement+=1

        global case00
        global case01
        global case02
        global case03

        global case10
        global case11
        global case12
        global case13

        global case20
        global case21
        global case22
        global case33

        global case30
        global case31
        global case32
        global case33
        case00=tkinter.Label(fenetre, text=TableauJeu[0][0])
        case00.grid(row=0, column=0)
        case01=tkinter.Label(fenetre, text=TableauJeu[0][1])
        case01.grid(row=0, column=1)
        case02=tkinter.Label(fenetre, text=TableauJeu[0][2])
        case02.grid(row=0, column=2)
        case03=tkinter.Label(fenetre, text=TableauJeu[0][3])
        case03.grid(row=0, column=3)

        case10=tkinter.Label(fenetre, text=TableauJeu[1][0])
        case10.grid(row=1, column=0)
        case11=tkinter.Label(fenetre, text=TableauJeu[1][1])
        case11.grid(row=1, column=1)
        case12=tkinter.Label(fenetre, text=TableauJeu[1][2])
        case12.grid(row=1, column=2)
        case13=tkinter.Label(fenetre, text=TableauJeu[1][3])
        case13.grid(row=1, column=3)

        case20=tkinter.Label(fenetre, text=TableauJeu[2][0])
        case20.grid(row=2, column=0)
        case21=tkinter.Label(fenetre, text=TableauJeu[2][1])
        case21.grid(row=2, column=1)
        case22=tkinter.Label(fenetre, text=TableauJeu[2][2])
        case22.grid(row=2, column=2)
        case23=tkinter.Label(fenetre, text=TableauJeu[2][3])
        case23.grid(row=2, column=3)

        case10=tkinter.Label(fenetre, text=TableauJeu[3][0])
        case10.grid(row=3, column=0)
        case11=tkinter.Label(fenetre, text=TableauJeu[3][1])
        case11.grid(row=3, column=1)
        case12=tkinter.Label(fenetre, text=TableauJeu[3][2])
        case12.grid(row=3, column=2)
        case13=tkinter.Label(fenetre, text=TableauJeu[3][3])
        case13.grid(row=3, column=3)

        AfficherJeu()

# Main
# Boucle pour mettre deux cases de 2 dans le tableau
while nbDeplacement<2:
    x,y=TuileAléatoire()
    if TableauJeu[y][x]==0:
        TableauJeu[y][x]=2
        nbDeplacement+=1

# Afficher le tableau
AfficherJeu()

# Lancer la fenêtre Tkinter
fenetre = tkinter.Tk()

# Îcone de la fenêtre
fenetre.iconbitmap("2048.ico")
# Nom de la fenêtre
fenetre.title("2048")
fenetre.resizable()

case00=tkinter.Label(fenetre, text=TableauJeu[0][0])
case00.grid(row=0, column=0)
case01=tkinter.Label(fenetre, text=TableauJeu[0][1])
case01.grid(row=0, column=1)
case02=tkinter.Label(fenetre, text=TableauJeu[0][2])
case02.grid(row=0, column=2)
case03=tkinter.Label(fenetre, text=TableauJeu[0][3])
case03.grid(row=0, column=3)

case10=tkinter.Label(fenetre, text=TableauJeu[1][0])
case10.grid(row=1, column=0)
case11=tkinter.Label(fenetre, text=TableauJeu[1][1])
case11.grid(row=1, column=1)
case12=tkinter.Label(fenetre, text=TableauJeu[1][2])
case12.grid(row=1, column=2)
case13=tkinter.Label(fenetre, text=TableauJeu[1][3])
case13.grid(row=1, column=3)

case20=tkinter.Label(fenetre, text=TableauJeu[2][0])
case20.grid(row=2, column=0)
case21=tkinter.Label(fenetre, text=TableauJeu[2][1])
case21.grid(row=2, column=1)
case22=tkinter.Label(fenetre, text=TableauJeu[2][2])
case22.grid(row=2, column=2)
case23=tkinter.Label(fenetre, text=TableauJeu[2][3])
case23.grid(row=2, column=3)

case10=tkinter.Label(fenetre, text=TableauJeu[3][0])
case10.grid(row=3, column=0)
case11=tkinter.Label(fenetre, text=TableauJeu[3][1])
case11.grid(row=3, column=1)
case12=tkinter.Label(fenetre, text=TableauJeu[3][2])
case12.grid(row=3, column=2)
case13=tkinter.Label(fenetre, text=TableauJeu[3][3])
case13.grid(row=3, column=3)

# Détecter les touches appuyées
fenetre.bind_all('<Key>',Appuyer)
fenetre.mainloop()
