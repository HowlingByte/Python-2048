# Importation des bibliothèques
import random
import tkinter
import pygame

def TuileAléatoire():
    """
        TuileAléatoire()
        Sorties :
            Deux entiers au hasard entre 0 et 3
    """
    x=random.randint(0,3)
    y=random.randint(0,3)
    return x,y

def AfficherImage(case):
    """
        AfficherImage(case : entier) : tkinter.PhotoImage
        Entrée :
            case : numéro de la case
        Sortie :
            tkinter.PhotoImage - image de la case
    """
    return (tkinter.PhotoImage(file=f"Cases/{case}.png"))