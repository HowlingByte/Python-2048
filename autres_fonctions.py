# Importation des bibliothèques
import random
from PIL import Image, ImageTk

##Couleur
# Gris
GRIS1 = "#505050"
GRIS2 = "#4D4D4D"
GRIS3 = "#3C3C3C"
GRIS4 = "#1E1E1E"
# Bleu
BLEU1 = "#1177BB"
BLEU2 = "#0E639C"
BLEU3 = "#094771"
# Rouge
ROUGE = "#D71526"
# Blanc
BLANC = "#FFFFFF"

## Variable
BG_TEMP = GRIS3
FG_TEMP = BLANC


def tuile_aleatoire():
    """
    tuile_aleatoire()
    Sorties :
        Deux entiers au hasard entre 0 et 3
    """

    random_x = random.randint(0, 3)  # On génère un entier entre 0 et 3
    random_y = random.randint(0, 3)  # On génère un entier entre 0 et 3
    return random_x, random_y  # On retourne les deux entiers


def afficher_image(case, taille):
    """
    afficher_image(case : entier) : tkinter.PhotoImage
    Entrée :
        case : numéro de la case
    Sortie :
        tkinter.PhotoImage - image de la case
    """

    # Ouverture de l'image
    image = Image.open("Cases/" + str(case) + ".png")

    if taille == 200:
        taille = 189
    elif taille == 150:
        taille = 139
    elif taille == 100:
        taille = 95

    # Redimensionner l'image
    imageRedimensionner = image.resize((taille, taille))

    # Retourner l'image
    return ImageTk.PhotoImage(imageRedimensionner)


def enter_bouton_fermer(event):
    """
    enter_bouton_fermer(event)
        Changement de couleur du bouton lorsqu'on passe la souris dessus
    """
    global BG_TEMP
    global FG_TEMP
    BG_TEMP = event.widget["bg"]
    FG_TEMP = event.widget["fg"]
    event.widget.configure(bg=ROUGE, fg=BLANC)  # Changement de couleur du bouton


def leave_bouton_fermer(event):
    """
    leave_bouton_fermer(event)
        Changement de couleur du bouton lorsqu'on sort la souris de la zone du bouton
    """
    event.widget.configure(bg=BG_TEMP, fg=FG_TEMP)  # Changement de couleur du bouton


def enter_bouton_minimiser(event):
    """
    enter_bouton_minimiser(event)
        Changement de couleur du bouton lorsqu'on passe la souris dessus
    """
    global BG_TEMP
    global FG_TEMP
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
