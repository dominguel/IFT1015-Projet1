def palette(x, y, couleurs):
    pass# undefined
    # impure function; outputs to display

    # proper type signature
    assert type(x) is int
    assert type(y) is int
#    assert type(couleurs) is #TODO: liste de couleurs

    # tests potentiels
    assert len(couleurs) <= getScreenWidth()-x

    for i,c in enumerate(couleurs):
        setPixel(x+i, y, c)

def afficher(x, y, forme, couleurs):
    pass# undefined

    # proper type signature
    assert type(x) is int
    assert type(y) is int
#    assert type(couleurs) is #TODO: liste de couleurs
#    TODO: assert forme est une matrice valide

    # tests potentiels
    # forme contient des index -1 <= i < len(couleurs)
    # forme a des dimensions valides selon getScreenWidth(), getScreenHeight()

    #TODO: verifier si les axes sont bien definis
    # voir la convention des axes; y, j := rangees
    for j in range(len(forme)):
        # x, i := colonnes
        for i,c in enumerate(forme[j]):
            if c != -1:# si non-transparent
                setPixel(x+i,y+j,couleurs[c])

def effacer(x, y, largeur, hauteur):
    pass# undefined

    #TODO: type signature, tests, etc...

    fillRectangle(x, y, largeur, hauteur, "#000")

def superpose(forme1, forme2, x, y):
    pass# undefined
