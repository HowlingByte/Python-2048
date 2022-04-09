# Importation des bibliothèques
import random
from PIL import Image, ImageTk

def TuileAléatoire():
    """
        TuileAléatoire()
        Sorties :
            Deux entiers au hasard entre 0 et 3
    """

    x=random.randint(0,3) # On génère un entier entre 0 et 3
    y=random.randint(0,3) # On génère un entier entre 0 et 3
    return x,y # On retourne les deux entiers

def AfficherImage(case, taille):
    """
        AfficherImage(case : entier) : tkinter.PhotoImage
        Entrée :
            case : numéro de la case
        Sortie :
            tkinter.PhotoImage - image de la case
    """
    
    # Ouverture de l'image
    image = Image.open("Cases/"+str(case)+".png")

    if taille==200:
        taille=189
    elif taille==150:
        taille=139
    elif taille==100:
        taille=95
    
    # Redimensionner l'image
    imageRedimensionner=image.resize((taille, taille))
    
    # Retourner l'image
    return (ImageTk.PhotoImage(imageRedimensionner))

def EnterBoutonFermer(event):
    """
        EnterBoutonFermer(event)
            Changement de couleur du bouton lorsqu'on passe la souris dessus
    """

    event.widget.configure(bg="#D71526", fg="white") # Changement de couleur du bouton

def LeaveBoutonFermer(event):
    """
        LeaveBoutonFermer(event)
            Changement de couleur du bouton lorsqu'on sort la souris de la zone du bouton
    """

    event.widget.configure(bg="#3C3C3C", fg="white") # Changement de couleur du bouton

def EnterBoutonMinimiser(event):
    """
        EnterBoutonMinimiser(event)
            Changement de couleur du bouton lorsqu'on passe la souris dessus
    """

    event.widget.configure(bg="#505050", fg="white") # Changement de couleur du bouton

def LeaveBoutonMinimiser(event):
    """
        LeaveBoutonMinimiser(event)
            Changement de couleur du bouton lorsqu'on sort la souris de la zone du bouton
    """

    event.widget.configure(bg="#3C3C3C", fg="white") # Changement de couleur du bouton

def EnterBouton(event):
    """
        EnterBouton(event)
            Changement de couleur du bouton lorsqu'on passe la souris dessus
    """
    event.widget.configure(bg="#1177BB", fg="white") # Changement de couleur du bouton

def LeaveBouton(event):
    """
        LeaveBouton(event)
            Changement de couleur du bouton lorsqu'on sort la souris de la zone du bouton
    """
    event.widget.configure(bg="#0E639C", fg="white") # Changement de couleur du bouton