"""
autres_fonctions.py
    contient les fonctions annexes au jeu
    Auteur : Ryse93
"""

# Importation des bibliothèques
import random
import tkinter
from PIL import Image, ImageTk

##Couleur
# Gris
GRIS1: str = "#505050"
GRIS2: str = "#4D4D4D"
GRIS3: str = "#3C3C3C"
GRIS4: str = "#1E1E1E"
# Bleu
BLEU1: str = "#1177BB"
BLEU2: str = "#0E639C"
BLEU3: str = "#094771"
# Rouge
ROUGE: str = "#D71526"
# Blanc
BLANC: str = "#FFFFFF"

## Variable
BG_TEMP: str = GRIS3
FG_TEMP: str = BLANC


def tuile_aleatoire() -> tuple[int, int]:
    """
    tuile_aleatoire()
    Sorties :
        Deux entiers au hasard entre 0 et 3
    """

    random_x: int = random.randint(0, 3)  # On génère un entier entre 0 et 3
    random_y: int = random.randint(0, 3)  # On génère un entier entre 0 et 3
    return random_x, random_y  # On retourne les deux entiers


def afficher_image(case: int, taille: int) -> ImageTk.PhotoImage:
    """
    afficher_image(case : entier) : ImageTk.PhotoImage
    Entrée :
        case : numéro de la case
    Sortie :
        ImageTk.PhotoImage - image de la case
    """

    # Ouverture de l'image
    image = Image.open("cases/" + str(case) + ".png")

    if taille == 200:
        taille = 189
    elif taille == 150:
        taille = 139
    elif taille == 100:
        taille = 95

    # Redimensionner l'image
    image_redimensionner = image.resize((taille, taille))

    # Retourner l'image
    return ImageTk.PhotoImage(image_redimensionner)


def enter_bouton_fermer(event: tkinter.Event) -> None:
    """
    enter_bouton_fermer(event)
        Changement de couleur du bouton lorsqu'on passe la souris dessus
    """
    global BG_TEMP # pylint: disable=global-statement
    global FG_TEMP # pylint: disable=global-statement
    BG_TEMP = event.widget["bg"]
    FG_TEMP = event.widget["fg"]
    event.widget.configure(bg=ROUGE, fg=BLANC)  # Changement de couleur du bouton


def leave_bouton_fermer(event: tkinter.Event) -> None:
    """
    leave_bouton_fermer(event)
        Changement de couleur du bouton lorsqu'on sort la souris de la zone du bouton
    """
    event.widget.configure(bg=BG_TEMP, fg=FG_TEMP)  # Changement de couleur du bouton


def enter_bouton_minimiser(event: tkinter.Event) -> None:
    """
    enter_bouton_minimiser(event)
        Changement de couleur du bouton lorsqu'on passe la souris dessus
    """
    global BG_TEMP # pylint: disable=global-statement
    global FG_TEMP # pylint: disable=global-statement
    BG_TEMP = event.widget["bg"]
    FG_TEMP = event.widget["fg"]
    event.widget.configure(bg=GRIS1, fg=BLANC)  # Changement de couleur du bouton


def leave_bouton_minimiser(event):
    """
    leave_bouton_minimiser(event)
        Changement de couleur du bouton lorsqu'on sort la souris de la zone du bouton
    """

    event.widget.configure(bg=BG_TEMP, fg=FG_TEMP)  # Changement de couleur du bouton


def enter_bouton(event):
    """
    enter_bouton(event)
        Changement de couleur du bouton lorsqu'on passe la souris dessus
    """
    event.widget.configure(bg=BLEU1, fg=BLANC)  # Changement de couleur du bouton


def leave_bouton(event):
    """
    leave_bouton(event)
        Changement de couleur du bouton lorsqu'on sort la souris de la zone du bouton
    """
    event.widget.configure(bg=BLEU2, fg=BLANC)  # Changement de couleur du bouton
