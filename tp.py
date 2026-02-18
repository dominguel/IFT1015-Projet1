import tests

def palette(x, y, couleurs):
    assert tests.palette(x, y, couleurs)
    for i,c in enumerate(couleurs):
        setPixel(x+i, y, c)

def afficher(x, y, forme, couleurs):
    #TODO: verifier si les axes sont bien definis
    # voir la convention des axes; y, j := rangees
    for j in range(len(forme)):
        # x, i := colonnes
        for i,c in enumerate(forme[j]):
            if c != -1:# si non-transparent
                setPixel(x+i,y+j,couleurs[c])

def effacer(x, y, largeur, hauteur):
    fillRectangle(x, y, largeur, hauteur, "#000")

def superpose(forme1, forme2, x, y):
    pass# undefined
