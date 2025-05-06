def lire_graphe(fichier):
    """
    Lit un fichier de graphe et retourne :
    - la liste des sommets
    - la matrice des capacites
    - la matrice des coûts (ou None si pas presente)
    - le type de probleme ('max' ou 'min')
    """
    with open(fichier, 'r') as f:
        lignes = f.readlines()
 
    # Nettoyer les lignes
    lignes = [ligne.strip() for ligne in lignes if ligne.strip() != '']
 
    n = int(lignes[0])  # nombre de sommets
    noms_sommets = lignes[1].split()
 
    # Verification
    if len(noms_sommets) != n:
        raise ValueError("Erreur : nombre de sommets incoherent avec les noms donnes.")
 
    # Lire matrice des capacites
    capacites = []
    for i in range(2, 2 + n):
        capacites.append(list(map(int, lignes[i].split())))
 
    # Detecter s'il y a une matrice de coûts
    couts = None
    type_probleme = 'max'  # par defaut : flot maximal
    if len(lignes) > 2 + n:
        if lignes[2 + n] == ' '.join(noms_sommets):
            couts = []
            for i in range(3 + n, 3 + 2 * n):
                couts.append(list(map(int, lignes[i].split())))
            type_probleme = 'min'  # flot à coût minimal detecte
 
    return noms_sommets, capacites, couts, type_probleme
 
def afficher_matrice(noms, matrice, titre):
    """
    Affiche une matrice avec colonnes parfaitement alignees,
    peu importe la taille des nombres (1, 2 ou 3 chiffres).
    """
    print(f"\n{titre}\n")
 
    # Calculer la largeur maximale d'affichage pour les nombres
    largeur = max(
        max(len(str(val)) for ligne in matrice for val in ligne),
        max(len(nom) for nom in noms),
        2  # minimum 2 caracteres pour lisibilite
    ) + 1  # petit bonus pour espace entre colonnes
 
    # En-tête
    print(" ".ljust(largeur), end="")
    for nom in noms:
        print(str(nom).rjust(largeur), end="")
    print()
 
    # Lignes
    for i, ligne in enumerate(matrice):
        print(str(noms[i]).ljust(largeur), end="")
        for val in ligne:
            print(str(val).rjust(largeur), end="")
        print()
 
# Exemple d'utilisation
if __name__ == "__main__":
    fichier = "../graphes/graphe1.txt"  # chemin d'un fichier graphe
    noms, capacites, couts, type_probleme = lire_graphe(fichier)
 
    print(f"Type de probleme detecte : {'Flot Maximal' if type_probleme == 'max' else 'Flot à Coût Minimal'}")
 
    afficher_matrice(noms, capacites, "Matrice des capacites")
    if couts:
        afficher_matrice(noms, couts, "Matrice des coûts")