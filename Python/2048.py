# Importation des bibliothèques
import tkinter
import copy
import pygame
import tkinter.messagebox

# Importation des fichiers .py du dossier python
import mouvement
from fonction2048 import *
from taillefenetre import *

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
score=0

def AfficherJeu():
    """
        AfficherJeu()
        Sortie :
            Affiche le tableau avec 4 lignes et forme la fenêtre
    """
    global score

    print(" ")
    for i in range(4):
        # Afficher les 4 lignes
        print(TableauJeu[i])
    
        # Création des images
        for j in range(4):
            Img[i][j]=AfficherImage(TableauJeu[i][j], taille)
            Case[i][j]=tkinter.Label(fenetre, image=Img[i][j], bg ="#4d4d4d")
            Case[i][j].grid(row=i+5, column=j)
        
    # Calculer la somme du tableau
    sommeTableau=sum(TableauJeu[0])+sum(TableauJeu[1])+sum(TableauJeu[2])+sum(TableauJeu[3])

    # Afficher le nombre de déplacement
    nbDeplacementLabel=tkinter.Label(fenetre, text=f"  Nombre de déplacement : {nbDeplacement}\t\t", bg ="#4d4d4d", fg="white", font=("Helvetica", 10, "bold"))
    nbDeplacementLabel.grid(row=1, column=0, columnspan=4, sticky="w")

    # Afficher le score
    scoreLabel=tkinter.Label(fenetre, text=f"  Score : {score}\t\t", bg ="#4d4d4d", fg="white", font=("Helvetica", 10, "bold"))
    scoreLabel.grid(row=2, column=0, columnspan=4, sticky="w")

    # Afficher la somme du tableau
    sommeTableauLabel=tkinter.Label(fenetre, text=f"  Somme du tableau : {sommeTableau}\t\t", bg ="#4d4d4d", fg="white", font=("Helvetica", 10, "bold"))
    sommeTableauLabel.grid(row=3, column=0, columnspan=4, sticky="w")    

def Quitter():
    """
        Quitter()
            Fermer tkinter et pygame
    """

    if tkinter.messagebox.askyesno("Quitter 2048", "Voulez-vous vraiment quitter ?"):
        fenetre.destroy()
        pygame.mixer.quit()
        exit()

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
    global score

    # Remettre à zéro les tableaux
    for i in range(4):
        TableauJeu[i]=[0, 0, 0, 0]
        Case[i]=[0, 0, 0, 0]
        Img[i]=[0, 0, 0, 0]

    # Remettre à zéro le nombre de déplacement
    nbDeplacement=0
    # Remettre à zéro la variable perdu
    perdu=False
    # Remettre à zéro le score
    score=0

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
    global score

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
    deplacementGauche, fusionGauche, scoreGauche=mouvement.gauche(TableauJeuTempGauche)

    TableauJeuTempHaut=copy.deepcopy(TableauJeu)
    deplacementHaut, fusionHaut, scoreHaut=mouvement.haut(TableauJeuTempHaut)

    TableauJeuTempDroite=copy.deepcopy(TableauJeu)
    deplacementDroite, fusionDroite, scoreDroite=mouvement.droite(TableauJeuTempDroite)

    TableauJeuTempBas=copy.deepcopy(TableauJeu)
    deplacementBas, fusionBas, scoreBas=mouvement.bas(TableauJeuTempBas)

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
                score+=scoreGauche
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
                score+=scoreHaut
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
                score+=scoreDroite
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
                score+=scoreBas
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
    """
    # Récupére la largeur
    width = fenetre.winfo_width() 
    # Récupére la hauteur
    height = fenetre.winfo_height()
    print("Largeur :", width)   # Affiche la largeur
    print("Hauteur :", height) 
    """

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
fenetre.resizable(False, False) # Non redimensionnement de la fenêtre

# Afficher le tableau
AfficherJeu()

# Espacement entre les cases
for i in range(4):
    fenetre.grid_columnconfigure(i, minsize=taille)
    fenetre.grid_rowconfigure(i+5, minsize=taille)

# Couleur de fond fond
fenetre.configure(background = "#4d4d4d")

# Exécution de la fonction "Quitter" lors de lors du click de fermeture de la fenêtre
fenetre.protocol("WM_DELETE_WINDOW", Quitter)

# Barre de menu
barreMenu = tkinter.Frame(fenetre, borderwidth=3, bg="#3C3C3C")
barreMenu.grid(row=0, column=0, columnspan=4, sticky="nsew")
# Création de l"onglet Menu
menu = tkinter.Menubutton(barreMenu, text="Menu", bg="#3C3C3C", activebackground="#505050", activeforeground="white", foreground="white")
menu.grid(row=0, column=0)
# Création d"un menu défilant
menuDeroulant = tkinter.Menu(menu, background="#4d4d4d", foreground="#ffffff", tearoff=0)
# Ajouter un checkbutton au menu
paremetreSon=tkinter.BooleanVar()
paremetreSon.set(True)
menuDeroulant.add_checkbutton(label="Son", onvalue=True, offvalue=False, variable=paremetreSon, command=Son())
# Ajouter bouton recommancer au menu
menuDeroulant.add_command(label="Recommancer", command=Recommancer)
# Ajouter un séparateur
menuDeroulant.add_separator()
# Ajouter minimiser quitter au menu
menuDeroulant.add_command(label="Minimiser", command=fenetre.iconify)
# Ajouter bouton quitter au menu
menuDeroulant.add_command(label="Quitter", command=lambda:[fenetre.quit(), pygame.mixer.quit(), exit()])
# Ajouter un séparateur
menuDeroulant.add_separator()
# Ajouter un bouton à propos au menu
menuDeroulant.add_command(label="À propos", command = lambda:[tkinter.messagebox.showinfo("À propos", "2048 (Projet NSI GA.1)\n\nCréé par :\n\n- ING Bryan\n- ABASSE Tidiane\n- GALANG Andrei\n\nVersion : 5.0")])
# Attribution du menu déroulant au menu Affichage
menu.configure(menu=menuDeroulant)

"""
# Barre menu
barreMenu = tkinter.Menu(fenetre)
# Ajouter le menu au barre menu
menu = tkinter.Menu(barreMenu, tearoff=0, background="#4d4d4d", foreground="white")
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
menu.add_command(label="Quitter", command=lambda:[fenetre.quit(), pygame.mixer.quit(), exit()])
# Ajouter un séparateur
menu.add_separator()
# Ajouter un bouton à propos au menu
menu.add_command(label="À propos", command=lambda:[tkinter.messagebox.showinfo("À propos", "2048 (Projet NSI GA.1)\n\nCréé par :\n\n- ING Bryan\n- ABASSE Tidiane\n- GALANG Andrei\n\nVersion : 5.0")])
barreMenu.add_cascade(label="Menu", menu=menu)
fenetre.config(menu=barreMenu)
"""

# Détecter les touches appuyées
fenetre.bind_all("<Key>",Appuyer)

# Mainloop
fenetre.mainloop()

