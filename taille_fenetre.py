# Importation des bibliothèques
import tkinter
import tkinter.messagebox
import signal
from PIL import Image, ImageTk

# Importation des fichiers .py du dossier python
from autresfonctions2048 import (
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


def taille_fenetre():
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
        exit()

    def bouger_fenetre_commence(event):
        """
        bouger_fenetre_commence(event)
            Fonction qui permet de bouger la fenêtre
        Entrée :
            event : événement
        """
        global x, y  # On récupère les variables x et y
        x = event.x  # On récupère la position de la souris en x
        y = event.y  # On récupère la position de la souris en y

    def bouger_fenetre_arrete(_event):
        """
        bouger_fenetre_arrete(_event)
            Fonction qui permet de bouger la fenêtre
        """
        global x, y  # On récupère les variables x et y
        x = None  # On réinitialise x
        y = None  # On réinitialise y

    def bouger_fenetre(event):
        """
        bouger_fenetre(event)
        Entrée :
            event : événement
        Sortie :
            Bouge la fenêtre
        """
        global x, y  # On récupère les variables x et y
        deltax = (
            event.x - x
        )  # On calcule la différence entre la position de la souris et la position de la souris au début du déplacement
        deltay = (
            event.y - y
        )  # On calcule la différence entre la position de la souris et la position de la souris au début du déplacement
        ax = (
            fenetre.winfo_x() + deltax
        )  # On calcule la nouvelle position de la fenêtre en fonction de la différence entre la position de la souris et la position de la souris au début du déplacement
        ay = (
            fenetre.winfo_y() + deltay
        )  # On calcule la nouvelle position de la fenêtre en fonction de la différence entre la position de la souris et la position de la souris au début du déplacement
        fenetre.geometry(f"+{ax}+{ay}")  # On déplace la fenêtre

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
    barreTitre = tkinter.Frame(fenetre, bg=GRIS3, borderwidth=2)
    barreTitre.pack(side="top", fill="x")
    barreTitre.bind("<ButtonPress-1>", bouger_fenetre_commence)
    barreTitre.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
    barreTitre.bind("<B1-Motion>", bouger_fenetre)

    # Icone dans la barre titre
    icone = Image.open("2048.ico")
    icone = icone.resize((16, 16))
    icone = ImageTk.PhotoImage(icone)
    iconeLabel = tkinter.Label(barreTitre, image=icone, bg=GRIS3)
    iconeLabel.pack(side="left", padx=5, pady=5)
    iconeLabel.bind("<ButtonPress-1>", bouger_fenetre_commence)
    iconeLabel.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
    iconeLabel.bind("<B1-Motion>", bouger_fenetre)

    # Titre dans la barre titre
    titre = tkinter.Label(barreTitre, text="  2048", bg=GRIS3, fg=BLANC)
    titre.pack(side="left")
    titre.bind("<ButtonPress-1>", bouger_fenetre_commence)
    titre.bind("<ButtonRelease-1>", bouger_fenetre_arrete)
    titre.bind("<B1-Motion>", bouger_fenetre)

    # Bouton fermer
    boutonFermer = tkinter.Button(
        barreTitre,
        text="    X    ",
        command=lambda: [fenetre.destroy(), exit()],
        bg=GRIS3,
        fg=BLANC,
        activebackground=ROUGE,
        activeforeground=BLANC,
        borderwidth=0,
        font=("Arial", 12),
    )
    boutonFermer.pack(side="right")
    boutonFermer.bind("<Enter>", enter_bouton_fermer)
    boutonFermer.bind("<Leave>", leave_bouton_fermer)

    # Barre de menu
    barreMenu = tkinter.Frame(fenetre, borderwidth=3, bg=GRIS3)
    barreMenu.pack(side="top", fill="x")

    # Création de l"onglet Menu
    menu = tkinter.Menubutton(
        barreMenu,
        text="Menu",
        bg=GRIS3,
        activebackground=GRIS1,
        activeforeground=BLANC,
        foreground=BLANC,
    )
    menu.pack(side="left")

    # Création d"un menu défilant
    menuDeroulant = tkinter.Menu(
        menu, background=GRIS2, foreground=BLANC, activebackground=BLEU3, tearoff=0
    )
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

    # Image
    img = tkinter.PhotoImage(file="2048_logo.png")
    imgLabel = tkinter.Label(fenetre, image=img, bg=GRIS4)
    imgLabel.pack(pady=10)

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
    fenetre.protocol("WM_DELETE_WINDOW", lambda: [fenetre.destroy(), exit()])

    # Détecte KeyboardInterrupt
    signal.signal(signal.SIGINT, sigint_handler)

    # Exécution de la fenêtre
    fenetre.mainloop()

    # Récupération de la taille
    return int(int(variable.get().split("x")[0]) / 4)
