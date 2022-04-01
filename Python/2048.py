# Importation des bibliothèques
import tkinter
import copy
import pygame
import tkinter.messagebox
from fonction2048 import *
from taillefenetre import *

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
    
        for j in range(4):
            Img[i][j]=AfficherImage(TableauJeu[i][j], taille)
            Case[i][j]=tkinter.Label(fenetre, image=Img[i][j], bg ="#4d4d4d")
            Case[i][j].grid(row=i, column=j)

def Quitter():
    """
        Quitter()
            Fermer tkinter et pygame
    """

    if tkinter.messagebox.askyesno("Quitter 2048", "Voulez-vous vraiment quitter ?"):
        fenetre.destroy()
        pygame.mixer.quit()

def Son():
    """
        Son()
            Initialise ou éteint pygame.mixer en fonction de la variable paremetreSon
    """

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

def Recommancer():
    """
        Recommancer():
            Recommancer le jeu
    """

    # Variables globales
    global nbDeplacement
    global perdu

    # Remettre à zéro les tableaux
    for i in range(4):
        TableauJeu[i]=[0, 0, 0, 0]
        Case[i]=[0, 0, 0, 0]
        Img[i]=[0, 0, 0, 0]

    # Remettre à zéro le nombre de déplacement
    nbDeplacement=0
    # Remettre à zéro la variable perdu
    perdu=False

    # Boucle pour mettre deux cases de 2 dans le tableau
    case_debut=0
    while case_debut<2:
        x,y=TuileAléatoire()
        if TableauJeu[y][x]==0:
            TableauJeu[y][x]=2
            case_debut+=1

    # Afficher le jeu
    AfficherJeu()

def Appuyer(event):
    """
        Appuyer(event : event)
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
        if tkinter.messagebox.showinfo("Perdu", "Vous avez perdu !"):
            Recommancer()

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

    # Test si 2048 est atteint
    for i in range(4):
        if 2048 in TableauJeu[i]:
            # Message de victoire
            tkinter.messagebox.showinfo("Gagné", "Vous avez gagné !")
            # Demande à l'utilisateur si recommencer
            if tkinter.messagebox.askquestion("Recommencer", "Voulez-vous recommencer ?"):
                Recommancer()

# Main
# Boucle pour mettre deux cases de 2 dans le tableau
case_debut=0
while case_debut<2:
    x,y=TuileAléatoire()
    if TableauJeu[y][x]==0:
        TableauJeu[y][x]=2
        case_debut+=1

# Lancer la fonction TailleFenêtre pour avoir la taille de la fenêtre qu'on demande à l'utilisateur
taille=TailleFenetre()

# Lancer la fenêtre Tkinter
fenetre = tkinter.Tk()

# Paramètre de la fenêtre
fenetre.iconbitmap("2048.ico") # Îcone de la fenêtre
fenetre.title("2048") # Nom de la fenêtre
fenetre.resizable() # Non redimensionnement de la fenêtre

# Afficher le tableau
AfficherJeu()

# Espacement entre les cases
for i in range(4):
    fenetre.grid_columnconfigure(i, minsize=taille)
    fenetre.grid_rowconfigure(i, minsize=taille)

# Couleur de fond fond
fenetre.configure(background = "#4d4d4d")

# Exécution de la fonction "Quitter" lors de lors du click de fermeture de la fenêtre
fenetre.protocol("WM_DELETE_WINDOW", Quitter)

# Barre menu
barreMenu = tkinter.Menu(fenetre)
# Ajouter le menu au barre menu
menu = tkinter.Menu(barreMenu, tearoff=0)
# Ajouter un checkbutton au menu
paremetreSon=tkinter.BooleanVar()
paremetreSon.set(True)
menu.add_checkbutton(label="Son", onvalue=True, offvalue=False, variable=paremetreSon, command=Son())
# Ajouter bouton recommancer au menu
menu.add_command(label="Recommancer", command=Recommancer)
# Ajouter un séparateur
menu.add_separator()
# Ajouter minimiser quitter au menu
menu.add_command(label="Minimiser", command=fenetre.iconify)
# Ajouter bouton quitter au menu
menu.add_command(label="Quitter", command=lambda:[fenetre.quit(), pygame.mixer.quit()])
barreMenu.add_cascade(label="Menu", menu=menu)
fenetre.config(menu=barreMenu)

# Détecter les touches appuyées
fenetre.bind_all('<Key>',Appuyer)

# Mainloop
fenetre.mainloop()

