def palette(x, y, couleurs):
    pass# undefined
    # La procédure palette prend en paramètre deux entiers x et y et une liste de couleurs en format RGB444. Elle affiche cette palette de couleur sur une ligne horizontale commencant à la position (x,y).
    # i.e. impure function; outputs to display

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
    #  La procédure afficher prend en entrée deux entiers x et y, une forme (une matrice 2D contenant des index vers une couleur de la palette de couleur) et une palette de couleurs (une liste de couleurs au format RGB444). Elle affiche la forme à l'écran en utilisant les couleurs correspondantes. La valeur -1 dans la forme correspond à une case vide pour laquelle la couleur déjà présente dans le dessin doit être conservée.

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
        # x,i := colonnes
        for i,c in enumerate(forme[j]):
            if c != -1:# si non-transparent
                setPixel(x+i,y+j,couleurs[c])

def effacer(x, y, largeur, hauteur):
    pass# undefined
    #  La procédure effacer prend en entrée quatres entiers. Les deux premiers paramètres, x et y représentent la position du coin supérieur gauche d'un rectangle. Les dimensions du rectangle sont données par les deux derniers paramètres, largeur et hauteur. La procédure doit remplacer tous les pixels du rectangle par des pixels noirs ("#000").

    #TODO: type signature, tests, etc...

    fillRectangle(x, y, largeur, hauteur, "#000")

def superpose(forme1, forme2, x, y):
    pass# undefined
    #  La fonction superpose prend deux formes (des matrices 2D) et retourne une nouvelle forme (une autre matrice 2D) ayant les mêmes dimensions de la forme1, mais à laquelle la forme2 a été ajoutée à la position (x, y). La forme2 est superposée à la forme1 de telle sorte que les pixels de la forme2 remplacent ceux de la forme1 à la position correspondante. Si un pixel de la forme2 est égal à -1, le pixel de la forme1 est conservé.
