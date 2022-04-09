# Importation des bibliothèques
import tkinter
import tkinter.messagebox
import sys
import signal
from PIL import Image, ImageTk

from fonction2048 import *

def TailleFenetre():
    """
        TailleFenetre()
        Sortie :
            Retourne la taille de la fenêtre
    """

    def sigint_handler(signal, frame):
        """
            sigint_handler(signal, frame)
                Ferme la fenetre sans erreur lors du KeyboardInterrupt
        """
        fenetre.destroy()
        exit()

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

    # Lancer la fenêtre Tkinter
    fenetre = tkinter.Tk()

    # Paramètre de la fenêtre
    fenetre.iconbitmap("2048.ico") # Îcone de la fenêtre
    fenetre.title("2048") # Nom de la fenêtre
    fenetre.geometry("280x370+100+100") # Taille de la fenêtre
    fenetre.configure(background = "#1E1E1E") # Couleur de fond fond
    fenetre.overrideredirect(True)
    fenetre.attributes("-topmost", True) # Fond de la fenêtre au premier plan

    # Barre titre pour changer la barre windows originale
    barreTitre=tkinter.Frame(fenetre, bg="#3C3C3C", borderwidth=2)
    barreTitre.pack(side="top", fill="x")
    barreTitre.bind("<ButtonPress-1>", BougerFenetreCommence)
    barreTitre.bind("<ButtonRelease-1>", BougerFenetreArrete)
    barreTitre.bind("<B1-Motion>", BougerFenetre)
    # Icone dans la barre titre
    icone = Image.open("2048.ico")
    icone = icone.resize((16, 16))
    icone = ImageTk.PhotoImage(icone)
    label = tkinter.Label(barreTitre, image=icone, bg="#3C3C3C")
    label.pack(side="left", padx=5, pady=5)
    label.bind("<ButtonPress-1>", BougerFenetreCommence)
    label.bind("<ButtonRelease-1>", BougerFenetreArrete)
    label.bind("<B1-Motion>", BougerFenetre)
    # Titre dans la barre titre
    titre=tkinter.Label(barreTitre, text="  2048", bg="#3C3C3C", fg="white")
    titre.pack(side="left")
    titre.bind("<ButtonPress-1>", BougerFenetreCommence)
    titre.bind("<ButtonRelease-1>", BougerFenetreArrete)
    titre.bind("<B1-Motion>", BougerFenetre)
    # Bouton fermer
    boutonFermer=tkinter.Button(
        barreTitre, text="    X    ", command=lambda:[fenetre.destroy(), exit()], bg="#3C3C3C", fg="white",
        activebackground="#D71526", activeforeground="white", borderwidth=0, font=("Arial", 12))
    boutonFermer.pack(side="right")
    boutonFermer.bind("<Enter>", EnterBoutonFermer)
    boutonFermer.bind("<Leave>", LeaveBoutonFermer)

    # Barre de menu
    barreMenu = tkinter.Frame(fenetre, borderwidth=3, bg="#3C3C3C")
    barreMenu.pack(side="top", fill="x")
    # Création de l"onglet Menu
    menu = tkinter.Menubutton(barreMenu, text="Menu", bg="#3C3C3C", activebackground="#505050", activeforeground="white", foreground="white")
    menu.pack(side="left")
    # Création d"un menu défilant
    menuDeroulant = tkinter.Menu(menu, background="#4d4d4d", foreground="#ffffff", activebackground="#094771", tearoff=0)
    menuDeroulant.add_command(
        label="À propos", command = lambda:[tkinter.messagebox.showinfo(
            "À propos", "2048 (Projet NSI GA.1)\n\nCréé par :\n\n- ING Bryan\n- ABASSE Tidiane\n- GALANG Andrei\n\nVersion : 5.0 (S5)"
            )])
    # Attribution du menu déroulant au menu Affichage
    menu.configure(menu=menuDeroulant)

    # Image
    img = tkinter.PhotoImage(file="2048_logo.png")
    label = tkinter.Label(fenetre, image=img, bg="#1E1E1E")
    label.pack(pady=10)

    # Texte
    text=tkinter.Label(fenetre, text="Veuillez choisir la taille de la fenêtre", bg="#1E1E1E", fg="white")
    text.pack()

    # Création du menu
    OptionList = \
        [
        "800x932",
        "600x666",
        "400x433",
        ]
    variable = tkinter.StringVar(fenetre)
    variable.set(OptionList[1])
    menuTaille = tkinter.OptionMenu(fenetre, variable, *OptionList)
    menuTaille.config(background="#3C3C3C", activebackground="#3C3C3C", foreground="white", activeforeground="white", borderwidth=0, bd=0, highlightthickness=0, width=20, border=0)
    menuTaille["menu"].config(background="#3C3C3C", activebackground="#094771", foreground="white", activeforeground="white", borderwidth=0, bd=0)
    menuTaille.pack(pady=10)

    # Bouton pour valider
    bouton = tkinter.Button(fenetre, text="   Valider   ", command=fenetre.destroy, borderwidth=0, bg="#0E639C", fg="white", font=("Helvetica", 10))
    bouton.pack()
    bouton.bind("<Enter>", EnterBouton)
    bouton.bind("<Leave>", LeaveBouton)

    # Fermer le programme lors de lors du click de fermeture de la fenêtre
    fenetre.protocol("WM_DELETE_WINDOW", lambda:[fenetre.destroy(), exit()])

    # Détecte KeyboardInterrupt
    signal.signal(signal.SIGINT, sigint_handler)

    # Exécution de la fenêtre
    fenetre.mainloop()

    # Récupération de la taille
    if variable.get() == "800x932":
        return 200
    elif variable.get() == "600x666":
        return 150
    elif variable.get() == "400x433":
        return 100
