# Importation des bibliothèques
import random
import tkinter
import copy
import pygame
from fonction2048 import *

# Importation de messagebox de tkinter
from tkinter import messagebox

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
            Case[i][j]=tkinter.Label(fenetre, image=Img[i][j], bg ="#4d4d4d")
            Case[i][j].grid(row=i, column=j)

def Quitter():
    """
        Quitter()
            Fermer tkinter et pygame
    """
    if messagebox.askyesno("Quitter 2048", "Voulez-vous vraiment quitter ?"):
        fenetre.destroy()
        pygame.mixer.quit()

def Son():
    if paremetreSon.get():
        pygame.mixer.init()
    else:
        pygame.mixer.quit()

def JouerSon(son):
    """
        JouerSon(son : string)
            Jouer le son donné
    """
    if paremetreSon.get():
        pygame.mixer.music.load(son)
        pygame.mixer.music.play(loops=0)

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
    deplacementFait=False

    # Test si case vide donc déplacement possible
    for i in range(0,4):
        for j in range(0,4):
            if TableauJeu[i][j]==0:
                caseVide=True
                deplacementPossible=True


    # Test si seulement déplacement possible
    TableauJeuTempGauche=copy.deepcopy(TableauJeu)
    deplacementGauche, fusionGauche=mouvement.gauche(TableauJeuTempGauche)

    TableauJeuTempHaut=copy.deepcopy(TableauJeu)
    deplacementHaut, fusionHaut=mouvement.haut(TableauJeuTempHaut)

    TableauJeuTempDroite=copy.deepcopy(TableauJeu)
    deplacementDroite, fusionDroite=mouvement.droite(TableauJeuTempDroite)

    TableauJeuTempBas=copy.deepcopy(TableauJeu)
    deplacementBas, fusionBas=mouvement.bas(TableauJeuTempBas)

    if deplacementGauche or deplacementHaut or deplacementDroite or deplacementBas or fusionGauche or fusionHaut or fusionDroite or fusionBas:
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
        if (keycode==37 or keycode==81 or keycode==100) and (deplacementGauche or fusionGauche):
            mouvement.gauche(TableauJeu)
            deplacementFait=True

            if fusionGauche:
                JouerSon("Audio/Fusion.mp3")
            else:
                JouerSon("Audio/Deplacement.mp3")

        # 38 Flèche haut
        # 90 Z
        # 104 Pavé numérique haut
        elif (keycode==38 or keycode==90 or keycode==104) and (deplacementHaut or fusionHaut):
            mouvement.haut(TableauJeu)
            deplacementFait=True

            if fusionHaut:
                JouerSon("Audio/Fusion.mp3")
            else:
                JouerSon("Audio/Deplacement.mp3")

        # 39 Flèche droite
        # 68 D
        # 102 Pavé numérique droite
        elif (keycode==39 or keycode==68 or keycode==102) and (deplacementDroite or fusionDroite):
            mouvement.droite(TableauJeu)
            deplacementFait=True

            if fusionDroite:
                JouerSon("Audio/Fusion.mp3")
            else:
                JouerSon("Audio/Deplacement.mp3")

        # 40 Flèche bas
        # 83 S
        # 98 Pavé numérique bas
        elif (keycode==40 or keycode==83 or keycode==98) and (deplacementBas or fusionBas):
            mouvement.bas(TableauJeu)
            deplacementFait=True

            if fusionBas:
                JouerSon("Audio/Fusion.mp3")
            else:
                JouerSon("Audio/Deplacement.mp3")

    if caseVide and deplacementFait:
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
case_debut=0
while case_debut<2:
    x,y=TuileAléatoire()
    if TableauJeu[y][x]==0:
        TableauJeu[y][x]=2
        case_debut+=1

# Lancer la fenêtre Tkinter
fenetre = tkinter.Tk()

# Paramètre de la fenêtre
fenetre.iconbitmap("2048.ico") # Îcone de la fenêtre
fenetre.title("2048") # Nom de la fenêtre
fenetre.resizable(False, False) # Non redimensionnement de la fenêtre

# Afficher le tableau
AfficherJeu()

# Espacement entre les cases
nombreCol, nombreRow = fenetre.grid_size()
for col in range(nombreCol):
    fenetre.grid_columnconfigure(col, minsize=200)
for row in range(nombreRow):
    fenetre.grid_rowconfigure(row, minsize=200)

# Couleur de fond fond
fenetre.configure(background = "#4d4d4d")

# Exécution de la fonction "Quitter" lors de lors du click de fermeture de la fenêtre
fenetre.protocol("WM_DELETE_WINDOW", Quitter)

# Barre menu
barreMenu = tkinter.Menu(fenetre)
menu = tkinter.Menu(barreMenu, tearoff=0)
paremetreSon=tkinter.BooleanVar()
paremetreSon.set(True)
menu.add_checkbutton(label="Son", onvalue=True, offvalue=False, variable=paremetreSon, command=Son())
menu.add_command(label="Minimiser", command=fenetre.iconify)
menu.add_command(label="Quitter", command=Quitter)
barreMenu.add_cascade(label="Menu", menu=menu)
fenetre.config(menu=barreMenu)

# Détecter les touches appuyées
fenetre.bind_all('<Key>',Appuyer)

# Mainloop
fenetre.mainloop()