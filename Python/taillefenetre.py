# Importation des bibliothèques
import tkinter
from PIL import ImageTk

def TailleFenetre():
    """
        TailleFenetre()
        Sortie :
            Retourne la taille de la fenêtre
    """
    
    # Lancer la fenêtre Tkinter
    fenetre = tkinter.Tk()

    # Paramètre de la fenêtre
    fenetre.iconbitmap("2048.ico") # Îcone de la fenêtre
    fenetre.title("2048") # Nom de la fenêtre
    fenetre.geometry('300x300') # Taille de la fenêtre

    # Image
    img = ImageTk.PhotoImage(file="Cases/2048.png")
    label = tkinter.Label(fenetre, image=img)
    label.pack()

    # Création du menu
    OptionList = \
        [
        "Normale (200x200)",
        "100x100",
        ] 
    variable = tkinter.StringVar(fenetre)
    variable.set(OptionList[0])
    menu = tkinter.OptionMenu(fenetre, variable, *OptionList)
    menu.config(width=90, font=('Calibri', 12))
    menu.pack()

    # Bouton pour valider
    bouton = tkinter.Button(fenetre, text="OK", command=fenetre.destroy)
    bouton.pack()

    # Fermer le programme lors de lors du click de fermeture de la fenêtre
    fenetre.protocol("WM_DELETE_WINDOW", lambda:[fenetre.destroy(), exit()])

    # Exécution de la fenêtre
    fenetre.mainloop()

    # Récupération de la taille
    if variable.get() == "Normale (200x200)":
        return 200
    elif variable.get() == "100x100":
        return 100
    
    # Retourne la taille de la fenêtre
    return variable.get()