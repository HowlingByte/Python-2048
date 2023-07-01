"""
main.py
    Fichier qui contient le code du jeu 2048
    Auteur : Ahhj93
"""

# Importation des bibliothèques
import tkinter
import tkinter.messagebox
import copy
import signal
import time
import sys
import pygame
from PIL import Image, ImageTk

# Importation des fichiers .py du dossier python
import mouvement
from autres_fonctions import (
    GRIS1,
    GRIS2,
    GRIS3,
    GRIS4,
    BLEU3,
    ROUGE,
    BLANC,
    enter_bouton_fermer,
    leave_bouton_fermer,
    tuile_aleatoire,
    enter_bouton_minimiser,
    leave_bouton_minimiser,
    afficher_image,
)
from taille_fenetre import taille_fenetre

# Start- Discord RPC
try:
    from pypresence import Presence

    RPC_MODULE = True
    CLIENT_ID = "1111927811419164682"
    RPC = Presence(CLIENT_ID)
    RPC.connect()
except ModuleNotFoundError:
    RPC_MODULE = False
    print("Module pypresence not found so the Discord RPC is not working")
# End- Discord RPC

# Initialisation des variables
TableauJeu = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
Case = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
Img = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
NB_DEPLACEMENT = 0
PERDU = False
GAGNER = False
JOUER = True

X: int | None = None
Y: int | None = None


def reinitialiser_score():
    """
    reinitialiser_score()
        Reinitialiser le record
    """
    fichier_ecrire = open(
        "record.txt", "w", encoding="utf-8"
    )  # On ouvre le fichier record.txt en écriture
    fichier_ecrire.write("0")  # On écrit 0 dans le fichier
    fichier_ecrire.close()  # On ferme le fichier
    afficher_jeu()


def fenetre_focus_in(_event):
    """
    fenetre_focus_in(_event)
        Fonction qui permet de mettre à jour la couleur de la fenêtre lorsqu'on a le focus sur la
        fênetre
    """

    barreTitre.configure(bg=GRIS3)
    titre.configure(bg=GRIS3, fg=BLANC)
    boutonFermerMinimiserFrame.configure(bg=GRIS3)
    boutonFermer.configure(bg=GRIS3, fg=BLANC)
    boutonMinimiser.configure(bg=GRIS3, fg=BLANC)
    label.configure(bg=GRIS3)
    menu.configure(bg=GRIS3, fg=BLANC)
    menuDeroulant.configure(bg=GRIS3, fg=BLANC)
    fenetre.configure(bg=GRIS2)
    recordLabel.configure(bg=GRIS2, fg=BLANC)
    nbDeplacementLabel.configure(bg=GRIS2, fg=BLANC)
    sommeTableauLabel.configure(bg=GRIS2, fg=BLANC)
    timerLabel.configure(bg=GRIS2, fg=BLANC)
    for case_y in range(4):
        for case_x in range(4):
            Case[case_y][case_x].configure(bg=GRIS2)  # type: ignore


def fenetre_focus_out(_event):
    """
    fenetre_focus_out(_event)
        Fonction qui permet de mettre à jour la couleur de la fenêtre lorsqu'on n'a plus le focus
        sur la fênetre
    """

    barreTitre.configure(bg=GRIS4)
    titre.configure(bg=GRIS4, fg=GRIS1)
    boutonFermerMinimiserFrame.configure(bg=GRIS4)
    boutonFermer.configure(bg=GRIS4, fg=GRIS1)
    boutonMinimiser.configure(bg=GRIS4, fg=GRIS1)
    label.configure(bg=GRIS4)
    menu.configure(bg=GRIS4, fg=GRIS1)
    menuDeroulant.configure(bg=GRIS4, fg=GRIS1)
    fenetre.configure(bg=GRIS3)
    recordLabel.configure(bg=GRIS3, fg=GRIS1)
    nbDeplacementLabel.configure(bg=GRIS3, fg=GRIS1)
    sommeTableauLabel.configure(bg=GRIS3, fg=GRIS1)
    timerLabel.configure(bg=GRIS3, fg=GRIS1)
    for case_y in range(4):
        for case_x in range(4):
            Case[case_y][case_x].configure(bg=GRIS3)  # type: ignore


def fonction_timer(temps_seconde, temps_label):
    """
    fonction_timer(i, label)
        Fonction qui permet de mettre à jour le label timerLabel
    Entrée :
        i : temps en seconde
        label : label qui contient le temps
    """

    minute = f"0{temps_seconde//60}"[-2:]  # On récupère les minutes
    seconde = f"0{temps_seconde%60}"[-2:]  # On récupère les secondes
    temps_label.set(f"  Timer : {minute}:{seconde}")  # On met à jour le label
    temps_seconde = round(time.time() - TEMPS_DEBUT)  # On met à jour le temps

    if RPC_MODULE:
        somme_tableau = (
            sum(TableauJeu[0])
            + sum(TableauJeu[1])
            + sum(TableauJeu[2])
            + sum(TableauJeu[3])
        )
        plus_grand_nombre = max(
            *TableauJeu[0], *TableauJeu[1], *TableauJeu[2], *TableauJeu[3]
        )
        RPC.update(
            details="Un jeu de puzzle numérique addictif",
            state="Score : " + str(somme_tableau),
            start=TEMPS_DEBUT,
            large_image="logo",
            large_text="Python-2048",
            small_image=str(plus_grand_nombre),
            small_text="Plus grand nombre : " + str(plus_grand_nombre),
            buttons=[
                {"label": "GitHub", "url": "https://github.com/Ryse93/Python-2048"}
            ],
        )

    # On rappelle la fonction fonction_timer() après 1 seconde
    fenetre.after(1000, lambda: [fonction_timer(i, label)])


def focus(_event):
    """
    focus(_event)
        Fonction qui permet de récupérer le focus de la fenêtre
    """

    fenetre.focus_get()  # On récupère le focus de la fenêtre
    fenetre.lift()  # On remonte la fenêtre
    fenetre_focus_in(None)


def minimiser(_event):
    """
    minimiser(_event)
        Minimiser la fenêtre
    """

    fenetre.withdraw()


def agrandir(_event):
    """
    agrandir(_event)
        Agrandir la fenêtre
    """

    fenetre.deiconify()


def sigint_handler(_signal, _frame):
    """
    sigint_handler(_signal, _frame)
        Fonction qui permet de fermer la fenetre sans erreur lors du KeyboardInterrupt
    """

    fenetre.destroy()  # Fermer la fenêtre
    pygame.mixer.quit()  # Fermer pygame
    sys.exit()  # Quitter le programme


def bouger_fenetre_commence(event):
    """
    bouger_fenetre_commence(event)
        Fonction qui permet de récupérer la position de la souris au début du déplacement
    Entrée :
        event : événement
    """
    global X, Y  # pylint: disable=global-statement # On récupère les variables x et y
    X = event.x  # On récupère la position de la souris en x
    Y = event.y  # On récupère la position de la souris en y


def bouger_fenetre_arrete(_event):
    """
    bouger_fenetre_arrete(_event)
        Fonction qui permet de réinitialiser les variables x et y
    """
    global X, Y  # pylint: disable=global-statement # On récupère les variables x et y
    X = None  # On réinitialise x
    Y = None  # On réinitialise y


def bouger_fenetre(event):
    """
    bouger_fenetre(event)
        Fonction qui permet de bouger la fenêtre
    Entrée :
        event : événement
    Sortie :
        Bouge la fenêtre
    """

    global X, Y  # pylint: disable=W0602 # On récupère les variables x et y
    delta_x = (
        event.x - X
    )  # On calcule la différence entre la position de la souris et la position de la souris au début du déplacement
    delta_y = (
        event.y - Y
    )  # On calcule la différence entre la position de la souris et la position de la souris au début du déplacement
    a_x = (
        fenetre.winfo_x() + delta_x
    )  # On calcule la nouvelle position de la fenêtre en fonction de la différence entre la position de la souris et la position de la souris au début du déplacement
    a_y = (
        fenetre.winfo_y() + delta_y
    )  # On calcule la nouvelle position de la fenêtre en fonction de la différence entre la position de la souris et la position de la souris au début du déplacement
    fenetre.geometry(f"+{a_x}+{a_y}")  # On déplace la fenêtre


def quitter():
    """
    quitter()
        Fermer tkinter et pygame
    """

    # Demande de confirmation
    if tkinter.messagebox.askyesno(
        "Quitter 2048", "Voulez-vous vraiment quitter ?", icon="question"
    ):
        fenetre.destroy()  # Fermer la fenêtre
        pygame.mixer.quit()  # Fermeture de pygame
        sys.exit()  # Quitter le programme


def son():
    """
    son()
        Initialise ou éteint pygame.mixer en fonction de la variable parametreSon
    """

    # Si parametreSon est à True
    if parametreSon.get():
        pygame.mixer.init()  # Initialisation de pygame.mixer
    else:  # Sinon
        pygame.mixer.quit()  # Arrêt de pygame.mixer


def jouer_son(fichier_son: str):
    """
    jouer_son(son : string)
        Jouer le son donné
    """

    # Si parametreSon est à True
    if parametreSon.get():
        pygame.mixer.music.load(fichier_son)  # Chargement du son
        pygame.mixer.music.play(loops=0)  # Jouer le son


def afficher_jeu():
    """
    afficher_jeu()
    Sortie :
        Affiche le tableau avec 4 lignes et forme la fenêtre
    """

    for case_y in range(4):
        # Création des images
        for case_x in range(4):
            Img[case_y][case_x] = afficher_image(TableauJeu[case_y][case_x], taille)  # type: ignore # Création des images
            Case[case_y][case_x].configure(image=Img[case_y][case_x])  # type: ignore
            Case[case_y][case_x].image = Img[case_y][case_x]  # type: ignore

    # Afficher le nombre de déplacement
    nbDeplacementVar.set(f"  Nombre de déplacement : {NB_DEPLACEMENT}")

    # Afficher le score (somme du tableau)
    somme_tableau = (
        sum(TableauJeu[0])
        + sum(TableauJeu[1])
        + sum(TableauJeu[2])
        + sum(TableauJeu[3])
    )
    sommeTableauVar.set(f"  Score : {somme_tableau}")

    # Afficher le record
    fichier_lire = open("record.txt", "r", encoding="utf-8")
    record = int(fichier_lire.read())
    fichier_lire.close()
    if somme_tableau > record:
        fichier_ecrire = open("record.txt", "w", encoding="utf-8")
        fichier_ecrire.write(str(somme_tableau))
        fichier_ecrire.close()
        record = somme_tableau
    recordVar.set(f"  Record score : {record}")


def recommencer():
    """
    recommencer():
        Recommencer le jeu
    """

    # Variables globales
    global NB_DEPLACEMENT  # pylint: disable=global-statement
    global PERDU  # pylint: disable=global-statement
    global TEMPS_DEBUT  # pylint: disable=global-statement

    # Remettre à zéro le tableau
    for ligne in range(4):
        TableauJeu[ligne] = [0, 0, 0, 0]

    # Remettre à zéro le nombre de déplacement
    NB_DEPLACEMENT = 0
    # Remettre à zéro la variable perdu
    PERDU = False
    # Remettre à zéro le temps de départ
    TEMPS_DEBUT = int(time.time())

    # Boucle pour mettre deux cases de 2 dans le tableau
    case_debut = 0
    while case_debut < 2:
        random_x, random_y = tuile_aleatoire()
        if TableauJeu[random_y][random_x] == 0:
            TableauJeu[random_y][random_x] = 2
            case_debut += 1

    # Afficher le jeu
    afficher_jeu()


def appuyer(event):
    """
    appuyer(event)
        Fonction utilisée en jeu
    """

    # Variables globales
    global PERDU  # pylint: disable=global-statement
    global GAGNER  # pylint: disable=global-statement
    global NB_DEPLACEMENT  # pylint: disable=global-statement
    global JOUER  # pylint: disable=global-statement

    # Variables locales
    case_vide = False
    deplacement = False
    deplacement_possible = False
    deplacement_fait = False

    # Test si case vide donc déplacement possible
    for case_y in range(0, 4):
        for case_x in range(0, 4):
            if TableauJeu[case_y][case_x] == 0:
                case_vide = True
                deplacement_possible = True

    # Test si seulement déplacement possible
    tableau_jeu_temp_gauche = copy.deepcopy(TableauJeu)
    deplacement_gauche, fusion_gauche = mouvement.Gauche(tableau_jeu_temp_gauche)

    tableau_jeu_temp_haut = copy.deepcopy(TableauJeu)
    deplacement_haut, fusion_haut = mouvement.Haut(tableau_jeu_temp_haut)

    tableau_jeu_temp_droite = copy.deepcopy(TableauJeu)
    deplacement_droite, fusion_droite = mouvement.Droite(tableau_jeu_temp_droite)

    tableau_jeu_temp_bas = copy.deepcopy(TableauJeu)
    deplacement_bas, fusion_bas = mouvement.Bas(tableau_jeu_temp_bas)

    if (
        deplacement_gauche
        or deplacement_haut
        or deplacement_droite
        or deplacement_bas
        or fusion_gauche
        or fusion_haut
        or fusion_droite
        or fusion_bas
    ):
        deplacement_possible = True

    # Si déplacement impossible, perdu
    if not deplacement_possible and not PERDU and JOUER:
        PERDU = True
        jouer_son("Audio/Perdu.mp3")
        JOUER = False
        if tkinter.messagebox.showinfo(
            "Perdu",
            f"Vous avez perdu !\n{nbDeplacementVar.get()}\n{sommeTableauVar.get()}\n{timer.get()}",
            icon="info",
        ):
            recommencer()
            JOUER = True

    elif deplacement_possible and JOUER:
        # Récupérer keycode de la touche appuyée
        keycode = event.keycode

        # 37 Flèche gauche
        # 81 Q
        # 100 Pavé numérique gauche
        if (
            (keycode == 37 or keycode == 81 or keycode == 100)
            and (deplacement_gauche or fusion_gauche)
            and TableauJeu != tableau_jeu_temp_gauche
        ):
            mouvement.Gauche(TableauJeu)
            deplacement_fait = True

            if fusion_gauche:
                jouer_son("Audio/Fusion.mp3")  # Jouer le son de la fusion
            else:
                # Jouer le son du déplacement
                jouer_son("Audio/Deplacement.mp3")

        # 38 Flèche haut
        # 90 Z
        # 104 Pavé numérique haut
        elif (
            (keycode == 38 or keycode == 90 or keycode == 104)
            and (deplacement_haut or fusion_haut)
            and TableauJeu != tableau_jeu_temp_haut
        ):
            mouvement.Haut(TableauJeu)
            deplacement_fait = True

            if fusion_haut:
                jouer_son("Audio/Fusion.mp3")  # Jouer le son de la fusion
            else:
                # Jouer le son du déplacement
                jouer_son("Audio/Deplacement.mp3")

        # 39 Flèche droite
        # 68 D
        # 102 Pavé numérique droite
        elif (
            (keycode == 39 or keycode == 68 or keycode == 102)
            and (deplacement_droite or fusion_droite)
            and TableauJeu != tableau_jeu_temp_droite
        ):
            mouvement.Droite(TableauJeu)
            deplacement_fait = True

            if fusion_droite:
                jouer_son("Audio/Fusion.mp3")  # Jouer le son de la fusion
            else:
                # Jouer le son du déplacement
                jouer_son("Audio/Deplacement.mp3")

        # 40 Flèche bas
        # 83 S
        # 98 Pavé numérique bas
        elif (
            (keycode == 40 or keycode == 83 or keycode == 98)
            and (deplacement_bas or fusion_bas)
            and TableauJeu != tableau_jeu_temp_bas
        ):
            mouvement.Bas(TableauJeu)
            deplacement_fait = True

            if fusion_bas:
                jouer_son("Audio/Fusion.mp3")  # Jouer le son de la fusion
            else:
                # Jouer le son du déplacement
                jouer_son("Audio/Deplacement.mp3")

    if case_vide and deplacement_fait:
        # Faire apparaître une nouvelle case de 2
        while not deplacement:
            random_x, random_y = tuile_aleatoire()
            if TableauJeu[random_y][random_x] == 0:
                TableauJeu[random_y][random_x] = 2
                deplacement = True

        # Ajouter 1 au compteur d'étape
        NB_DEPLACEMENT += 1

    # Valeur du tableau "TableauJeu" dans la fenêtre
    afficher_jeu()

    # Test si 2048 est atteint
    for ligne in range(4):
        if 2048 in TableauJeu[ligne] and not GAGNER and JOUER:
            JOUER = False
            GAGNER = True
            # Son lorsque gagné
            jouer_son("Audio/Gagne.mp3")
            # Message de victoire
            tkinter.messagebox.showinfo(
                "Gagné",
                f"Vous avez gagné !\n{nbDeplacementVar.get()} \
                \n{sommeTableauVar.get()} \
                \n{timer.get()}",
                icon="info",
            )
            # Demande à l'utilisateur si recommencer
            if not tkinter.messagebox.askyesno(
                "Continuer", "Voulez-vous continuez ?", icon="question"
            ):
                recommencer()
                JOUER = True
            else:
                JOUER = True


# Main
# Boucle pour mettre deux cases de 2 dans le tableau
CASE_DEBUT = 0
while CASE_DEBUT < 2:
    RANDOM_X, RANDOM_Y = tuile_aleatoire()
    if TableauJeu[RANDOM_Y][RANDOM_X] == 0:
        TableauJeu[RANDOM_Y][RANDOM_X] = 2
        CASE_DEBUT += 1

# Lancer la fonction TailleFenêtre pour avoir la taille de la fenêtre qu'on demande à l'utilisateur
taille = taille_fenetre()

# Lancer la fenêtre Tkinter
root = tkinter.Tk()
root.attributes("-alpha", 0.0)
root.bind("<Unmap>", minimiser)
root.bind("<Map>", agrandir)
fenetre = tkinter.Toplevel(root)

root.iconbitmap("2048.ico")  # Îcone de la fenêtre
root.title("2048")  # Nom de la fenêtre

# Paramètre de la fenêtre
fenetre.iconbitmap("2048.ico")  # Îcone de la fenêtre
fenetre.title("2048")  # Nom de la fenêtre
fenetre.resizable(False, False)  # Non redimensionnement de la fenêtre
fenetre.geometry("+0+0")  # Position de la fenêtre

# Enlever barre windows
fenetre.overrideredirect(True)
# fenetre.attributes("-topmost", True) # Fenêtre au premier plan

# Barre titre pour changer la barre windows originale
barreTitre = tkinter.Frame(fenetre, bg=GRIS3, borderwidth=1)
barreTitre.grid(row=0, columnspan=4, sticky="nsew")
barreTitre.bind("<ButtonPress-1>", bouger_fenetre_commence)
barreTitre.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
barreTitre.bind("<B1-Motion>", bouger_fenetre)

# Titre dans la barre titre
titre = tkinter.Label(fenetre, text="  2048", bg=GRIS3, fg="white")
titre.grid(row=0, column=1, columnspan=2)
titre.bind("<ButtonPress-1>", bouger_fenetre_commence)
titre.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
titre.bind("<B1-Motion>", bouger_fenetre)

# Bouton fermer et minimiser dans la barre titre
boutonFermerMinimiserFrame = tkinter.Frame(fenetre, bg=GRIS3, borderwidth=2)
boutonFermerMinimiserFrame.grid(row=0, columnspan=4, sticky="ne")
boutonFermer = tkinter.Button(
    boutonFermerMinimiserFrame,
    text="    X    ",
    command=quitter,
    bg=GRIS3,
    fg="white",
    activebackground=ROUGE,
    activeforeground="white",
    borderwidth=0,
    font=("Arial", 12),
)
boutonFermer.grid(row=0, column=1, sticky="ne")
boutonFermer.bind("<Enter>", enter_bouton_fermer)
boutonFermer.bind("<Leave>", leave_bouton_fermer)
boutonMinimiser = tkinter.Button(
    boutonFermerMinimiserFrame,
    text="    —    ",
    command=lambda: [fenetre.withdraw(), root.iconify()],
    bg=GRIS3,
    fg="white",
    activebackground=GRIS1,
    activeforeground="white",
    borderwidth=0,
    font=("Arial", 12),
)
boutonMinimiser.grid(row=0, column=0, sticky="ne")
boutonMinimiser.bind("<Enter>", enter_bouton_minimiser)
boutonMinimiser.bind("<Leave>", leave_bouton_minimiser)

# Icone dans la barre titre
icone = Image.open("2048.ico")
icone = icone.resize((16, 16))
icone = ImageTk.PhotoImage(icone)
label = tkinter.Label(barreTitre, image=icone, bg=GRIS3)
label.grid(row=0, column=0, padx=5, pady=5)
label.bind("<ButtonPress-1>", bouger_fenetre_commence)
label.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
label.bind("<B1-Motion>", bouger_fenetre)

# Création de l"onglet Menu
menu = tkinter.Menubutton(
    barreTitre,
    text="Menu",
    bg=GRIS3,
    activebackground=GRIS1,
    activeforeground="white",
    foreground="white",
)
menu.grid(row=0, column=1)

# Création d"un menu défilant
menuDeroulant = tkinter.Menu(
    menu, background=GRIS2, foreground=BLANC, tearoff=0, activebackground=BLEU3
)

# Ajouter un checkbutton au menu
parametreSon = tkinter.BooleanVar()
parametreSon.set(True)
menuDeroulant.add_checkbutton(
    label="Son", onvalue=True, offvalue=False, variable=parametreSon, command=son()  # type: ignore
)

# Ajouter bouton Recommencer au menu
menuDeroulant.add_command(label="Recommencer", command=recommencer)

# Ajouter bouton Reinitialiser score au menu
menuDeroulant.add_command(label="Reinitialiser le score", command=reinitialiser_score)

# Ajouter un séparateur
menuDeroulant.add_separator()

# Ajouter minimiser quitter au menu
menuDeroulant.add_command(
    label="Minimiser", command=lambda: [fenetre.withdraw(), root.iconify()]
)

# Ajouter bouton quitter au menu
menuDeroulant.add_command(label="Quitter", command=quitter)

# Ajouter un séparateur
menuDeroulant.add_separator()

# Ajouter un bouton à propos au menu
menuDeroulant.add_command(
    label="À propos",
    command=lambda: [
        tkinter.messagebox.showinfo(
            "À propos",
            "Python-2048\n\nCréé par :\n\n- Ryse93\n\nVersion : 10.0 (S10)",
            icon="info",
        )
    ],
)

# Attribution du menu déroulant au menu Affichage
menu.configure(menu=menuDeroulant)

# Label cases
for i in range(4):
    for j in range(4):
        Img[i][j] = afficher_image(  # type: ignore # Création des images
            TableauJeu[i][j], taille
        )
        Case[i][j] = tkinter.Label(  # type: ignore # Créer la case
            fenetre, image=Img[i][j], bg=GRIS2 # type: ignore
        )
        # Placer la case dans la grille de la fenêtre
        Case[i][j].grid(row=i + 6, column=j)  # type: ignore

# Label record
recordVar = tkinter.StringVar()
recordLabel = tkinter.Label(
    fenetre,
    textvariable=recordVar,
    bg=GRIS2,
    fg="white",
    font=("Helvetica", 10, "bold"),
)
recordLabel.grid(row=2, column=0, columnspan=4, sticky="w")

# Label nbDeplacement
nbDeplacementVar = tkinter.StringVar()
nbDeplacementVar.set(f"  Nombre de déplacement : {NB_DEPLACEMENT}")
nbDeplacementLabel = tkinter.Label(
    fenetre,
    textvariable=nbDeplacementVar,
    bg=GRIS2,
    fg="white",
    font=("Helvetica", 10, "bold"),
)
nbDeplacementLabel.grid(row=3, column=0, columnspan=4, sticky="w")

# Label somme_tableau (score)
sommeTableauVar = tkinter.StringVar()
sommeTableauVar.set(f"  Score : {0}")
sommeTableauLabel = tkinter.Label(
    fenetre,
    textvariable=sommeTableauVar,
    bg=GRIS2,
    fg="white",
    font=("Helvetica", 10, "bold"),
)
sommeTableauLabel.grid(row=4, column=0, columnspan=4, sticky="w")

# Timers
TEMPS_DEBUT: int = int(time.time())
temps: int = round(time.time() - TEMPS_DEBUT)
timer = tkinter.StringVar()
timer.set(str(temps))
timerLabel = tkinter.Label(
    fenetre, textvariable=timer, bg=GRIS2, fg="white", font=("Helvetica", 10, "bold")
)
timerLabel.grid(row=5, column=0, columnspan=4, sticky="w")
fonction_timer(temps, timer)

# Afficher le tableau
afficher_jeu()

# Espacement entre les cases
for i in range(4):
    fenetre.grid_columnconfigure(i, minsize=taille)
    fenetre.grid_rowconfigure(i + 6, minsize=taille)

# Couleur de fond fond
fenetre.configure(background=GRIS2)

# Exécution de la fonction "Quitter" lors de lors du click de fermeture de la fenêtre
fenetre.protocol("WM_DELETE_WINDOW", quitter)

# Détecter les touches appuyées
fenetre.bind_all("<KeyRelease>", appuyer)

# Détecte KeyboardInterrupt
signal.signal(signal.SIGINT, sigint_handler)

# Fenêtre au premier plan avec le focus
fenetre.focus_force()
fenetre.lift()

# Détecter lorsqu'on a le focus ou pas
root.bind("<FocusIn>", focus)
root.bind("<FocusOut>", fenetre_focus_out)
fenetre.bind("<FocusIn>", fenetre_focus_in)
fenetre.bind("<FocusOut>", fenetre_focus_out)

# Mainloop
fenetre.mainloop()
