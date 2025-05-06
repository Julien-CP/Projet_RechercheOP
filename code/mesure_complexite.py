import time
import random
import csv
import os
from lecteur_graphe import afficher_matrice
from ford_fulkerson import ford_fulkerson
from push_relabel import push_relabel
from min_cost_flow import min_cost_flow
from generer_probleme import generer_probleme_flot
 
def mesurer_temps_algorithmes(n, nb_tests=100):
    """
    Mesure les temps d'exécution pour Ford-Fulkerson, Push-Relabel, Min-Cost Flow
    sur nb_tests problèmes de flot aléatoires de taille n.
    """
    resultats = []  # Pour stocker toutes les mesures
 
    for _ in range(nb_tests):
        # Générer un problème aléatoire
        capacites, couts = generer_probleme_flot(n, avec_couts=True)
        noms = [f"v{i}" for i in range(n)]
        noms[0] = 's'
        noms[-1] = 't'
 
        # Copies de matrices
        capacites_ff = [row[:] for row in capacites]
        capacites_pr = [row[:] for row in capacites]
        capacites_min = [row[:] for row in capacites]
        couts_min = [row[:] for row in couts]
 
        # Ford-Fulkerson
        start = time.process_time()
        ford_fulkerson(noms, capacites_ff)
        end = time.process_time()
        temps_ff = end - start
 
        # Push-Relabel
        start = time.process_time()
        push_relabel(noms, capacites_pr)
        end = time.process_time()
        temps_pr = end - start
 
        # Min-Cost Flow
        flot_max = ford_fulkerson(noms, capacites_min)
        flot_demande = flot_max // 2
 
        start = time.process_time()
        min_cost_flow(noms, capacites_min, couts_min, flot_demande)
        end = time.process_time()
        temps_min = end - start
 
        # Calcul du rapport θFF/θPR (attention à éviter division par zéro)
        if temps_pr > 0:
            rapport_ff_pr = temps_ff / temps_pr
        else:
            rapport_ff_pr = 0
 
        # Stocker la ligne complète
        resultats.append([n, temps_ff, temps_pr, temps_min, rapport_ff_pr])
 
    return resultats
 
def sauver_resultats(resultats, fichier_csv):
    """
    Sauvegarde toutes les mesures dans un fichier CSV
    """
    with open(fichier_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["n", "temps_FF", "temps_PR", "temps_MIN", "rapport_FF_PR"])
        writer.writerows(resultats)
 
def main():
    tailles = [10, 20, 40, 100, 400, 1000, 4000, 10000]
    nb_tests_par_taille = 100
    os.makedirs("../resultats", exist_ok=True)
 
    for n in tailles:
        print(f"Mesure pour n={n} sommets...")
        resultats_n = mesurer_temps_algorithmes(n, nb_tests_par_taille)
        fichier_csv = f"../resultats/mesures_n{n}.csv"
        sauver_resultats(resultats_n, fichier_csv)
 
    print("\n=== Toutes les mesures sont terminées ===")
 
if __name__ == "__main__":
    main()
 