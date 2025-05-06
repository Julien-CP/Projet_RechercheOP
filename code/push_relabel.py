from lecteur_graphe import afficher_matrice
 
def push(u, v, capacites, flux, excedent):
    """
    Effectue un push de u vers v
    """
    delta = min(excedent[u], capacites[u][v] - flux[u][v])
    flux[u][v] += delta
    flux[v][u] -= delta
    excedent[u] -= delta
    excedent[v] += delta
    print(f"Push {delta} de {u} vers {v}")
 
def relabel(u, capacites, flux, hauteur):
    """
    Reetiquette le sommet u
    """
    min_hauteur = float('inf')
    for v in range(len(capacites)):
        if capacites[u][v] - flux[u][v] > 0:
            min_hauteur = min(min_hauteur, hauteur[v])
    if min_hauteur < float('inf'):
        hauteur[u] = min_hauteur + 1
        print(f"Relabel sommet {u}, nouvelle hauteur {hauteur[u]}")
 
def push_relabel(noms, capacites, source_nom='s', puits_nom='t'):
    """
    Algorithme de Push-Relabel
    """
    sommet_to_index = {nom: idx for idx, nom in enumerate(noms)}
    source = sommet_to_index[source_nom]
    puits = sommet_to_index[puits_nom]
 
    n = len(noms)
    flux = [[0] * n for _ in range(n)]
    hauteur = [0] * n
    excedent = [0] * n
 
    # Initialisation
    hauteur[source] = n
    for v in range(n):
        flux[source][v] = capacites[source][v]
        flux[v][source] = -capacites[source][v]
        excedent[v] = capacites[source][v]
        excedent[source] -= capacites[source][v]
 
    print("\n=== Debut de Push-Relabel ===")
    print(f"Hauteurs initiales : {hauteur}")
    print(f"Excedents initiaux : {excedent}")
 
    # Liste des sommets actifs (hors source et puits)
    actifs = [i for i in range(n) if i != source and i != puits and excedent[i] > 0]
 
    while actifs:
        u = actifs.pop(0)
        pushed = False
        for v in range(n):
            if capacites[u][v] - flux[u][v] > 0 and hauteur[u] == hauteur[v] + 1:
                push(u, v, capacites, flux, excedent)
                pushed = True
                if v != source and v != puits and v not in actifs and excedent[v] > 0:
                    actifs.append(v)
                if excedent[u] > 0 and u not in actifs:
                    actifs.append(u)
                break
        if not pushed:
            relabel(u, capacites, flux, hauteur)
            actifs.append(u)
 
        # Affichage etat courant
        print(f"\netat actuel:")
        print(f"Hauteurs : {hauteur}")
        print(f"Excedents : {excedent}")
 
    # Calcul du flot total
    flot_max = sum(flux[source][v] for v in range(n) if flux[source][v] > 0)
 
    print("\n===== Resultat final =====")
    print(f"Flot maximal total : {flot_max}")
 
    return flot_max
 
# Test direct (optionnel)
if __name__ == "__main__":
    from lecteur_graphe import lire_graphe
    noms, capacites, couts, type_probleme = lire_graphe("../graphes/graphe1.txt")
    push_relabel(noms, capacites)
 