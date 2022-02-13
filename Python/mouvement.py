def gauche(Tab):
    """
        Déplacement des cases vers la gauche et fusion des cases si deux cases côte à côte sont égaux.
        Variables locales:
            i : ligne
            j : colonne
    """

    # Boucle pour chaque ligne
    for i in range(4):

        # Déplacement des cases vers la gauche
        for loup in range(3):
            for j in range(3,0,-1):
                if Tab[i][j-1]==0:
                    Tab[i][j-1]=Tab[i][j]
                    Tab[i][j]=0

        # Fusion des cases
        for j in range(0,3):
            if Tab[i][j]==Tab[i][j+1]:
                Tab[i][j]=(Tab[i][j])*2
                Tab[i][j+1]=0

        # Déplacement des cases vers la gauche
        for loup in range(3):
            for j in range(3,0,-1):
                if Tab[i][j-1]==0:
                    Tab[i][j-1]=Tab[i][j]
                    Tab[i][j]=0

def haut(Tab):
    """
        Déplacement des cases vers la haut et fusion des cases si deux cases côte à côte sont égaux.
        Variables locales:
            i : ligne
            j : colonne
    """

    # Boucle pour chaque colonne
    for j in range(4):

        # Déplacement des cases vers la haut
        for loup in range(3):
            for i in range(3,0,-1):
                if Tab[i-1][j]==0:
                    Tab[i-1][j]=Tab[i][j]
                    Tab[i][j]=0

        # Fusion des cases
        for i in range(0,3):
            if Tab[i][j]==Tab[i+1][j]:
                Tab[i][j]=(Tab[i][j])*2
                Tab[i+1][j]=0

        # Déplacement des cases vers la haut
        for loup in range(3):
            for i in range(3,0,-1):
                if Tab[i-1][j]==0:
                    Tab[i-1][j]=Tab[i][j]
                    Tab[i][j]=0

def droite(Tab):
    """
        Déplacement des cases vers la droite et fusion des cases si deux cases côte à côte sont égaux.
        Variables locales:
            i : ligne
            j : colonne
    """

    # Boucle pour chaque ligne
    for i in range(4):

        # Déplacement des cases vers la droite
        for loup in range(3):
            for j in range(0,3):
                if Tab[i][j+1]==0:
                    Tab[i][j+1]=Tab[i][j]
                    Tab[i][j]=0

        # Fusion des cases
        for j in range(3,0,-1):
            if Tab[i][j]==Tab[i][j-1]:
                Tab[i][j]=(Tab[i][j])*2
                Tab[i][j-1]=0

        # Déplacement des cases vers la droite
        for loup in range(3):
            for j in range(0,3):
                if Tab[i][j+1]==0:
                    Tab[i][j+1]=Tab[i][j]
                    Tab[i][j]=0

def bas(Tab):
    """
        Déplacement des cases vers le bas et fusion des cases si deux cases côte à côte sont égaux.
        Variables locales:
            i : ligne
            j : colonne
    """

    # Boucle pour chaque colonne
    for j in range(4):

        # Déplacement des cases vers le bas
        for loup in range(3):
            for i in range(0,3):
                if Tab[i+1][j]==0:
                    Tab[i+1][j]=Tab[i][j]
                    Tab[i][j]=0

        # Fusion des cases
        for i in range(3,0,-1):
            if Tab[i][j]==Tab[i-1][j]:
                Tab[i][j]=(Tab[i][j])*2
                Tab[i-1][j]=0

        # Déplacement des cases vers la droite
        for loup in range(3):
            for i in range(0,3):
                if Tab[i+1][j]==0:
                    Tab[i+1][j]=Tab[i][j]
                    Tab[i][j]=0