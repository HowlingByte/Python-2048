# Importation des bibliothèques
import random
import tkinter
import copy

# Importation du fichier mouvement.py
import mouvement

# Initialisation des variables
TableauJeu= \
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
Case= \
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
Img= \
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
nbDeplacement=0
perdu=False

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
            Affiche le tableau avec 4 lignes et forme la fenêtre
    """
    print(" ")
    for i in range(4):
        print(TableauJeu[i])

    for i in range(4):
        for j in range(4):
            Img[i][j]=AfficherImage(TableauJeu[i][j])
            Case[i][j]=tkinter.Label(fenetre, image=Img[i][j])
            Case[i][j].grid(row=i, column=j)

def AfficherImage(case):
    """
        AfficherImage(case : entier) : tkinter.PhotoImage
        Entrée :
            case : numéro de la case
        Sortie :
            tkinter.PhotoImage - image de la case
    """
    return (tkinter.PhotoImage(file=f"Cases/{case}.png"))

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
    TableauJeuTemp=copy.deepcopy(TableauJeu)
    mouvement.gauche(TableauJeuTemp)
    if TableauJeuTemp!=TableauJeu:
        deplacementPossible=True

    TableauJeuTemp=copy.deepcopy(TableauJeu)
    mouvement.haut(TableauJeuTemp)
    if TableauJeuTemp!=TableauJeu:
        deplacementPossible=True

    TableauJeuTemp=copy.deepcopy(TableauJeu)
    mouvement.droite(TableauJeuTemp)
    if TableauJeuTemp!=TableauJeu:
        deplacementPossible=True

    TableauJeuTemp=copy.deepcopy(TableauJeu)
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

        # Valeur du tableau "TableauJeu" dans la fenêtre
        AfficherJeu()

# Main
# Boucle pour mettre deux cases de 2 dans le tableau
while nbDeplacement<2:
    x,y=TuileAléatoire()
    if TableauJeu[y][x]==0:
        TableauJeu[y][x]=2
        nbDeplacement+=1

# Lancer la fenêtre Tkinter
fenetre = tkinter.Tk()

# Îcone de la fenêtre
fenetre.iconbitmap("2048.ico")
# Nom de la fenêtre
fenetre.title("2048")
fenetre.resizable(False, False)

# Afficher le tableau
AfficherJeu()

# Détecter les touches appuyées
fenetre.bind_all('<Key>',Appuyer)
fenetre.mainloop()
