# La procédure palette prend en paramètre deux entiers x et y et une liste de
# couleurs en format RGB444.
# Elle affiche cette palette de couleur sur une ligne horizontale commencant à
# la position (x,y).
def palette(x, y, couleurs):

    # validite de la palette
    assert palette_valide(couleurs)# abstraite pour repetition

    assert isinstance(x, int)
    # ecran existant?
    assert getScreenWidth() > 0
    # x dans l'ecran?
    assert x >= 0 and x < getScreenWidth()

    assert isinstance(y, int)
    # y dans l'ecran?
    assert y >= 0 and y < getScreenHeight()
    # ecran assez large?
    assert len(couleurs) <= getScreenWidth() - x

def palette_valide(couleurs):
    assert isinstance(couleurs, list)
    # validite des couleurs
    for i in list:
        assert rgb444_valide(i)

def rgb444_valide(couleur):
    # Selon la specification, on accepte le format "#000" a "#FFF"
    # Les exemples montrent aussi des minuscules acceptees
    assert isinstance(couleur, str)
    assert len(couleur) == 4
    assert couleur[0] == "#"
    for i in range(1, 4):
        assert i.upper in "0123456789ABCDEF"

# La procédure afficher prend en entrée deux entiers x et y, une forme (une 
# matrice 2D contenant des index vers une couleur de la palette de couleur) et
# une palette de couleurs (une liste de couleurs au format RGB444). Elle affiche
# la forme à l'écran en utilisant les couleurs correspondantes. La valeur -1
# dans la forme correspond à une case vide pour laquelle la couleur déjà
# présente dans le dessin doit être conservée.
def afficher(x, y, forme, couleurs):
    #TODO: verifier le comportement attendu quand la forme ne rentre pas

    # validite de la palette
    palette_valide(couleurs)
    # validite de la forme
    assert forme_valide(forme)
    # validite des references forme -> palette
    for rangee in forme:
        for i in rangee:
            assert i >= -1 and i < len(couleurs)

    assert isinstance(x, int)
    # x dans l'ecran
    assert 0 <= x < getScreenWidth() 
    # forme dans l'ecran (horizontalement) ssi forme passe deja forme_valide()
    assert getScreenWidth() >= len(forme[0]) + x

    assert isinstance(y, int)
    # y dans l'ecran
    assert 0 <= y < getScreenHeight()
    # forme dans l'ecran (verticalement)
    assert getScreenHeight() >= len(forme) + y

def forme_valide(forme):

    assert isinstance(forme, list)
    largeur = len(forme[0])
    for rangee in forme:
        assert isinstance(rangee, list)

        # matrice valide?
        assert len(rangee) == largeur

        for i in rangee:
            assert isinstance(i, int)

            # couleurs dans [-1, +infini[
            assert i >= -1

# La procédure effacer prend en entrée quatres entiers. Les deux premiers
# paramètres, x et y représentent la position du coin supérieur gauche d'un
# rectangle. Les dimensions du rectangle sont données par les deux derniers
# paramètres, largeur et hauteur. La procédure doit remplacer tous les pixels
# du rectangle par des pixels noirs ("#000").
def effacer(x, y, largeur, hauteur)
#TODO: verifier le comportement attendu quand le rectangle ne rentre pas

    assert isinstance(x, int)
    # x dans l'ecran
    0 <= x < getScreenWidth()

    assert isinstance(largeur, int)
    # largeur non-negative
    largeur >= 0
    # largeur dans l'ecran
    getScreenWidth() >= x + largeur 

    assert isinstance(y, int)
    # y dans l'ecran
    0 <= y < getScreenHeight()

    assert isinstance(hauteur, int)
    # hauteur non-negative
    largeur >= 0
    # hauteur dans l'ecran
    getScreenHeight() >= y + hauteur 


# La fonction superpose prend deux formes (des matrices 2D) et retourne une
# nouvelle forme (une autre matrice 2D) ayant les mêmes dimensions de la forme1,
# mais à laquelle la forme2 a été ajoutée à la position (x, y). La forme2 est
# superposée à la forme1 de telle sorte que les pixels de la forme2 remplacent
# ceux de la forme1 à la position correspondante. Si un pixel de la forme2 est
# égal à -1, le pixel de la forme1 est conservé.

# types:
# forme1 :: [[int]]
# forme2 :: [[int]]

# assertions:
# forme1 est une matrice valide
# forme2 est une matrice valide

# notes:
# la matrice de retour est un nouvel objet de dimensions forme1
# les pixels de forme2 d'index hors forme1 sont ignores
# -1 est la couleur transparente


#  La fonction negatif prend une forme en entrée et retourne une nouvelle forme où les pixels colorés sont remplacés par des pixels vides (représentés par -1), et les pixels vides sont remplacés par la couleur 0.

# types:
# forme :: [[int]]

# notes:
# fonction constituee d'un test ==-1 et d'une forme de retour
# devrait seulement briser sur une matrice heterogene (erreur de type)


#  La fonction aleatoire prend quatres entiers en paramètres et retourne une forme de dimensions largeur x hauteur où chaque pixel est assigné à une couleur aléatoire parmi nb_couleurs. Les couleurs sont représentées par des entiers allant de 0 à nb_couleurs - 1.

# TODO: demander au prof des explications sur le quatrieme argument (trois entiers definis par la spec)

# types:
# largeur :: int
# hauteur :: int
# nb_couleurs :: int

# assertions:
# largeur >= 0
# hauteur >= 0
# nb_couleurs > 0 # selon la specification, aleatoire ne contient jamais la couleur -1


#  La fonction incrementer_couleurs prend une forme et un nombre de couleurs en paramètres, et retourne une nouvelle forme de mêmes dimensions où chaque pixel coloré est remplacé par la couleur suivante dans une palette de couleurs allant de 0 à nb_couleurs - 1. Si un pixel a la couleur nb_couleurs - 1, il est remplacé par la couleur 0. Les pixels vides (représentés par -1) restent inchangés.

# types:
# forme :: [[int]]
# nb_couleurs :: int

# assertions:
# nb_couleurs > 0
# forme ne contient que c t.q. nb_couleurs > c

# notes:
# operation pixel-par-pixel seulement; forme n'a pas besoin de dimensions valides
# utiliser % (mod) pour rester dans le domaine de nb_couleurs
# on ignore les pixels de couleur -1


#  La fonction decrementer_couleurs a le comportement inverse de incrementer_couleurs. Elle prend une forme et un nombre de couleurs en paramètres, et retourne une nouvelle forme de mêmes dimensions où chaque pixel coloré est remplacé par la couleur précédente dans la palette de couleurs. Si un pixel a la couleur 0, il est remplacé par la couleur nb_couleurs - 1. Les pixels vides (représentés par -1) restent inchangés.

# voir incrementer_couleurs
# rotation gauche sur palette


#  La fonction rotation_horaire prend une forme en entrée et retourne une nouvelle forme qui est la rotation de la forme d'entrée dans le sens horaire.

# types:
# forme :: [[int]]

# notes: on peut utiliser la multiplication matricielle ssi forme est une matrice valide


#  La fonction rotation_antihoraire prend une forme en entrée et retourne une nouvelle forme qui est la rotation de la forme d'entrée dans le sens antihoraire.

# voir rotation_horaire


# TODO: read the specs
def jeu_de_la_vie(forme):
    pass
