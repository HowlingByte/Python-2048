"""
mouvement.py
    Fonction de mouvement des cases du jeu.
    Auteur : Ahhj93
"""

def gauche(tab):
    """
    gauche(tab : tab) : (deplacement : bouléen, fusion : bouléen)
    Déplacement des cases vers la gauche et fusion des cases si deux cases côte à côte sont égaux.
    Variables locales:
        i : ligne
        j : colonne
    """

    fusion = False
    deplacement = False

    # Boucle pour chaque ligne
    for i in range(4):
        # Déplacement des cases vers la gauche
        for _ in range(3):
            for j in range(3, 0, -1):
                if tab[i][j - 1] == 0:
                    tab[i][j - 1] = tab[i][j]
                    tab[i][j] = 0
                    deplacement = True

        # Fusion des cases
        for j in range(0, 3):
            if tab[i][j] == tab[i][j + 1] and tab[i][j] != 0:
                tab[i][j] = (tab[i][j]) * 2
                tab[i][j + 1] = 0
                fusion = True

        # Déplacement des cases vers la gauche
        for _ in range(3):
            for j in range(3, 0, -1):
                if tab[i][j - 1] == 0:
                    tab[i][j - 1] = tab[i][j]
                    tab[i][j] = 0
                    deplacement = True

    # Retourne les valeurs de déplacement et fusion
    return deplacement, fusion


def haut(tab):
    """
    haut(tab : tab) : (deplacement : bouléen, fusion : bouléen)
    Déplacement des cases vers la haut et fusion des cases si deux cases côte à côte sont égaux.
    Variables locales:
        i : ligne
        j : colonne
    """

    deplacement = False
    fusion = False

    # Boucle pour chaque colonne
    for j in range(4):
        # Déplacement des cases vers la haut
        for _ in range(3):
            for i in range(3, 0, -1):
                if tab[i - 1][j] == 0:
                    tab[i - 1][j] = tab[i][j]
                    tab[i][j] = 0
                    deplacement = True

        # Fusion des cases
        for i in range(0, 3):
            if tab[i][j] == tab[i + 1][j] and tab[i][j] != 0:
                tab[i][j] = (tab[i][j]) * 2
                tab[i + 1][j] = 0
                fusion = True

        # Déplacement des cases vers la haut
        for _ in range(3):
            for i in range(3, 0, -1):
                if tab[i - 1][j] == 0:
                    tab[i - 1][j] = tab[i][j]
                    tab[i][j] = 0
                    deplacement = True

    # Retourne les valeurs de déplacement et fusion
    return deplacement, fusion


def droite(tab):
    """
    droite(tab : tab) : (deplacement : bouléen, fusion : bouléen)
    Déplacement des cases vers la droite et fusion des cases si deux cases côte à côte sont égaux.
    Variables locales:
        i : ligne
        j : colonne
    """

    deplacement = False
    fusion = False

    # Boucle pour chaque ligne
    for i in range(4):
        # Déplacement des cases vers la droite
        for _ in range(3):
            for j in range(0, 3):
                if tab[i][j + 1] == 0:
                    tab[i][j + 1] = tab[i][j]
                    tab[i][j] = 0
                    deplacement = True

        # Fusion des cases
        for j in range(3, 0, -1):
            if tab[i][j] == tab[i][j - 1] and tab[i][j] != 0:
                tab[i][j] = (tab[i][j]) * 2
                tab[i][j - 1] = 0
                fusion = True

        # Déplacement des cases vers la droite
        for _ in range(3):
            for j in range(0, 3):
                if tab[i][j + 1] == 0:
                    tab[i][j + 1] = tab[i][j]
                    tab[i][j] = 0
                    deplacement = True

    # Retourne les valeurs de déplacement et fusion
    return deplacement, fusion


def bas(tab):
    """
    bas(tab : tab) : (deplacement : bouléen, fusion : bouléen)
        j : colonne
    """

    deplacement = False
    fusion = False

    # Boucle pour chaque colonne
    for j in range(4):
        # Déplacement des cases vers le bas
        for _ in range(3):
            for i in range(0, 3):
                if tab[i + 1][j] == 0:
                    tab[i + 1][j] = tab[i][j]
                    tab[i][j] = 0
                    deplacement = True

        # Fusion des cases
        for i in range(3, 0, -1):
            if tab[i][j] == tab[i - 1][j] and tab[i][j] != 0:
                tab[i][j] = (tab[i][j]) * 2
                tab[i - 1][j] = 0
                fusion = True

        # Déplacement des cases vers la droite
        for _ in range(3):
            for i in range(0, 3):
                if tab[i + 1][j] == 0:
                    tab[i + 1][j] = tab[i][j]
                    tab[i][j] = 0
                    deplacement = True

    # Retourne les valeurs de déplacement et fusion
    return deplacement, fusion
