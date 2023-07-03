"""
taille_fenetre.py
    Fonction de la taille de la fenêtre du jeu.
    Auteur : Ahhj93
"""

# Importation des bibliothèques
import tkinter
import tkinter.messagebox
import signal
import sys
from PIL import Image, ImageTk

# Importation des fichiers .py du dossier python
from autres_fonctions import (
    GRIS1,
    GRIS2,
    GRIS3,
    GRIS4,
    BLEU2,
    BLEU3,
    ROUGE,
    BLANC,
    enter_bouton_fermer,
    leave_bouton_fermer,
    enter_bouton,
    leave_bouton,
)

X: int | None = None
Y: int | None = None

def taille_fenetre() -> int:
    """
    taille_fenetre()
    Sortie :
        Retourne la taille de la fenêtre
    """

    def sigint_handler(_signal, _frame):
        """
        sigint_handler(_signal, _frame)
            Ferme la fenetre sans erreur lors du KeyboardInterrupt
        """
        fenetre.destroy()
        sys.exit()

    def bouger_fenetre_commence(event):
        """
        bouger_fenetre_commence(event)
            Fonction qui permet de bouger la fenêtre
        Entrée :
            event : événement
        """
        global X, Y  #pylint: disable=W0603 # On récupère les variables x et y
        X = event.x  # On récupère la position de la souris en x
        Y = event.y  # On récupère la position de la souris en y

    def bouger_fenetre_arrete(_event):
        """
        bouger_fenetre_arrete(_event)
            Fonction qui permet de bouger la fenêtre
        """
        global X, Y  #pylint: disable=W0603 # On récupère les variables x et y
        X = None  # On réinitialise x
        Y = None  # On réinitialise y

    def bouger_fenetre(event):
        """
        bouger_fenetre(event)
        Entrée :
            event : événement
        Sortie :
            Bouge la fenêtre
        """
        global X, Y  #pylint: disable=W0602 # On récupère les variables x et y
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

    # Lancer la fenêtre Tkinter
    fenetre = tkinter.Tk()

    # Paramètre de la fenêtre
    fenetre.iconbitmap("2048.ico")  # Îcone de la fenêtre
    fenetre.title("2048")  # Nom de la fenêtre
    fenetre.geometry("280x370+100+100")  # Taille de la fenêtre
    fenetre.configure(background=GRIS4)  # Couleur de fond fond
    fenetre.overrideredirect(True)
    fenetre.attributes("-topmost", True)  # Fond de la fenêtre au premier plan

    # Barre titre pour changer la barre windows originale
    barre_titre = tkinter.Frame(fenetre, bg=GRIS3, borderwidth=2)
    barre_titre.pack(side="top", fill="x")
    barre_titre.bind("<ButtonPress-1>", bouger_fenetre_commence)
    barre_titre.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
    barre_titre.bind("<B1-Motion>", bouger_fenetre)

    # Icone dans la barre titre
    icone = Image.open("2048.ico")
    icone = icone.resize((16, 16))
    icone = ImageTk.PhotoImage(icone)
    icone_label = tkinter.Label(barre_titre, image=icone, bg=GRIS3)
    icone_label.pack(side="left", padx=5, pady=5)
    icone_label.bind("<ButtonPress-1>", bouger_fenetre_commence)
    icone_label.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
    icone_label.bind("<B1-Motion>", bouger_fenetre)

    # Titre dans la barre titre
    titre = tkinter.Label(barre_titre, text="  2048", bg=GRIS3, fg=BLANC)
    titre.pack(side="left")
    titre.bind("<ButtonPress-1>", bouger_fenetre_commence)
    titre.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
    titre.bind("<B1-Motion>", bouger_fenetre)

    # Bouton fermer
    bouton_fermer = tkinter.Button(
        barre_titre,
        text="    X    ",
        command=lambda: [fenetre.destroy(), sys.exit()],
        bg=GRIS3,
        fg=BLANC,
        activebackground=ROUGE,
        activeforeground=BLANC,
        borderwidth=0,
        font=("Arial", 12),
    )
    bouton_fermer.pack(side="right") #pylint: disable=W0101
    bouton_fermer.bind("<Enter>", enter_bouton_fermer)
    bouton_fermer.bind("<Leave>", leave_bouton_fermer)

    # Barre de menu
    barre_menu = tkinter.Frame(fenetre, borderwidth=3, bg=GRIS3)
    barre_menu.pack(side="top", fill="x")

    # Création de l"onglet Menu
    menu = tkinter.Menubutton(
        barre_menu,
        text="Menu",
        bg=GRIS3,
        activebackground=GRIS1,
        activeforeground=BLANC,
        foreground=BLANC,
    )
    menu.pack(side="left")

    # Création d"un menu défilant
    menu_deroulant = tkinter.Menu(
        menu, background=GRIS2, foreground=BLANC, activebackground=BLEU3, tearoff=0
    )
    menu_deroulant.add_command(
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
    menu.configure(menu=menu_deroulant)

    # Image
    img = tkinter.PhotoImage(file="2048_logo.png")
    img_label = tkinter.Label(fenetre, image=img, bg=GRIS4)
    img_label.pack(pady=10)

    # Texte
    text = tkinter.Label(
        fenetre,
        text=f"Veuillez choisir la taille de la fenêtre\nVotre écran a une résolution {fenetre.winfo_screenwidth()}x{fenetre.winfo_screenheight()}",
        bg="#1E1E1E",
        fg=BLANC,
    )
    text.pack()

    # Création du menu
    option_list = [
        "800x876",
        "600x676",
        "400x476",
    ]
    variable = tkinter.StringVar(fenetre)
    menu_taille = tkinter.OptionMenu(fenetre, variable, *option_list)
    menu_taille.config(
        background=GRIS3,
        activebackground=GRIS3,
        foreground=BLANC,
        activeforeground=BLANC,
        borderwidth=0,
        bd=0,
        highlightthickness=0,
        width=20,
        border=0,
    )
    menu_taille["menu"].config(
        background=GRIS3,
        activebackground=BLEU3,
        foreground=BLANC,
        activeforeground=BLANC,
        borderwidth=0,
        bd=0,
    )
    menu_taille.pack(pady=10)

    choixpref = False
    for option in option_list:
        if (
            int(option.split("x")[0]) > fenetre.winfo_screenwidth()
            or int(option.split("x")[1]) > fenetre.winfo_screenheight()
        ):
            menu_taille["menu"].entryconfig(option, state="disabled")

        elif not choixpref:
            choixpref = True
            variable.set(option)

    # Bouton pour valider
    bouton = tkinter.Button(
        fenetre,
        text="   Valider   ",
        command=fenetre.destroy,
        borderwidth=0,
        bg=BLEU2,
        fg=BLANC,
        font=("Helvetica", 10),
    )
    bouton.pack()
    bouton.bind("<Enter>", enter_bouton)
    bouton.bind("<Leave>", leave_bouton)

    # Fermer le programme lors de lors du click de fermeture de la fenêtre
    fenetre.protocol("WM_DELETE_WINDOW", lambda: [fenetre.destroy(), sys.exit()])

    # Détecte KeyboardInterrupt
    signal.signal(signal.SIGINT, sigint_handler) #pylint: disable=W0101

    # Exécution de la fenêtre
    fenetre.mainloop()

    # Récupération de la taille
    return int(int(variable.get().split("x")[0]) / 4)
