# TESTS UNITAIRES

def unit_tests():
    pass# undefined
    #TODO: demander au prof si les tests unitaires sont necessaires
    # quand on a autant d'assertions sur de si simples fonctions
    # i.e. comment trouver un cas limite pour palette qui n'est pas un assert?

# ASSERTIONS POUR LES ARGUMENTS

# La procedure palette prend en parametre deux entiers x et y et une liste de
# couleurs en format RGB444.
# Elle affiche cette palette de couleur sur une ligne horizontale commencant a
# la position (x,y).
def palette(x, y, couleurs):

    palette_valide(couleurs)

    assert isinstance(x, int)               , "type invalide"
    assert getScreenWidth() > 0             , "ecran de largeur 0"
    assert x >= 0 and x < getScreenWidth()  , "coordonee x hors champ"
    assert len(couleurs)<=getScreenWidth()-x, "palette trop large"

    assert isinstance(y, int)               , "type invalide"
    assert y >= 0 and y < getScreenHeight() , "coordonee y hors champ"

def palette_valide(couleurs):
    assert isinstance(couleurs, list)       , "type invalide"
    for i in couleurs:
        # validite des couleurs
        rgb444_valide(i)

def rgb444_valide(couleur):
    # Selon la specification, on accepte le format "#000" a "#FFF"
    # Les exemples montrent aussi des minuscules acceptees
    assert isinstance(couleur, str)         , "type invalide"
    assert len(couleur) == 4                , "code couleur de forme invalide"
    assert couleur[0] == "#"                , "symbole \"#\" manquant"
    for i in couleur[1:]:# pour chaque symbole i apres "#" (par une slice)
        assert i.upper() in "0123456789ABCDEF", "symbole non-hex dans couleur"


# La procedure afficher prend en entree deux entiers x et y, une forme (une 
# matrice 2D contenant des index vers une couleur de la palette de couleur) et
# une palette de couleurs (une liste de couleurs au format RGB444). Elle affiche
# la forme a l'ecran en utilisant les couleurs correspondantes. La valeur -1
# dans la forme correspond a une case vide pour laquelle la couleur deja
# presente dans le dessin doit etre conservee.
def afficher(x, y, forme, couleurs):
    #TODO: verifier le comportement attendu quand la forme ne rentre pas

    palette_valide(couleurs)
    forme_valide(forme)

    # validite des references forme -> palette
    for rangee in forme:
        for i in rangee:
            assert i >= -1 and i < len(couleurs), (
                "forme contient une couleur non-definie"
            )

    assert isinstance(x, int)               , "type invalide"
    assert 0 <= x < getScreenWidth()        , "coordonee x hors champ"
    # forme dans l'ecran (horizontalement) ssi forme passe deja forme_valide()
    assert getScreenWidth()>=len(forme[0])+x, "forme depasse l'ecran"

    assert isinstance(y, int)               , "type invalide"
    assert 0 <= y < getScreenHeight()       , "coordonee y hors champ"
    assert getScreenHeight()>=len(forme)+y  , "forme depasse l'ecran"

def forme_valide(forme):

    assert isinstance(forme, list)          , "type invalide"

    largeur = len(forme[0])
    for rangee in forme:
        assert isinstance(rangee, list)     , "type invalide"
        assert len(rangee) == largeur       , "matrice non-rectangulaire"

        for i in rangee:
            assert isinstance(i, int)       , "type invalide"
            # couleurs dans [-1, +infini[
            assert i >= -1                  , "couleur negative indefinissable"


# La procedure effacer prend en entree quatres entiers. Les deux premiers
# parametres, x et y représentent la position du coin superieur gauche d'un
# rectangle. Les dimensions du rectangle sont donnees par les deux derniers
# parametres, largeur et hauteur. La procedure doit remplacer tous les pixels
# du rectangle par des pixels noirs ("#000").
def effacer(x, y, largeur, hauteur):
    #TODO: verifier le comportement attendu quand forme1 ne contient pas forme2

    assert isinstance(x, int)               , "type invalide"
    assert 0 <= x and x < getScreenWidth()  , "coordonee x hors champ"

    assert isinstance(largeur, int)         , "type invalide"
    assert largeur >= 0                     , "largeur negative"
    assert getScreenWidth() >= x + largeur  , "aire definie depasse l'ecran"

    assert isinstance(y, int)               , "type invalide"
    assert 0 <= y and y < getScreenHeight() , "coordonee y hors champ"

    assert isinstance(hauteur, int)         , "type invalide"
    assert hauteur >= 0                     , "hauteur negative"
    assert getScreenHeight() >= y + hauteur , "aire definie depasse l'ecran"


# La fonction superpose prend deux formes (des matrices 2D) et retourne une
# nouvelle forme (une autre matrice 2D) ayant les memes dimensions de la forme1,
# mais a laquelle la forme2 a ete ajoutee a la position (x, y). La forme2 est
# superposee a la forme1 de telle sorte que les pixels de la forme2 remplacent
# ceux de la forme1 a la position correspondante. Si un pixel de la forme2 est
# egal a -1, le pixel de la forme1 est conserve.
def superpose(forme1, forme2, x, y):
    #TODO: verifier le comportement attendu quand forme2 depasse forme1
    # apres la translation (+x, +y)

    forme_valide(forme1)
    forme_valide(forme2)

    assert isinstance(x, int)               , "type invalide"
    assert 0 <= x and x < getScreenWidth()  , "coordonee x hors champ"
    assert isinstance(y, int)               , "type invalide"
    assert 0 <= x and y < getScreenHeight() , "coordonee y hors champ"
# notes:
# la matrice de retour est un nouvel objet de dimensions forme1
# les pixels de forme2 d'index hors forme1 sont ignores?
# -1 est la couleur transparente


# La fonction negatif prend une forme en entree et retourne une nouvelle forme
# ou les pixels colores sont remplaces par des pixels vides (representes par
# -1), et les pixels vides sont remplaces par la couleur 0.
def negatif(forme):
    forme_valide(forme)
# notes:
# fonction constituee d'un test ==-1 et d'une forme de retour
# devrait seulement briser sur une matrice heterogene (erreur de type)


# La fonction aleatoire prend quatres entiers en parametres et retourne une
# forme de dimensions largeur x hauteur ou chaque pixel est assigne a une
# couleur aleatoire parmi nb_couleurs. Les couleurs sont representees par des
# entiers allant de 0 a nb_couleurs - 1.
def aleatoire(largeur, hauteur, nb_couleurs):
    #TODO: demander au prof des explications sur le quatrieme argument (trois
    # entiers definis par la spec)

    assert isinstance(largeur, int)     , "type invalide"
    assert largeur >= 0                 , "largeur negative"

    assert isinstance(hauteur, int)     , "type invalide"
    assert hauteur >= 0                 , "hauteur negative"

    assert isinstance(nb_couleurs, int) , "type invalide"
    # selon la spec, aleatoire ne contient jamais la couleur -1
    assert nb_couleurs > 0              , "palette insuffisante"


# La fonction incrementer_couleurs prend une forme et un nombre de couleurs en
# parametres, et retourne une nouvelle forme de memes dimensions ou chaque pixel
# colore est remplace par la couleur suivante dans une palette de couleurs
# allant de 0 a nb_couleurs - 1. Si un pixel a la couleur nb_couleurs - 1, il
# est remplace par la couleur 0. Les pixels vides (representes par -1) restent
# inchanges.
def incrementer_couleurs(forme, nb_couleurs):
#TODO: Comportement attendu quand forme a une couleur > nb_couleur?

    forme_valide(forme)

    assert isinstance(nb_couleurs, int) , "type invalide"
    assert nb_couleurs > 0              , "palette insuffisante"

    # la rotation des couleurs s'effectue sur une palette inconnue, donc avec
    # les couleurs deja utilisees par forme
    # forme contient un nombre inconnu de couleurs, possiblement > nb_couleurs
    for rangee in forme:
        for i in rangee:
            assert i < nb_couleurs      , (
                "incrementation impossible; forme a trop de couleurs"
            )
# notes:
# operation pixel-par-pixel; forme n'a pas besoin de dimensions valides
# utiliser % (mod) pour rester dans le domaine de nb_couleurs
# on ignore les pixels de couleur -1


# La fonction decrementer_couleurs a le comportement inverse de
# incrementer_couleurs. Elle prend une forme et un nombre de couleurs en
# parametres, et retourne une nouvelle forme de memes dimensions ou chaque pixel
# colore est remplace par la couleur precedente dans la palette de couleurs. Si
# un pixel a la couleur 0, il est remplace par la couleur nb_couleurs - 1. Les
# pixels vides (representes par -1) restent inchanges.
def decrementer_couleurs(forme, nb_couleurs):

    forme_valide(forme)

    assert isinstance(nb_couleurs, int) , "type invalide"
    assert nb_couleurs > 0              , "palette insuffisante"

    # la rotation des couleurs s'effectue sur une palette inconnue, donc avec
    # les couleurs deja utilisees par forme
    # forme contient un nombre inconnu de couleurs, possiblement > nb_couleurs
    for rangee in forme:
        for i in rangee:
            assert i < nb_couleurs      , (
                "decrementation impossible; forme a trop de couleurs"
            )
# voir incrementer_couleurs
# rotation gauche sur palette


# La fonction rotation_horaire prend une forme en entree et retourne une
# nouvelle forme qui est la rotation de la forme d'entree dans le sens horaire.
def rotation_horaire(forme):

    forme_valide(forme)
# notes: on peut utiliser la multiplication matricielle ssi forme est une
# matrice valide


# La fonction rotation_antihoraire prend une forme en entree et retourne une
# nouvelle forme qui est la rotation de la forme d'entree dans le sens
# antihoraire.
def rotation_antihoraire(forme):

    forme_valide(forme)
# voir rotation_horaire


# TODO: read the specs
def jeu_de_la_vie(forme):
    pass
