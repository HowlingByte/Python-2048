# Importation des bibliothèques
import tkinter
import tkinter.messagebox
import copy
import pygame
import signal
from PIL import Image, ImageTk
import time

# Importation des fichiers .py du dossier python
import mouvement
from autresfonctions2048 import *
from taillefenetre import *

# Initialisation des variables
TableauJeu = \
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
Case = \
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
Img = \
[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
nbDeplacement = 0
perdu = False
gagne = False
minimiser = False
jouer = True

def ReinitialiserScore():
    """
        ReinitialiserScore()
            Reinitialiser le record
    """
    fichierEcrire = open("record.txt", "w") # On ouvre le fichier record.txt en écriture
    fichierEcrire.write("0") # On écrit 0 dans le fichier
    fichierEcrire.close() # On ferme le fichier
    AfficherJeu()

def FenetreFocusIn(event):
    """
        FenetreFocusIn(event)
            Fonction qui permet de mettre à jour la couleur de la fenêtre lorsqu'on a le focus sur la fênetre
    """
    
    barreTitre.configure(bg = gris3)
    titre.configure(bg = gris3, fg = blanc)
    boutonFermerMinimiserFrame.configure(bg = gris3)
    boutonFermer.configure(bg = gris3, fg = blanc)
    boutonMinimiser.configure(bg = gris3, fg = blanc)
    label.configure(bg = gris3)
    menu.configure(bg = gris3, fg = blanc)
    menuDeroulant.configure(bg = gris3, fg = blanc)
    fenetre.configure(bg = gris2)
    recordLabel.configure(bg = gris2, fg = blanc)
    nbDeplacementLabel.configure(bg = gris2, fg = blanc)
    sommeTableauLabel.configure(bg = gris2, fg = blanc)
    timerLabel.configure(bg = gris2, fg = blanc)
    for i in range(4):
        for j in range(4): 
            Case[i][j].configure(bg = gris2)

def FenetreFocusOut(event):
    """
        FenetreFocusOut(event)
            Fonction qui permet de mettre à jour la couleur de la fenêtre lorsqu'on n'a plus le focus sur la fênetre
    """

    barreTitre.configure(bg = gris4)
    titre.configure(bg = gris4, fg = gris1)
    boutonFermerMinimiserFrame.configure(bg = gris4)
    boutonFermer.configure(bg = gris4, fg = gris1)
    boutonMinimiser.configure(bg = gris4, fg = gris1)
    label.configure(bg = gris4)
    menu.configure(bg = gris4, fg = gris1)
    menuDeroulant.configure(bg = gris4, fg = gris1)
    fenetre.configure(bg = gris3)
    recordLabel.configure(bg = gris3, fg = gris1)
    nbDeplacementLabel.configure(bg = gris3, fg = gris1)
    sommeTableauLabel.configure(bg = gris3, fg = gris1)
    timerLabel.configure(bg = gris3, fg = gris1)
    for i in range(4):
        for j in range(4): 
            Case[i][j].configure(bg = gris3)
            
def Timer(i, label):
    """
        Timer(i, label)
            Fonction qui permet de mettre à jour le label timerLabel
        Entrée :
            i : temps en seconde
            label : label qui contient le temps
    """

    minute = (f"0{i//60}"[-2:]) # On récupère les minutes
    seconde = (f"0{i%60}"[-2:]) # On récupère les secondes
    label.set(f"  Timer : {minute}:{seconde}") # On met à jour le label
    i = round(time.time() - tempsDebut) # On met à jour le temps
    fenetre.after(1000, lambda: [Timer(i, label)]) # On rappelle la fonction Timer() après 1 seconde

def Focus(event):
    """
        Focus(event)
            Fonction qui permet de récupérer le focus de la fenêtre
    """

    fenetre.focus_get() # On récupère le focus de la fenêtre
    fenetre.lift() # On remonte la fenêtre
    FenetreFocusIn(None)

def Minimiser(event): 
    """
        Minimiser(event)
            Minimiser la fenêtre
    """

    fenetre.withdraw()

def Agrandir(event):
    """
        Agrandir(event)
            Agrandir la fenêtre
    """

    fenetre.deiconify()

def Sigint_handler(signal, frame):
    """
        Sigint_handler(signal, frame)
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

    if tkinter.messagebox.askyesno("Quitter 2048", "Voulez-vous vraiment quitter ?", icon="question"): # Demande de confirmation
        fenetre.destroy() # Fermer la fenêtre
        pygame.mixer.quit() # Fermeture de pygame
        exit() # Quitter le programme

def Son():
    """
        Son()
            Initialise ou éteint pygame.mixer en fonction de la variable parametreSon
    """

    # Si parametreSon est à True
    if parametreSon.get():
        pygame.mixer.init() # Initialisation de pygame.mixer
    else: # Sinon
        pygame.mixer.quit() # Arrêt de pygame.mixer

def JouerSon(son):
    """
        JouerSon(son : string)
            Jouer le son donné
    """

    # Si parametreSon est à True
    if parametreSon.get():
        pygame.mixer.music.load(son) # Chargement du son
        pygame.mixer.music.play(loops = 0) # Jouer le son

def AfficherJeu():
    """
        AfficherJeu()
        Sortie :
            Affiche le tableau avec 4 lignes et forme la fenêtre
    """

    for i in range(4):

        # Création des images
        for j in range(4): 
            Img[i][j] = AfficherImage(TableauJeu[i][j], taille) # Création des images
            Case[i][j].configure(image = Img[i][j])
            Case[i][j].image = Img[i][j]

    # Afficher le nombre de déplacement
    nbDeplacementVar.set(f"  Nombre de déplacement : {nbDeplacement}")

    # Afficher le score (somme du tableau)
    sommeTableau = sum(TableauJeu[0]) + sum(TableauJeu[1]) + sum(TableauJeu[2]) + sum(TableauJeu[3])
    sommeTableauVar.set(f"  Score : {sommeTableau}")

    # Afficher le record
    fichierLire = open("record.txt", "r")
    record = int(fichierLire.read())
    fichierLire.close()
    if sommeTableau>record:
        fichierEcrire = open("record.txt", "w")
        fichierEcrire.write(str(sommeTableau))
        fichierEcrire.close()
        record = sommeTableau
    recordVar.set(f"  Record score : {record}")

def Recommencer():
    """
        Recommencer():
            Recommencer le jeu
    """

    # Variables globales
    global nbDeplacement
    global perdu
    global tempsDebut

    # Remettre à zéro le tableau
    for i in range(4):
        TableauJeu[i] = [0, 0, 0, 0]

    # Remettre à zéro le nombre de déplacement
    nbDeplacement = 0
    # Remettre à zéro la variable perdu
    perdu = False
    # Remettre à zéro le temps de départ
    tempsDebut = time.time()

    # Boucle pour mettre deux cases de 2 dans le tableau
    caseDebut = 0
    while caseDebut<2:
        x,y = TuileAleatoire()
        if TableauJeu[y][x] == 0:
            TableauJeu[y][x] = 2
            caseDebut += 1

    # Afficher le jeu
    AfficherJeu()

def Appuyer(event):
    """
        Appuyer(event)
            Fonction utilisée en jeu
    """

    # Variables globales
    global perdu
    global gagne
    global nbDeplacement
    global jouer

    # Variables locales
    caseVide = False
    deplacement = False
    deplacementPossible = False
    deplacementFait = False

    # Test si case vide donc déplacement possible
    for i in range(0,4):
        for j in range(0,4):
            if TableauJeu[i][j] == 0:
                caseVide = True
                deplacementPossible = True


    # Test si seulement déplacement possible
    TableauJeuTempGauche = copy.deepcopy(TableauJeu)
    deplacementGauche, fusionGauche = mouvement.gauche(TableauJeuTempGauche)

    TableauJeuTempHaut = copy.deepcopy(TableauJeu)
    deplacementHaut, fusionHaut = mouvement.haut(TableauJeuTempHaut)

    TableauJeuTempDroite = copy.deepcopy(TableauJeu)
    deplacementDroite, fusionDroite = mouvement.droite(TableauJeuTempDroite)

    TableauJeuTempBas = copy.deepcopy(TableauJeu)
    deplacementBas, fusionBas = mouvement.bas(TableauJeuTempBas)

    if deplacementGauche or deplacementHaut or deplacementDroite or deplacementBas or fusionGauche or fusionHaut or fusionDroite or fusionBas:
        deplacementPossible = True

    # Si déplacement impossible, perdu
    if not deplacementPossible and not perdu and jouer:
        perdu = True
        JouerSon("Audio/Perdu.mp3")
        jouer = False
        if tkinter.messagebox.showinfo("Perdu", f"Vous avez perdu !\n{nbDeplacementVar.get()}\n{sommeTableauVar.get()}\n{timer.get()}", icon = "info"):
            Recommencer()
            jouer = True

    elif deplacementPossible and jouer:

        # Récupérer keycode de la touche appuyée
        keycode = (event.keycode)

        # 37 Flèche gauche
        # 81 Q
        # 100 Pavé numérique gauche
        if (keycode == 37 or keycode == 81 or keycode == 100) and (deplacementGauche or fusionGauche) and TableauJeu != TableauJeuTempGauche:
            mouvement.gauche(TableauJeu)
            deplacementFait=True

            if fusionGauche:
                JouerSon("Audio/Fusion.mp3") # Jouer le son de la fusion
            else:
                JouerSon("Audio/Deplacement.mp3") # Jouer le son du déplacement

        # 38 Flèche haut
        # 90 Z
        # 104 Pavé numérique haut
        elif (keycode == 38 or keycode == 90 or keycode == 104) and (deplacementHaut or fusionHaut) and TableauJeu != TableauJeuTempHaut:
            mouvement.haut(TableauJeu)
            deplacementFait=True

            if fusionHaut:
                JouerSon("Audio/Fusion.mp3") # Jouer le son de la fusion
            else:
                JouerSon("Audio/Deplacement.mp3") # Jouer le son du déplacement

        # 39 Flèche droite
        # 68 D
        # 102 Pavé numérique droite
        elif (keycode == 39 or keycode == 68 or keycode == 102) and (deplacementDroite or fusionDroite) and TableauJeu != TableauJeuTempDroite:
            mouvement.droite(TableauJeu)
            deplacementFait=True

            if fusionDroite:
                JouerSon("Audio/Fusion.mp3") # Jouer le son de la fusion
            else:
                JouerSon("Audio/Deplacement.mp3") # Jouer le son du déplacement

        # 40 Flèche bas
        # 83 S
        # 98 Pavé numérique bas
        elif (keycode == 40 or keycode == 83 or keycode == 98) and (deplacementBas or fusionBas) and TableauJeu != TableauJeuTempBas:
            mouvement.bas(TableauJeu)
            deplacementFait = True

            if fusionBas:
                JouerSon("Audio/Fusion.mp3") # Jouer le son de la fusion
            else:
                JouerSon("Audio/Deplacement.mp3") # Jouer le son du déplacement

    if caseVide and deplacementFait:
        # Faire apparaître une nouvelle case de 2
        while not deplacement:
            x,y=TuileAleatoire()
            if TableauJeu[y][x] == 0:
                TableauJeu[y][x] = 2
                deplacement = True

        # Ajouter 1 au compteur d'étape
        nbDeplacement += 1

    # Valeur du tableau "TableauJeu" dans la fenêtre
    AfficherJeu()

    # Test si 2048 est atteint
    for i in range(4):
        if 2048 in TableauJeu[i] and not gagne and jouer:
            jouer = False
            gagne = True
            # Son lorsque gagné
            JouerSon("Audio/Gagne.mp3")
            # Message de victoire
            tkinter.messagebox.showinfo("Gagné", f"Vous avez gagné !\n{nbDeplacementVar.get()}\n{sommeTableauVar.get()}\n{timer.get()}", icon = "info")
            # Demande à l'utilisateur si recommencer
            if not tkinter.messagebox.askyesno("Continuer", "Voulez-vous continuez ?", icon = "question"):
                Recommencer()
                jouer = True
            else:
                jouer = True

# Main
# Boucle pour mettre deux cases de 2 dans le tableau
caseDebut = 0
while caseDebut<2:
    x,y = TuileAleatoire()
    if TableauJeu[y][x] == 0:
        TableauJeu[y][x] = 2
        caseDebut += 1

# Lancer la fonction TailleFenêtre pour avoir la taille de la fenêtre qu'on demande à l'utilisateur
taille=TailleFenetre()

# Lancer la fenêtre Tkinter
root = tkinter.Tk()
root.attributes("-alpha",0.0)
root.bind("<Unmap>", Minimiser)
root.bind("<Map>", Agrandir)
fenetre = tkinter.Toplevel(root)

root.iconbitmap("2048.ico") # Îcone de la fenêtre
root.title("2048") # Nom de la fenêtre

# Paramètre de la fenêtre
fenetre.iconbitmap("2048.ico") # Îcone de la fenêtre
fenetre.title("2048") # Nom de la fenêtre
fenetre.resizable(False, False) # Non redimensionnement de la fenêtre
fenetre.geometry("+0+0") # Position de la fenêtre

# Enlever barre windows
fenetre.overrideredirect(True)
#fenetre.attributes("-topmost", True) # Fenêtre au premier plan

# Barre titre pour changer la barre windows originale
barreTitre = tkinter.Frame(fenetre, bg = gris3, borderwidth = 1)
barreTitre.grid(row = 0, columnspan = 4, sticky = "nsew")
barreTitre.bind("<ButtonPress-1>", BougerFenetreCommence)
barreTitre.bind("<ButtonRelease-1>", BougerFenetreArrete)
barreTitre.bind("<B1-Motion>", BougerFenetre)

# Titre dans la barre titre
titre = tkinter.Label(fenetre, text = "  2048", bg = gris3, fg = "white")
titre.grid(row = 0, column = 1, columnspan = 2)
titre.bind("<ButtonPress-1>", BougerFenetreCommence)
titre.bind("<ButtonRelease-1>", BougerFenetreArrete)
titre.bind("<B1-Motion>", BougerFenetre)
        
# Bouton fermer et minimiser dans la barre titre
boutonFermerMinimiserFrame = tkinter.Frame(fenetre, bg = gris3, borderwidth = 2)
boutonFermerMinimiserFrame.grid(row = 0, columnspan = 4, sticky = "ne")
boutonFermer = tkinter.Button(
    boutonFermerMinimiserFrame, text = "    X    ", command = Quitter, bg = gris3, fg = "white", activebackground = rouge,
    activeforeground = "white", borderwidth = 0, font = ("Arial", 12)
)
boutonFermer.grid(row = 0, column = 1, sticky = "ne")
boutonFermer.bind("<Enter>", EnterBoutonFermer)
boutonFermer.bind("<Leave>", LeaveBoutonFermer)
boutonMinimiser = tkinter.Button(
    boutonFermerMinimiserFrame, text = "    —    ", command = lambda:[fenetre.withdraw(), root.iconify()], bg = gris3, fg = "white", activebackground = gris1, 
    activeforeground = "white", borderwidth = 0, font = ("Arial", 12)
)
boutonMinimiser.grid(row = 0, column = 0, sticky = "ne")
boutonMinimiser.bind("<Enter>", EnterBoutonMinimiser)
boutonMinimiser.bind("<Leave>", LeaveBoutonMinimiser)

# Icone dans la barre titre
icone = Image.open("2048.ico")
icone = icone.resize((16, 16))
icone = ImageTk.PhotoImage(icone)
label = tkinter.Label(barreTitre, image = icone, bg = gris3)
label.grid(row = 0, column = 0, padx = 5, pady = 5)
label.bind("<ButtonPress-1>", BougerFenetreCommence)
label.bind("<ButtonRelease-1>", BougerFenetreArrete)
label.bind("<B1-Motion>", BougerFenetre)

# Création de l"onglet Menu
menu = tkinter.Menubutton(
    barreTitre, text = "Menu", bg = gris3, activebackground = gris1, activeforeground = "white", foreground = "white"
)
menu.grid(row = 0, column = 1)

# Création d"un menu défilant
menuDeroulant = tkinter.Menu(
    menu, background = gris2, foreground = blanc, tearoff = 0, activebackground = bleu3
)

# Ajouter un checkbutton au menu
parametreSon = tkinter.BooleanVar()
parametreSon.set(True)
menuDeroulant.add_checkbutton(
    label = "Son", onvalue = True, offvalue = False, variable = parametreSon, command = Son()
)

# Ajouter bouton Recommencer au menu
menuDeroulant.add_command(
    label = "Recommencer", command = Recommencer
)

# Ajouter bouton Reinitialiser score au menu
menuDeroulant.add_command(
    label = "Reinitialiser score", command = ReinitialiserScore
)

# Ajouter un séparateur
menuDeroulant.add_separator()

# Ajouter minimiser quitter au menu
menuDeroulant.add_command(
    label = "Minimiser", command = lambda:[fenetre.withdraw(), root.iconify()]
)

# Ajouter bouton quitter au menu
menuDeroulant.add_command(
    label = "Quitter", command = Quitter)

# Ajouter un séparateur
menuDeroulant.add_separator()

# Ajouter un bouton à propos au menu
menuDeroulant.add_command(
    label = "À propos", command = lambda:[tkinter.messagebox.showinfo(
            "À propos", "Python-2048\n\nCréé par :\n\n- Ryse93\n\nVersion : 10.0 (S10)", icon = "info"
        )
    ]
)

# Attribution du menu déroulant au menu Affichage
menu.configure(menu = menuDeroulant)

# Label cases
for i in range(4):
    for j in range(4): 
        Img[i][j] = AfficherImage(TableauJeu[i][j], taille) # Création des images
        Case[i][j] = tkinter.Label(fenetre, image = Img[i][j], bg = gris2) # Créer la case
        Case[i][j].grid(row = i+6, column = j) # Placer la case dans la grille de la fenêtre

# Label record
recordVar = tkinter.StringVar()
recordLabel = tkinter.Label(fenetre, textvariable = recordVar, bg = gris2, fg = "white", font = ("Helvetica", 10, "bold"))
recordLabel.grid(
    row = 2, column = 0, columnspan = 4, sticky = "w"
)

# Label nbDeplacement
nbDeplacementVar = tkinter.StringVar()
nbDeplacementVar.set(f"  Nombre de déplacement : {nbDeplacement}")
nbDeplacementLabel = tkinter.Label(
    fenetre, textvariable = nbDeplacementVar, bg = gris2, fg = "white", font = ("Helvetica", 10, "bold")
)
nbDeplacementLabel.grid(
    row = 3, column = 0, columnspan = 4, sticky = "w"
) 

# Label sommeTableau (score)
sommeTableauVar = tkinter.StringVar()
sommeTableauVar.set(f"  Score : {0}")
sommeTableauLabel = tkinter.Label(fenetre, textvariable = sommeTableauVar, bg = gris2, fg = "white", font = ("Helvetica", 10, "bold"))
sommeTableauLabel.grid(
    row = 4, column = 0, columnspan = 4, sticky = "w"
)

# Timers
tempsDebut = time.time()
temps = round(time.time() - tempsDebut)
timer = tkinter.StringVar()
timer.set(temps)
timerLabel = tkinter.Label(fenetre, textvariable = timer, bg = gris2, fg = "white", font = ("Helvetica", 10, "bold"))
timerLabel.grid(
    row = 5, column = 0, columnspan = 4, sticky = "w"
)
Timer(temps, timer)

# Afficher le tableau
AfficherJeu()

# Espacement entre les cases
for i in range(4):
    fenetre.grid_columnconfigure(i, minsize = taille)
    fenetre.grid_rowconfigure(i+6, minsize = taille)

# Couleur de fond fond
fenetre.configure(background = gris2)

# Exécution de la fonction "Quitter" lors de lors du click de fermeture de la fenêtre
fenetre.protocol("WM_DELETE_WINDOW", Quitter)

# Détecter les touches appuyées
fenetre.bind_all("<KeyRelease>",Appuyer)

# Détecte KeyboardInterrupt
signal.signal(signal.SIGINT, Sigint_handler)

# Fenêtre au premier plan avec le focus
fenetre.focus_force()
fenetre.lift()

# Détecter lorsqu'on a le focus ou pas
root.bind("<FocusIn>", Focus)
root.bind("<FocusOut>", FenetreFocusOut)
fenetre.bind("<FocusIn>", FenetreFocusIn)
fenetre.bind("<FocusOut>", FenetreFocusOut)

# Mainloop
fenetre.mainloop()
