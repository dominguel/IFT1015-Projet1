import tests

def palette(x, y, couleurs):
    tests.palette(x, y, couleurs)# assertions
    for i, c in enumerate(couleurs):
        setPixel(x+i, y, c)

def afficher(x, y, forme, couleurs):
    tests.afficher(x, y, forme, couleurs)# assertions
    # voir la convention des axes; y, j := rangees
    for j, rangee in enumerate(forme):
        # x, i := colonnes
        for i, couleur in enumerate(rangee):
            if couleur != -1:# si non-transparent
                setPixel(x+i, y+j, couleurs[couleur])

def effacer(x, y, largeur, hauteur):
    tests.effacer(x, y, largeur, hauteur)# assertions
    fillRectangle(x, y, largeur, hauteur, "#000")

def superpose(forme1, forme2, x, y):
    tests.superpose(forme1, forme2, x, y)# assertions

    # accumulateur
    resultat = []
    # pour la rangee j de forme1
    for j, rangee1 in enumerate(forme1):
        resultat.append([])
        # pour la couleur [j][i]
        for i, couleur1 in enumerate(rangee1):

            hauteur2 = len(forme2)
            largeur2 = len(forme2[0])
            # ^ forme2[0] est suffisant car forme2 est une matrice rectangulaire 

            # si on est dans forme2 et non-transparent, voir la couleur forme2
            if  ( j >= y            # forme2 a debute verticalement
                and j < y + hauteur2# forme2 n'est pas terminee verticalement
                and i >= x          # forme2 a debute horizontalement
                and i < x + largeur2# forme2 n'est pas terminee horizontalement
                and forme2[j-y][i-x] != -1  # non-transparence
                # ^ ordre d'evaluation pour and: gauche -> droite
                # [j-y][i-x] est donc toujours un index valide quand on y accede
                ):
                resultat[j].append(forme2[j-y][i-x])
            # sinon, voir forme1
            else:
                resultat[j].append(forme1[j  ][i  ])

    return resultat

def negatif(forme) :
    tests.negatif(forme)# assertions

    resultat = []
    for j, rangee in enumerate(forme):
        resultat.append([])
        for i, c in enumerate(rangee):

            if c == -1:
                resultat[j].append(0)
            else:
                resultat[j].append(-1)

    return resultat

def aleatoire(largeur, hauteur, nb_couleurs):
    tests.aleatoire(largeur, hauteur, nb_couleurs)# assertions

    resultat = []
    for j in range(hauteur):
        resultat.append([])
        for _ in range(largeur):
            resultat[j].append(math.floor(random()*nb_couleurs))
            # ^ selon la spec, aleatoire() ne contient jamais la couleur -1
    return resultat

def incrementer_couleurs(forme, nb_couleurs):
    tests.incrementer_couleurs(forme, nb_couleurs)# assertions

    resultat = []
    for j, rangee in enumerate(forme):
        resultat.append([])
        for c in rangee:
            if c != -1:
                resultat[j].append((c+1) % nb_couleurs)
            else:
                resultat[j].append(c)

    return resultat

def decrementer_couleurs(forme, nb_couleurs):
    tests.decrementer_couleurs(forme, nb_couleurs)# assertions

    resultat = []
    for j, rangee in enumerate(forme):
        resultat.append([])
        for c in rangee:
            if c != -1:
                resultat[j].append((c-1) % nb_couleurs)
            else:
                resultat[j].append(c)

    return resultat

def rotation_horaire(forme):
    tests.rotation_horaire(forme)# assertions

    largeur = len(forme)    # colonne du resultat = rangee de l'originale
    hauteur = len(forme[0]) # vice-versa
    # ^ forme[0] est suffisant car forme est une matrice rectangulaire

    resultat = []
    # pour la rangee j dans resultat
    for j in range(hauteur):
        resultat.append([])
        # pour la colonne i dans resultat
        for i in range(largeur):
            # attention a l'inversion de la direction de lecture (indices < 0)
            # attention a eviter OBOE dans les indices negatifs
            resultat[j].append(forme[-i-1][j])

    return resultat

def rotation_antihoraire(forme):
    tests.rotation_antihoraire(forme)# assertions

    largeur = len(forme)    # colonne du resultat = rangee de l'originale
    hauteur = len(forme[0]) # vice-versa
    # ^ forme[0] est suffisant car forme est une matrice rectangulaire

    resultat = []
    # pour la rangee j dans resultat
    for j in range(hauteur):
        resultat.append([])
        # pour la colonne i dans resultat
        for i in range(largeur):
            # attention a l'inversion colonne/rangee
            # attention a eviter OBOE dans les indices negatifs
            resultat[j].append(forme[i][-j-1])

    return resultat

def jeu_de_la_vie(stateIn):
    tests.jeu_de_la_vie(stateIn)# assertions

    stateOut = []
    
    # application des regles du jeu
    for j, rangee in enumerate(stateIn):
        stateOut.append([])
        for i, cell in enumerate(rangee):

        nb_voisins = voisins(stateIn, i, j)
        # Notez qu'on ne prend pas pour acquis que chaque cellule de l'etat
        # initial correspond a son nombre de voisins.
        # On doit donc calculer les voisins dans la nouvelle forme separement
        # de l'application des regles du jeu.
        # C'est plus lent, mais l'etat initial est moins restreint.
        # Aussi, ca m'evite d'ecrire un test d'etat de jeu valide pour stateIn.
        # Donc cellule morte = -1 et cellule vivante = 0
        # on calcule les nouveaux voisins dans une autre iteration

        # Si une cellule (un pixel) dans la forme en paramètre est vivante
        # (colorée) et a moins de 2 voisins vivants, elle meurt (devient vide).
        if cell != -1 and nb_voisins < 2:
            stateOut[j].append(-1)

        # Si une cellule vivante a 2 ou 3 voisins vivants, elle reste vivante.
        elif cell != -1 and nb_voisins in {2, 3}:
            stateOut[j].append(0)

        # Si une cellule vivante a plus de 3 voisins vivants, elle meurt.
        elif cell != -1 and nb_voisins > 3:
            stateOut[j].append(-1)

        # Si une cellule vide a exactement 3 voisins vivants, elle devient
        # vivante (colorée).
        elif cell == -1 and nb_voisins == 3:
            stateOut[j].append(0)

        # cas de base
        else:
            stateOut[j].append(-1)

    # calcul des nouveaux voisins
    for j, rangee in enumerate(stateOut):
        for i, cell in enumerate(rangee):
            if cell != -1:
                stateOut[j][i] = voisins(stateOut, i, j)

    return stateOut

def voisins(forme, x, y):
# Retourne nb voisins vivants de forme[y][x]
# Fonction pure et simple, pas besoin de tests unitaires pour ca.
# Assertions sur les arguments testees par jeu_de_la_vie()

    nb_voisins = 0# acc

    # raccourcis pour lisibilite
    hauteur = len(forme)
    largeur = len(forme[0])
    # ^ forme[0] est suffisant car forme est une matrice rectangulaire

    # Compacter la logique ou laisser la forme plus lisible?

    if y > 0:               # rangee > 0, donc voisin nord existe
        if forme[y-1][x] != -1:
            nb_voisins += 1

    if y < (hauteur - 1):   # rangee avant la fin, donc voisin sud existe
        if forme[y+1][x] != -1:
            nb_voisins += 1

    if x > 0:               # colonne > 0, donc voisin ouest existe
        if forme[y][x-1] != -1:
            nb_voisins += 1

    if x < (largeur - 1):   # colonne avant la fin, donc voisin est existe
        if forme[y][x+1] != -1:
            nb_voisins += 1

    return nb_voisins
