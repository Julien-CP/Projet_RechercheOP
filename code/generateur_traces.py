import sys
import os
from lecteur_graphe import lire_graphe
from ford_fulkerson import ford_fulkerson
from push_relabel import push_relabel
from min_cost_flow import min_cost_flow
 
# Dossier où seront stockees les traces
trace_folder = "../traces"
os.makedirs(trace_folder, exist_ok=True)
 
# Configuration de ton equipe
groupe = "F"
equipe = "4"
 
# Valeurs de flot souhaite pour les graphes de coût minimal
# (à adapter si necessaire selon ton projet ou les consignes donnees)
valeurs_flots = {
    6: 5,
    7: 7,
    8: 10,
    9: 10,
    10: 10
}
 
def rediriger_sortie(nom_fichier):
    """
    Redirige la sortie standard vers un fichier
    """
    sys.stdout = open(os.path.join(trace_folder, nom_fichier), 'w')
 
def restaurer_sortie():
    """
    Restaure la sortie standard vers la console
    """
    sys.stdout.close()
    sys.stdout = sys.__stdout__
 
def traiter_graphe(num_graphe):
    fichier = f"../graphes/graphe{num_graphe}.txt"
    noms, capacites, couts, type_probleme = lire_graphe(fichier)
 
    if type_probleme == 'max':
        # Flot maximal -> Ford-Fulkerson
        nom_trace_ff = f"{groupe}{equipe}-trace{num_graphe}-FF.txt"
        rediriger_sortie(nom_trace_ff)
        print(f"=== Graphe {num_graphe} - Ford-Fulkerson ===")
        ford_fulkerson(noms, capacites)
        restaurer_sortie()
 
        # Flot maximal -> Push-Relabel
        nom_trace_pr = f"{groupe}{equipe}-trace{num_graphe}-PR.txt"
        rediriger_sortie(nom_trace_pr)
        print(f"=== Graphe {num_graphe} - Push-Relabel ===")
        push_relabel(noms, capacites)
        restaurer_sortie()
 
    elif type_probleme == 'min':
        # Flot à coût minimal -> Min-Cost Flow
        nom_trace_min = f"{groupe}{equipe}-trace{num_graphe}-MIN.txt"
        rediriger_sortie(nom_trace_min)
        print(f"=== Graphe {num_graphe} - Flot à Coût Minimal ===")
        valeur_flot = valeurs_flots.get(num_graphe, 5)  # 5 par defaut si pas precise
        min_cost_flow(noms, capacites, couts, valeur_flot)
        restaurer_sortie()
 
def main():
    print("=== Lancement de la generation des traces ===\n")
    for num_graphe in range(1, 11):
        print(f"Traitement du graphe {num_graphe}...")
        traiter_graphe(num_graphe)
    print("\n=== Toutes les traces ont ete generees avec succes ===")
 
if __name__ == "__main__":
    main()
 