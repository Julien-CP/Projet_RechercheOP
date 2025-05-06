from lecteur_graphe import afficher_matrice
 
def bellman_ford(capacites, couts, source):
    """
    Bellman-Ford pour trouver le plus court chemin en coût
    Retourne les distances et les parents
    """
    n = len(capacites)
    dist = [float('inf')] * n
    parent = [-1] * n
 
    dist[source] = 0
 
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if capacites[u][v] > 0 and dist[u] + couts[u][v] < dist[v]:
                    dist[v] = dist[u] + couts[u][v]
                    parent[v] = u
 
    return dist, parent
 
def min_cost_flow(noms, capacites, couts, valeur_flot, source_nom='s', puits_nom='t'):
    """
    Algorithme de flot de coût minimal avec Bellman-Ford
    """
    sommet_to_index = {nom: idx for idx, nom in enumerate(noms)}
    source = sommet_to_index[source_nom]
    puits = sommet_to_index[puits_nom]
 
    n = len(noms)
    residuel = [ligne[:] for ligne in capacites]
    total_cost = 0
    flot_envoye = 0
 
    iteration = 1
 
    print("\n=== Début de Min-Cost Flow ===")
 
    while flot_envoye < valeur_flot:
        dist, parent = bellman_ford(residuel, couts, source)
 
        if parent[puits] == -1:
            print("Aucun chemin supplémentaire trouvé. Flot non atteignable.")
            break
 
        # Trouver le flot qu'on peut envoyer (min des capacités sur le chemin)
        chemin = []
        flot_chemin = float('inf')
        v = puits
        while v != source:
            u = parent[v]
            chemin.append(noms[v])
            flot_chemin = min(flot_chemin, residuel[u][v])
            v = u
        chemin.append(noms[source])
        chemin.reverse()
 
        flot_envoye_now = min(flot_chemin, valeur_flot - flot_envoye)
 
        # Appliquer le flot sur le graphe résiduel
        v = puits
        while v != source:
            u = parent[v]
            residuel[u][v] -= flot_envoye_now
            residuel[v][u] += flot_envoye_now
            v = u
 
        cost_chemin = dist[puits] * flot_envoye_now
        total_cost += cost_chemin
        flot_envoye += flot_envoye_now
 
        # Affichage de l'itération
        print(f"\nItération {iteration}:")
        print(f"Chemin de coût minimal trouvé : {' -> '.join(chemin)}")
        print(f"Flot envoyé sur ce chemin : {flot_envoye_now}")
        print(f"Coût de ce chemin : {cost_chemin}")
        print(f"Flot cumulé envoyé : {flot_envoye}/{valeur_flot}")
        afficher_matrice(noms, residuel, f"Matrice résiduelle après itération {iteration}")
 
        iteration += 1
 
    print("\n===== Résultat final =====")
    if flot_envoye == valeur_flot:
        print(f"Flot total demandé atteint : {flot_envoye}")
        print(f"Coût total minimal : {total_cost}")
    else:
        print(f"Impossible d'atteindre le flot demandé. Flot envoyé : {flot_envoye}")
 
    return total_cost
 
# Test direct (optionnel)
if __name__ == "__main__":
    from lecteur_graphe import lire_graphe
    noms, capacites, couts, type_probleme = lire_graphe("../graphes/graphe6.txt")
    min_cost_flow(noms, capacites, couts, valeur_flot=10)