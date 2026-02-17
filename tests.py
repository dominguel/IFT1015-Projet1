#  La procédure palette prend en paramètre deux entiers x et y et une liste de couleurs en format RGB444. Elle affiche cette palette de couleur sur une ligne horizontale commencant à la position (x,y).

# types:
# x :: int
# y :: int
# couleurs :: [string]

# assertions:
# 0 <= x < getScreenWidth() # x dans l'ecran
# 0 <= y < getScreenHeight() # y dans l'ecran
# couleurs ne contient que des strings valides RGB444
# getScreenWidth() >= len(couleurs) + x # palette rentre dans l'ecran


#  La procédure afficher prend en entrée deux entiers x et y, une forme (une matrice 2D contenant des index vers une couleur de la palette de couleur) et une palette de couleurs (une liste de couleurs au format RGB444). Elle affiche la forme à l'écran en utilisant les couleurs correspondantes. La valeur -1 dans la forme correspond à une case vide pour laquelle la couleur déjà présente dans le dessin doit être conservée.

# types:
# x :: int
# y :: int
# forme :: [[int]]
# couleurs :: [string]

# assertions:
# 0 <= x < getScreenWidth() # x dans l'ecran
# 0 <= y < getScreenHeight() # y dans l'ecran
# couleurs ne contient que des strings valides RGB444
# forme est une matrice valide
# getScreenWidth() >= len(forme[0]) + x # forme dans l'ecran, ssi forme est une matrice valide
# getScreenHeight() >= len(forme) + y # forme dans l'ecran (verticalement)
# forme ne contient que c t.q. -1 <= c < len(couleurs)


#  La procédure effacer prend en entrée quatres entiers. Les deux premiers paramètres, x et y représentent la position du coin supérieur gauche d'un rectangle. Les dimensions du rectangle sont données par les deux derniers paramètres, largeur et hauteur. La procédure doit remplacer tous les pixels du rectangle par des pixels noirs ("#000").

# types:
# x :: int
# y :: int
# largeur :: int
# hauteur :: int

# assertions:
# 0 <= x < getScreenWidth() # x dans l'ecran
# 0 <= y < getScreenHeight() # y dans l'ecran
# getScreenWidth() >= x + largeur # rectangle dans l'ecran
# getScreenHeight() >= y + hauteur # rectangle dans l'ecran


#  La fonction superpose prend deux formes (des matrices 2D) et retourne une nouvelle forme (une autre matrice 2D) ayant les mêmes dimensions de la forme1, mais à laquelle la forme2 a été ajoutée à la position (x, y). La forme2 est superposée à la forme1 de telle sorte que les pixels de la forme2 remplacent ceux de la forme1 à la position correspondante. Si un pixel de la forme2 est égal à -1, le pixel de la forme1 est conservé.

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
