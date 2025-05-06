from lecteur_graphe import lire_graphe, afficher_matrice
from ford_fulkerson import ford_fulkerson
from push_relabel import push_relabel
from min_cost_flow import min_cost_flow 
def main():
    print("=== Projet de Recherche Opérationnelle ===\n")
 
    continuer = True
    while continuer:
        print("\nQuel graphe voulez-vous tester ?")
        graphe_numero = input("Entrez le numéro du graphe (1-10) : ").strip()
 
        fichier = f"../graphes/graphe{graphe_numero}.txt"
 
        try:
            noms, capacites, couts, type_probleme = lire_graphe(fichier)
        except Exception as e:
            print(f"Erreur : {e}")
            continue
 
        print(f"\n> Type de problème détecté : {'Flot Maximal' if type_probleme == 'max' else 'Flot à Coût Minimal'}")
        afficher_matrice(noms, capacites, "Matrice des capacités")
        if couts:
            afficher_matrice(noms, couts, "Matrice des coûts")
 
        if type_probleme == 'max':
            print("\nQuel algorithme voulez-vous utiliser ?")
            print(" 1 - Ford-Fulkerson")
            print(" 2 - Push-Relabel")
            choix_algo = input("Entrez votre choix (1 ou 2) : ").strip()
 
            if choix_algo == "1":
                print("\n[INFO] Déroulement de Ford-Fulkerson ")
                ford_fulkerson(noms, capacites)
            elif choix_algo == "2":
                print("\n[INFO] Déroulement de Push-Relabel ")
                push_relabel(noms, capacites)
            else:
                print("Choix invalide.")
                continue
 
        else:  # Problème de coût minimal
            print("\nQuel est la valeur de flot que vous souhaitez envoyer ?")
            valeur_flot = input("Entrez la valeur du flot souhaité (nombre entier) : ").strip()
 
            try:
                valeur_flot = int(valeur_flot)
            except ValueError:
                print("Erreur : veuillez entrer un nombre entier.")
                continue
 
            print(f"\n[INFO] Déroulement de Flot à Coût Minimal pour {valeur_flot} unités ")
            min_cost_flow(noms, capacites, couts, valeur_flot)
 
        # À la fin, demander si l'utilisateur veut recommencer
        continuer_choix = input("\nVoulez-vous tester un autre problème ? (o/n) : ").strip().lower()
        if continuer_choix != 'o':
            continuer = False
 
    print("\n=== Fin du programme ===")
 
if __name__ == "__main__":
    main()