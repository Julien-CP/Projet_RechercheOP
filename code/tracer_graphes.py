import csv
import matplotlib.pyplot as plt
import os
 
def lire_mesures(fichier_csv):
    """
    Lit un fichier de mesures et retourne les 100 listes de temps
    """
    temps_ff = []
    temps_pr = []
    temps_min = []
    rapport_ff_pr = []
 
    with open(fichier_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temps_ff.append(float(row["temps_FF"]))
            temps_pr.append(float(row["temps_PR"]))
            temps_min.append(float(row["temps_MIN"]))
            rapport_ff_pr.append(float(row["rapport_FF_PR"]))
 
    return temps_ff, temps_pr, temps_min, rapport_ff_pr
 
def tracer_nuages(tailles, mesures):
    """
    Trace les nuages de points avec même couleur par algorithme
    """
    plt.figure(figsize=(10,6))
 
    couleurs = {'ff': 'blue', 'pr': 'orange', 'min': 'green'}
    formes = {'ff': 'o', 'pr': 's', 'min': '^'}
    labels = {'ff': 'Ford-Fulkerson', 'pr': 'Push-Relabel', 'min': 'Min-Cost Flow'}
 
    for n in tailles:
        x = [n] * len(mesures[n]["ff"])
        plt.scatter(x, mesures[n]["ff"], color=couleurs['ff'], marker=formes['ff'], label=labels['ff'] if n == tailles[0] else "", s=15)
        plt.scatter(x, mesures[n]["pr"], color=couleurs['pr'], marker=formes['pr'], label=labels['pr'] if n == tailles[0] else "", s=15)
        plt.scatter(x, mesures[n]["min"], color=couleurs['min'], marker=formes['min'], label=labels['min'] if n == tailles[0] else "", s=15)
 
    plt.title("Nuage de points des temps d'exécution par algorithme")
    plt.xlabel("Nombre de sommets (n)")
    plt.ylabel("Temps d'exécution (secondes)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("../resultats/nuage_points_temp.png")
    plt.show()
 
import matplotlib.pyplot as plt
 
def tracer_nuages_separes(tailles, mesures):
    """
    Trace trois nuages de points séparés (un par algorithme) avec la même échelle
    """
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # 1 ligne, 3 colonnes
 
    algos = ['ff', 'pr', 'min']
    couleurs = {'ff': 'blue', 'pr': 'orange', 'min': 'green'}
    titres = {'ff': 'Ford-Fulkerson', 'pr': 'Push-Relabel', 'min': 'Min-Cost Flow'}
 
    # Trouver la valeur maximale Y de tous les temps pour fixer la même échelle
    tous_les_temps = []
    for n in tailles:
        tous_les_temps.extend(mesures[n]['ff'])
        tous_les_temps.extend(mesures[n]['pr'])
        tous_les_temps.extend(mesures[n]['min'])
    max_y = max(tous_les_temps)
 
    for i, algo in enumerate(algos):
        for n in tailles:
            x = [n] * len(mesures[n][algo])
            axs[i].scatter(x, mesures[n][algo], color=couleurs[algo], marker='o', s=15)
 
        axs[i].set_title(titres[algo])
        axs[i].set_xlabel('Nombre de sommets (n)')
        axs[i].set_ylabel('Temps (s)')
        axs[i].set_ylim(0, max_y * 1.1)  # même limite pour tous les graphes
        axs[i].grid(True)
 
    plt.tight_layout()
    plt.savefig("../resultats/nuage_points_temps_separes.png")
    plt.show()
def tracer_max_temps(tailles, mesures):
    """
    Trace la complexité dans le pire des cas pour chaque algorithme
    """
    max_ff = []
    max_pr = []
    max_min = []
 
    for n in tailles:
        max_ff.append(max(mesures[n]['ff']))
        max_pr.append(max(mesures[n]['pr']))
        max_min.append(max(mesures[n]['min']))
 
    plt.figure(figsize=(10,6))
    plt.plot(tailles, max_ff, marker='o', label='Ford-Fulkerson (max)')
    plt.plot(tailles, max_pr, marker='s', label='Push-Relabel (max)')
    plt.plot(tailles, max_min, marker='^', label='Min-Cost Flow (max)')
 
    plt.title("Complexité expérimentale dans le pire des cas")
    plt.xlabel("Nombre de sommets (n)")
    plt.ylabel("Temps maximal (secondes)")
    plt.grid(True)
    plt.legend()
    plt.xscale('log')  # très important car les tailles croissent beaucoup
    plt.yscale('log')  # pour mieux voir les tendances de complexité
    plt.tight_layout()
    plt.savefig("../resultats/complexite_pire_cas.png")
    plt.show()
 
def main():
    tailles = [10, 20, 40, 100]
    mesures = {}
 
    for n in tailles:
        fichier = f"../resultats/mesures_n{n}.csv"
        ff, pr, minc, rapport = lire_mesures(fichier)
        mesures[n] = {"ff": ff, "pr": pr, "min": minc, "rapport": rapport}
 
    tracer_nuages(tailles, mesures)
    tracer_max_temps(tailles, mesures)
    tracer_nuages_separes(tailles, mesures)
 
if __name__ == "__main__":
    main()
 
 