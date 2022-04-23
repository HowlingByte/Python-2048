# Importation des bibliothèques
import tkinter
import tkinter.messagebox
import copy
import pygame
import sys
import signal
from PIL import Image, ImageTk

# Importation des fichiers .py du dossier python
import mouvement
from autresfonctions2048 import *
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
gagne=False
score=0
minimiser=False

def sigint_handler(signal, frame):
    """
        sigint_handler(signal, frame)
            Ferme la fenetre sans erreur lors du KeyboardInterrupt
    """
    fenetre.destroy() # Fermer la fenêtre
    pygame.mixer.quit() # Fermer pygame
    exit() # Quitter le programme

def BougerFenetreCommence(event):
    global x, y # On récupère les variables x et y
    x = event.x # On récupère la position de la souris en x
    y = event.y # On récupère la position de la souris en y

def BougerFenetreArrete(event):
    global x, y # On récupère les variables x et y
    x = None # On réinitialise x
    y = None # On réinitialise y

def BougerFenetre(event):
    """
        BougerFenetre(event)
        Entrée :
            event : événement
        Sortie :
            Bouge la fenêtre
    """
    global x, y # On récupère les variables x et y
    deltax = event.x - x # On calcule la différence entre la position de la souris et la position de la souris au début du déplacement 
    deltay = event.y - y # On calcule la différence entre la position de la souris et la position de la souris au début du déplacement
    ax = fenetre.winfo_x() + deltax # On calcule la nouvelle position de la fenêtre en fonction de la différence entre la position de la souris et la position de la souris au début du déplacement
    ay = fenetre.winfo_y() + deltay # On calcule la nouvelle position de la fenêtre en fonction de la différence entre la position de la souris et la position de la souris au début du déplacement
    fenetre.geometry(f"+{ax}+{ay}") # On déplace la fenêtre

def Quitter():
    """
        Quitter()
            Fermer tkinter et pygame
    """

    if tkinter.messagebox.askyesno("Quitter 2048", "Voulez-vous vraiment quitter ?"): # Demande de confirmation
        fenetre.destroy() # Fermer la fenêtre
        pygame.mixer.quit() # Fermeture de pygame
        exit() # Quitter le programme

def Minimiser():
    """
        Minimiser()
            Minimiser la fenêtre
    """

    global minimiser # On récupère la variable minimiser
    fenetre.overrideredirect(False) # Désactiver overrideredirect
    fenetre.iconify() # Minimiser la fenêtre
    minimiser=0 # Réinitialisation de minimiser

def Agrandir(event):
    """
        Agrandir(event)
            Agrandir la fenêtre
    """

    global minimiser # On récupère la variable minimiser
    minimiser+=1 # On incrémente de 1 minimiser
    if minimiser==2: # Si minimiser est à 2 (2 car quand on a miniser la fenêtre cette fonction s'est exécuté, alors qu'on veut qu'elle s'éxcute que lorsque l'on a cliqué sur la fentêtre dans la barre des taches)
        minimiser=0 # Réinitialisation de minimiser
        fenetre.deiconify() # Agrandissement de la fenêtre
        fenetre.overrideredirect(True) # Remettre overriderdirect

def Son():
    """
        Son()
            Initialise ou éteint pygame.mixer en fonction de la variable paremetreSon
    """

    # Si parametreSon est à True
    if paremetreSon.get():
        pygame.mixer.init() # Initialisation de pygame.mixer
    else: # Sinon
        pygame.mixer.quit() # Arrêt de pygame.mixer

def JouerSon(son):
    """
        JouerSon(son : string)
            Jouer le son donné
    """

    # Si parametreSon est à True
    if paremetreSon.get():
        pygame.mixer.music.load(son) # Chargement du son
        pygame.mixer.music.play(loops=0) # Jouer le son

def AfficherJeu():
    """
        AfficherJeu()
        Sortie :
            Affiche le tableau avec 4 lignes et forme la fenêtre
    """
    global score
    #print(" ")
    for i in range(4):
        # Afficher les 4 lignes
        #print(TableauJeu[i])

        # Création des images
        for j in range(4): 
            Img[i][j]=AfficherImage(TableauJeu[i][j], taille) # Création des images
            if nbDeplacement!=0: # Si le joueur a déplacé au moins une case
                Case[i][j].grid_forget() # Supprimer la case dans la grille de la fenêtre
            Case[i][j]=tkinter.Label(fenetre, image=Img[i][j], bg ="#4d4d4d") # Créer la case
            Case[i][j].grid(row=i+6, column=j) # Placer la case dans la grille de la fenêtre

    # Calculer la somme du tableau
    sommeTableau=sum(TableauJeu[0])+sum(TableauJeu[1])+sum(TableauJeu[2])+sum(TableauJeu[3])

    # Afficher le nombre de déplacement
    nbDeplacementLabel=tkinter.Label(
        fenetre, text=f"  Nombre de déplacement : {nbDeplacement}\t\t", bg ="#4d4d4d", fg="white", font=("Helvetica", 10, "bold"))
    nbDeplacementLabel.grid(
        row=2, column=0, columnspan=4, sticky="w") # Placer le label dans la grille de la fenêtre

    # Afficher le score
    scoreLabel=tkinter.Label(
        fenetre, text=f"  Score : {score}\t\t", bg ="#4d4d4d", fg="white", font=("Helvetica", 10, "bold"))
    scoreLabel.grid(
        row=3, column=0, columnspan=4, sticky="w") # Placer le label dans la grille de la fenêtre

    # Afficher la somme du tableau
    sommeTableauLabel=tkinter.Label(
        fenetre, text=f"  Somme du tableau : {sommeTableau}\t\t", bg ="#4d4d4d", fg="white", font=("Helvetica", 10, "bold"))
    sommeTableauLabel.grid(
        row=4, column=0, columnspan=4, sticky="w") # Placer le label dans la grille de la fenêtre

def Recommencer():
    """
        Recommencer():
            Recommencer le jeu
    """

    # Variables globales
    global nbDeplacement
    global perdu
    global score

    # Remettre à zéro les tableaux
    for i in range(4):

        for j in range(4):
            Case[i][j].grid_forget() # Supprimer la case dans la grille de la fenêtre
        
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
    caseDebut=0
    while caseDebut<2:
        x,y=TuileAléatoire()
        if TableauJeu[y][x]==0:
            TableauJeu[y][x]=2
            caseDebut+=1

    # Afficher le jeu
    AfficherJeu()

def Appuyer(event):
    """
        Appuyer(event : event)
            Fonction utilisée en jeu
    """

    # Variables globales
    global perdu
    global gagne
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
        #print("Game Over !")
        #print("Nombre de déplacement", ":", nbDeplacement)
        JouerSon("Audio/Perdu.mp3")
        if tkinter.messagebox.showinfo("Perdu", "Vous avez perdu !"):
            Recommencer()

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
                JouerSon("Audio/Fusion.mp3") # Jouer le son de la fusion
                score+=scoreGauche # Ajouter le score de la fusion
            else:
                JouerSon("Audio/Deplacement.mp3") # Jouer le son du déplacement

        # 38 Flèche haut
        # 90 Z
        # 104 Pavé numérique haut
        elif (keycode==38 or keycode==90 or keycode==104) and (deplacementHaut or fusionHaut):
            mouvement.haut(TableauJeu)
            deplacementFait=True

            if fusionHaut:
                JouerSon("Audio/Fusion.mp3") # Jouer le son de la fusion
                score+=scoreHaut # Ajouter le score de la fusion
            else:
                JouerSon("Audio/Deplacement.mp3") # Jouer le son du déplacement

        # 39 Flèche droite
        # 68 D
        # 102 Pavé numérique droite
        elif (keycode==39 or keycode==68 or keycode==102) and (deplacementDroite or fusionDroite):
            mouvement.droite(TableauJeu)
            deplacementFait=True

            if fusionDroite:
                JouerSon("Audio/Fusion.mp3") # Jouer le son de la fusion
                score+=scoreDroite # Ajouter le score de la fusion
            else:
                JouerSon("Audio/Deplacement.mp3") # Jouer le son du déplacement

        # 40 Flèche bas
        # 83 S
        # 98 Pavé numérique bas
        elif (keycode==40 or keycode==83 or keycode==98) and (deplacementBas or fusionBas):
            mouvement.bas(TableauJeu)
            deplacementFait=True

            if fusionBas:
                JouerSon("Audio/Fusion.mp3") # Jouer le son de la fusion
                score+=scoreBas # Ajouter le score de la fusion
            else:
                JouerSon("Audio/Deplacement.mp3") # Jouer le son du déplacement

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
        if 2048 in TableauJeu[i] and not gagne:
            # Son lorsque gagné
            JouerSon("Audio/Gagne.mp3")
            # Message de victoire
            tkinter.messagebox.showinfo("Gagné", "Vous avez gagné !")
            # Demande à l'utilisateur si recommencer
            if tkinter.messagebox.askyesno("Recommencer", "Voulez-vous recommencer ?"):
                Recommencer()
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
caseDebut=0
while caseDebut<2:
    x,y=TuileAléatoire()
    if TableauJeu[y][x]==0:
        TableauJeu[y][x]=2
        caseDebut+=1

# Lancer la fonction TailleFenêtre pour avoir la taille de la fenêtre qu'on demande à l'utilisateur
taille=TailleFenetre()

# Lancer la fenêtre Tkinter
fenetre = tkinter.Tk()

# Paramètre de la fenêtre
fenetre.iconbitmap("2048.ico") # Îcone de la fenêtre
fenetre.title("2048") # Nom de la fenêtre
fenetre.resizable(False, False) # Non redimensionnement de la fenêtre
fenetre.geometry("+100+100") # Position de la fenêtre

# Enlever barre windows
fenetre.overrideredirect(True)
fenetre.attributes("-topmost", True) # Fenêtre au premier plan
# Barre titre pour changer la barre windows originale
barreTitre=tkinter.Frame(fenetre, bg="#3C3C3C", borderwidth=1)
barreTitre.grid(row=0, columnspan=4, sticky="nsew")
barreTitre.bind("<ButtonPress-1>", BougerFenetreCommence)
barreTitre.bind("<ButtonRelease-1>", BougerFenetreArrete)
barreTitre.bind("<B1-Motion>", BougerFenetre)
# Titre dans la barre titre
titre=tkinter.Label(fenetre, text="  2048", bg="#3C3C3C", fg="white")
titre.grid(row=0, column=1, columnspan=2)
titre.bind("<ButtonPress-1>", BougerFenetreCommence)
titre.bind("<ButtonRelease-1>", BougerFenetreArrete)
titre.bind("<B1-Motion>", BougerFenetre)
        
# Bouton fermer et minimiser dans la barre titre
boutonFermerMinimiserFrame=tkinter.Frame(fenetre, bg="#3C3C3C", borderwidth=2)
boutonFermerMinimiserFrame.grid(row=0, columnspan=4, sticky="ne")
boutonFermer=tkinter.Button(
    boutonFermerMinimiserFrame, text="    X    ", command=Quitter, bg="#3C3C3C", fg="white", activebackground="#D71526",
    activeforeground="white", borderwidth=0, font=("Arial", 12))
boutonFermer.grid(row=0, column=1, sticky="ne")
boutonFermer.bind("<Enter>", EnterBoutonFermer)
boutonFermer.bind("<Leave>", LeaveBoutonFermer)
boutonMinimiser=tkinter.Button(
    boutonFermerMinimiserFrame, text="    —    ", command=Minimiser, bg="#3C3C3C", fg="white", activebackground="#505050", 
    activeforeground="white", borderwidth=0, font=("Arial", 12))
boutonMinimiser.grid(row=0, column=0, sticky="ne")
boutonMinimiser.bind("<Enter>", EnterBoutonMinimiser)
boutonMinimiser.bind("<Leave>", LeaveBoutonMinimiser)
fenetre.bind("<Map>", Agrandir)
# Icone dans la barre titre
icone = Image.open("2048.ico")
icone = icone.resize((16, 16))
icone = ImageTk.PhotoImage(icone)
label = tkinter.Label(barreTitre, image=icone, bg="#3C3C3C")
label.grid(row=0, column=0, padx=5, pady=5)
label.bind("<ButtonPress-1>", BougerFenetreCommence)
label.bind("<ButtonRelease-1>", BougerFenetreArrete)
label.bind("<B1-Motion>", BougerFenetre)
# Création de l"onglet Menu
menu = tkinter.Menubutton(
    barreTitre, text="Menu", bg="#3C3C3C", activebackground="#505050", activeforeground="white", foreground="white")
menu.grid(row=0, column=1)
# Création d"un menu défilant
menuDeroulant = tkinter.Menu(
    menu, background="#4d4d4d", foreground="#ffffff", tearoff=0, activebackground="#094771")
# Ajouter un checkbutton au menu
paremetreSon=tkinter.BooleanVar()
paremetreSon.set(True)
menuDeroulant.add_checkbutton(
    label="Son", onvalue=True, offvalue=False, variable=paremetreSon, command=Son())
# Ajouter bouton Recommencer au menu
menuDeroulant.add_command(
    label="Recommencer", command=Recommencer)
# Ajouter un séparateur
menuDeroulant.add_separator()
# Ajouter minimiser quitter au menu
menuDeroulant.add_command(
    label="Minimiser", command=Minimiser)
# Ajouter bouton quitter au menu
menuDeroulant.add_command(
    label="Quitter", command=Quitter)
# Ajouter un séparateur
menuDeroulant.add_separator()
# Ajouter un bouton à propos au menu
menuDeroulant.add_command(
    label="À propos", command = lambda:[tkinter.messagebox.showinfo(
        "À propos", "2048 (Projet NSI GA.1)\n\nCréé par :\n\n- ING Bryan\n- ABASSE Tidiane\n- GALANG Andrei\n\nVersion : 5.0 (S5)"
        )])
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
# Ajouter bouton Recommencer au menu
menu.add_command(label="Recommencer", command=Recommencer)
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

# Afficher le tableau
AfficherJeu()

# Espacement entre les cases
for i in range(4):
    fenetre.grid_columnconfigure(i, minsize=taille)
    fenetre.grid_rowconfigure(i+6, minsize=taille)

# Couleur de fond fond
fenetre.configure(background = "#4d4d4d")

# Exécution de la fonction "Quitter" lors de lors du click de fermeture de la fenêtre
fenetre.protocol("WM_DELETE_WINDOW", Quitter)

# Détecter les touches appuyées
fenetre.bind_all("<Key>",Appuyer)

# Détecte KeyboardInterrupt
signal.signal(signal.SIGINT, sigint_handler)

# Mainloop
fenetre.mainloop()

