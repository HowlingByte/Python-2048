# Importation des bibliothèques
import random
from PIL import Image, ImageTk

def TuileAléatoire():
    """
        TuileAléatoire()
        Sorties :
            Deux entiers au hasard entre 0 et 3
    """

    x=random.randint(0,3)
    y=random.randint(0,3)
    return x,y

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
    elif taille==100:
        taille=95

    # Redimensionner l'image
    imageRedimensionner=image.resize((taille, taille))
    
    # Retourner l'image
    return (ImageTk.PhotoImage(imageRedimensionner))