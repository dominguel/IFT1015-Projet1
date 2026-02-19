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

    largeur = len(forme)    # largeur 2 <- hauteur 1
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
    for j in range(0, hauteur, 1):
        resultat.append([])
        # pour la colonne i dans resultat
        for i in range(0, largeur, 1):
            # attention a l'inversion colonne/rangee
            # attention a eviter OBOE dans les indices negatifs
            resultat[j].append(forme[i][-j-1])

    return resultat
