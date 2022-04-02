# Importation des bibliothèques
import tkinter

def TailleFenetre():
    """
        TailleFenetre()
        Sortie :
            Retourne la taille de la fenêtre
    """
    
    def BougerFenetre(event):
        """
            BougerFenetre(event)
            Entrée :
                event : événement
            Sortie :
                Bouge la fenêtre
        """
        
        fenetre.geometry("+{}+{}".format(event.x_root, event.y_root))

    def EnterBoutonFermer(event):
        event.widget.configure(bg="#D71526", fg="white")
    
    def LeaveBoutonFermer(event):
        event.widget.configure(bg="#3C3C3C", fg="white")

    def EnterBouton(event):
        event.widget.configure(bg="#1177BB", fg="white")

    def LeaveBouton(event):
        event.widget.configure(bg="#0E639C", fg="white")
        
    # Lancer la fenêtre Tkinter
    fenetre = tkinter.Tk()

    # Paramètre de la fenêtre
    fenetre.iconbitmap("2048.ico") # Îcone de la fenêtre
    fenetre.title("2048") # Nom de la fenêtre
    fenetre.geometry("330x500+40+40") # Taille de la fenêtre
    fenetre.configure(background = "#1E1E1E") # Couleur de fond fond
    fenetre.overrideredirect(True)
    fenetre.attributes("-topmost", True) # Fond de la fenêtre au premier plan

    # Barre titre pour changer la barre windows originale
    barreTitre=tkinter.Frame(fenetre, bg="#3C3C3C", borderwidth=2)
    barreTitre.pack(side="top", fill="x")
    barreTitre.bind("<B1-Motion>", BougerFenetre)
    titre=tkinter.Label(barreTitre, text="  2048", bg="#3C3C3C", fg="white")
    titre.pack(side="left")
    titre.bind("<B1-Motion>", BougerFenetre)
    boutonFermer=tkinter.Button(barreTitre, text="    X    ", command=lambda:[fenetre.destroy(), exit()], bg="#3C3C3C", fg="white", activebackground="#D71526", activeforeground="white", borderwidth=0, font=("Calibri", 12))
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
    menuDeroulant = tkinter.Menu(menu, background="#4d4d4d", foreground="#ffffff", tearoff=0)
    menuDeroulant.add_command(label="À propos", command = lambda:[tkinter.messagebox.showinfo("À propos", "2048 (Projet NSI GA.1)\n\nCréé par :\n\n- ING Bryan\n- ABASSE Tidiane\n- GALANG Andrei\n\nVersion : 5.0")])
    # Attribution du menu déroulant au menu Affichage
    menu.configure(menu=menuDeroulant)

    # Image
    img = tkinter.PhotoImage(file="2048_logo.png")
    label = tkinter.Label(fenetre, image=img, bg="#1E1E1E")
    label.pack(pady=10)

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
    menu = tkinter.OptionMenu(fenetre, variable, *OptionList)
    menu.config(background="#3C3C3C", activebackground="#3C3C3C", foreground="white", activeforeground="white", borderwidth=0, bd=0, highlightthickness=0, width=20, border=0)
    menu["menu"].config(background="#3C3C3C", activebackground="#094771", foreground="white", activeforeground="white", borderwidth=0, bd=0)
    menu.pack(pady=10)

    # Bouton pour valider
    bouton = tkinter.Button(fenetre, text="   Valider   ", command=fenetre.destroy, borderwidth=0, bg="#0E639C", fg="white", font=("Helvetica", 10))
    bouton.pack()
    bouton.bind("<Enter>", EnterBouton)
    bouton.bind("<Leave>", LeaveBouton)

    # Fermer le programme lors de lors du click de fermeture de la fenêtre
    fenetre.protocol("WM_DELETE_WINDOW", lambda:[fenetre.destroy(), exit()])

    # Exécution de la fenêtre
    fenetre.mainloop()

    # Récupération de la taille
    if variable.get() == "800x932":
        return 200
    elif variable.get() == "600x666":
        return 150
    elif variable.get() == "400x433":
        return 100
