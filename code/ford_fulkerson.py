from collections import deque
from lecteur_graphe import afficher_matrice
 
def bfs(capacites, source, puits, parents):
    """
    Parcours en largeur pour trouver un chemin augmentant.
    Remplit le tableau parents.
    """
    n = len(capacites)
    visite = [False] * n
 
    file = deque()
    file.append(source)
    visite[source] = True
 
    while file:
        u = file.popleft()
        for v in range(n):
            if not visite[v] and capacites[u][v] > 0:
                file.append(v)
                visite[v] = True
                parents[v] = u
                if v == puits:
                    return True  # trouve un chemin de s à t
    return False
 
def ford_fulkerson(noms, capacites, source_nom='s', puits_nom='t'):
    """
    Algorithme de Ford-Fulkerson utilisant BFS.
    Affiche chaque etape du deroulement.
    """
    # Associer les noms de sommets à des indices
    sommet_to_index = {nom: idx for idx, nom in enumerate(noms)}
    source = sommet_to_index[source_nom]
    puits = sommet_to_index[puits_nom]
 
    # Copier la matrice de capacites pour creer la matrice residuelle
    n = len(noms)
    residuel = [ligne[:] for ligne in capacites]
 
    parents = [-1] * n  # Pour reconstituer les chemins
    flot_max = 0
 
    iteration = 1
    while bfs(residuel, source, puits, parents):
        # Trouver le flot maximal possible sur ce chemin
        chemin = []
        flot_chemin = float('inf')
        v = puits
        while v != source:
            u = parents[v]
            chemin.append(noms[v])
            flot_chemin = min(flot_chemin, residuel[u][v])
            v = u
        chemin.append(noms[source])
        chemin.reverse()
 
        # Afficher le chemin trouve
        print(f"\nIteration {iteration}:")
        print(f"Chemin augmentant trouve : {' -> '.join(chemin)}")
        print(f"Flot ajoute sur ce chemin : {flot_chemin}")
 
        # Mettre à jour le graphe residuel
        v = puits
        while v != source:
            u = parents[v]
            residuel[u][v] -= flot_chemin
            residuel[v][u] += flot_chemin
            v = u
 
        flot_max += flot_chemin
 
        # Afficher la matrice residuelle
        afficher_matrice(noms, residuel, f"Matrice residuelle apres iteration {iteration}")
 
        iteration += 1
 
    print("\n===== Resultat final =====")
    print(f"Flot maximal total : {flot_max}")
 
    return flot_max
 
# Execution directe pour tester (optionnel)
if __name__ == "__main__":
    from lecteur_graphe import lire_graphe
    noms, capacites, couts, type_probleme = lire_graphe("../graphes/graphe1.txt")
    ford_fulkerson(noms, capacites)
 