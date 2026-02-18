import tests

def palette(x, y, couleurs):
    tests.palette(x, y, couleurs)# assertions
    for i,c in enumerate(couleurs):
        setPixel(x+i, y, c)

def afficher(x, y, forme, couleurs):
    tests.afficher(x, y, forme, couleurs)# assertions
    #TODO: verifier si les axes sont bien definis
    # voir la convention des axes; y, j := rangees
    for j, rangee in enumerate(forme):
        for i, couleur in enumerate(rangee):
            if couleur != -1:# si non-transparent
                setPixel(x+i, y+j, couleurs[couleur])

def effacer(x, y, largeur, hauteur):
    tests.effacer(x, y, largeur, hauteur)# assertions
    fillRectangle(x, y, largeur, hauteur, "#000")

def superpose(forme1, forme2, x, y):
    pass# undefined
