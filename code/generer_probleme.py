import random
 
def generer_probleme_flot(n, avec_couts=False):
    """
    Génère aléatoirement un problème de flot :
    - Matrice de capacité
    - Matrice de coût (optionnel)
    """
 
    # Initialisation : matrices de zéros
    capacites = [[0 for _ in range(n)] for _ in range(n)]
    couts = [[0 for _ in range(n)] for _ in range(n)] if avec_couts else None
 
    # Nombre d'arêtes à remplir : E(n^2 / 2)
    nb_aretes = (n * n) // 2
 
    couples = []
    for i in range(n):
        for j in range(n):
            if i != j:
                couples.append((i, j))
 
    # Tirage aléatoire sans remise de nb_aretes couples (i, j)
    arcs_choisis = random.sample(couples, nb_aretes)
 
    for (i, j) in arcs_choisis:
        capacites[i][j] = random.randint(1, 100)  # Capacité entre 1 et 100
        if avec_couts:
            couts[i][j] = random.randint(1, 100)   # Coût entre 1 et 100
 
    return capacites, couts
