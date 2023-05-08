def Gauche(Tab):
    """
        Gauche(Tab : Tab) : (deplacement : bouléen, fusion : bouléen)
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
        for loop in range(3):
            for j in range(3,0,-1):
                if Tab[i][j-1] == 0:
                    Tab[i][j-1] = Tab[i][j]
                    Tab[i][j] = 0
                    deplacement = True

        # Fusion des cases
        for j in range(0,3):
            if Tab[i][j] == Tab[i][j+1] and Tab[i][j] != 0:
                Tab[i][j] = (Tab[i][j])*2
                Tab[i][j+1] = 0
                fusion = True

        # Déplacement des cases vers la gauche
        for loop in range(3):
            for j in range(3,0,-1):
                if Tab[i][j-1] == 0:
                    Tab[i][j-1] = Tab[i][j]
                    Tab[i][j] = 0
                    deplacement = True
    
    # Retourne les valeurs de déplacement et fusion
    return deplacement, fusion

def Haut(Tab):
    """
        Haut(Tab : Tab) : (deplacement : bouléen, fusion : bouléen)
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
        for loop in range(3):
            for i in range(3,0,-1):
                if Tab[i-1][j] == 0:
                    Tab[i-1][j] = Tab[i][j]
                    Tab[i][j] = 0
                    deplacement = True

        # Fusion des cases
        for i in range(0,3):
            if Tab[i][j] == Tab[i+1][j] and Tab[i][j] != 0:
                Tab[i][j] = (Tab[i][j])*2
                Tab[i+1][j] = 0
                fusion = True

        # Déplacement des cases vers la haut
        for loop in range(3):
            for i in range(3,0,-1):
                if Tab[i-1][j] == 0:
                    Tab[i-1][j] = Tab[i][j]
                    Tab[i][j] = 0
                    deplacement = True

    # Retourne les valeurs de déplacement et fusion
    return deplacement, fusion

def Droite(Tab):
    """
        Droite(Tab : Tab) : (deplacement : bouléen, fusion : bouléen)
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
        for loop in range(3):
            for j in range(0,3):
                if Tab[i][j+1] == 0:
                    Tab[i][j+1] = Tab[i][j]
                    Tab[i][j] = 0
                    deplacement = True

        # Fusion des cases
        for j in range(3,0,-1):
            if Tab[i][j] == Tab[i][j-1] and Tab[i][j] != 0:
                Tab[i][j] = (Tab[i][j])*2
                Tab[i][j-1] = 0
                fusion = True

        # Déplacement des cases vers la droite
        for loop in range(3):
            for j in range(0,3):
                if Tab[i][j+1] == 0:
                    Tab[i][j+1] = Tab[i][j]
                    Tab[i][j] = 0
                    deplacement = True

    # Retourne les valeurs de déplacement et fusion
    return deplacement, fusion
    
def Bas(Tab):
    """
        Bas(Tab : Tab) : (deplacement : bouléen, fusion : bouléen)
            j : colonne
    """

    deplacement = False
    fusion = False

    # Boucle pour chaque colonne
    for j in range(4):

        # Déplacement des cases vers le bas
        for loop in range(3):
            for i in range(0,3):
                if Tab[i+1][j] == 0:
                    Tab[i+1][j] = Tab[i][j]
                    Tab[i][j] = 0
                    deplacement = True

        # Fusion des cases
        for i in range(3,0,-1):
            if Tab[i][j] == Tab[i-1][j] and Tab[i][j] != 0:
                Tab[i][j] = (Tab[i][j])*2
                Tab[i-1][j] = 0
                fusion = True

        # Déplacement des cases vers la droite
        for loop in range(3):
            for i in range(0,3):
                if Tab[i+1][j] == 0:
                    Tab[i+1][j] = Tab[i][j]
                    Tab[i][j] = 0
                    deplacement = True

    # Retourne les valeurs de déplacement et fusion
    return deplacement, fusion