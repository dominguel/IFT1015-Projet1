from tp import *
from tests import unit_tests
# Programme defini a la fin du TP:
# "Une fois que vous aurez implemente toutes les fonctions demandees..."
# On s'en sert comme test final, en plus des tests unitaires ajoutes au debut.

unit_tests()

set_screen_mode(20, 20)

# Couleurs
couleurs = ["#f00", "#f00", # rouge
            "#0f0", "#0f0", # vert
            "#fa0", "#fa0", "#fa0", "#fa0", "#fa0" # orange
         ]

# Creation d'une grille vide
forme = []
for _ in range(20):
    forme.append([-1] * 20)
    
# Forme representant un planeur dans le Jeu de la vie
planeur = [
    [-1, -1,  1],
    [ 1, -1,  2],
    [-1,  2,  2]
]

# On ajoute le planeur a la position (4, 4)
forme = superpose(forme, planeur, 4, 4)

# Iteration creant une animation du jeu de la vie
for _ in range(20):
    effacer(0, 0, 20, 20)
    afficher(0, 0, forme, couleurs)
    forme = jeu_de_la_vie(forme) # prochaine forme
    sleep(0.5) # Pause pour l'animation
