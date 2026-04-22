from joueur import Joueur
from equipe import Equipe
from match import Match
from tournoi import Tournoi
from bracket import Bracket

# ============= VARIABLES GLOBALES =============
liste_tournois = []  
tournoi_actuel = None 
bracket_actuel = None  

compteur_joueur = 1
compteur_equipe = 1
compteur_tournoi = 1
compteur_bracket = 1

# ============= MENU PRINCIPAL =============
def afficher_menu_principal():
    print("\n" + "="*70)
    print("          GESTIONNAIRE DE TOURNOIS E-SPORT ")
    print("="*70)
    
    if tournoi_actuel:
        print(f" Tournoi actif: {tournoi_actuel.get_nom()} ({tournoi_actuel.get_statut()})")
    else:
        print("⚪ Aucun tournoi sélectionné")
    
    print("\n MENU PRINCIPAL:")
    print("  1. Gérer les tournois")
    print("  2. Gérer équipes et joueurs")
    print("  3. Générer le bracket")
    print("  4. Simuler les matchs")
    print("  5. Afficher statistiques")
    print("  6. Quitter")
    print("="*70)

def afficher_menu_tournois():
    print("\n" + "="*70)
    print("          GESTION DES TOURNOIS")
    print("="*70)
    print("  1. Créer un tournoi")
    print("  2. Liste des tournois")
    print("  3. Sélectionner")
    print("  4. Supprimer")
    print("  5. Infos tournoi actif")
    print("  6. Retour")
    print("="*70)

def afficher_sous_menu_equipes():
    print("\n" + "="*70)
    print("          GESTION DES ÉQUIPES ET JOUEURS")
    print("="*70)
    print("  1. Ajouter équipe")
    print("  2. Afficher équipes")
    print("  3. Ajouter joueur")
    print("  4. Modifier joueur")
    print("  5. Supprimer joueur")
    print("  6. Supprimer équipe")
    print("  7. Retour")
    print("="*70)

def afficher_sous_menu_matchs():
    print("\n" + "="*70)
    print("          GESTION DES MATCHS")
    print("="*70)
    print("  1. Afficher bracket")
    print("  2. Simuler tour")
    print("  3. Tour suivant")
    print("  4. Stats bracket")
    print("  5. Retour")
    print("="*70)

# ============= TOURNOIS =============
def creer_tournoi():
    global tournoi_actuel, compteur_tournoi
    
    nom = input("Nom: ").strip()
    if not nom: return
    
    date = input("Date: ").strip()
    if not date: return
    
    jeu = input("Jeu: ").strip()
    if not jeu: return
    
    max_equipes = int(input("Max équipes: "))
    if max_equipes < 2: return
    
    t = Tournoi(compteur_tournoi, nom, date, jeu, max_equipes)
    liste_tournois.append(t)
    tournoi_actuel = t
    compteur_tournoi += 1

def afficher_liste_tournois():
    for i, t in enumerate(liste_tournois, 1):
        print(f"{i}. {t.get_nom()}")

def selectionner_tournoi():
    global tournoi_actuel
    
    afficher_liste_tournois()
    choix = int(input("Choix: ")) - 1
    
    if 0 <= choix < len(liste_tournois):
        tournoi_actuel = liste_tournois[choix]

def supprimer_tournoi():
    global tournoi_actuel
    
    afficher_liste_tournois()
    choix = int(input("Supprimer: ")) - 1
    
    if 0 <= choix < len(liste_tournois):
        liste_tournois.pop(choix)

def afficher_info_tournoi_actif():
    if tournoi_actuel:
        tournoi_actuel.afficher_info()

# ============= ÉQUIPES =============
def ajouter_equipe():
    global compteur_equipe
    
    nom = input("Nom équipe: ")
    niveau = int(input("Niveau: "))
    
    e = Equipe(compteur_equipe, nom, niveau)
    tournoi_actuel.ajouter_equipe(e)
    compteur_equipe += 1

def afficher_equipes():
    tournoi_actuel.afficher_equipes()

def supprimer_equipe():
    id_equipe = int(input("ID équipe: "))
    tournoi_actuel.supprimer_equipe(id_equipe)

# ============= JOUEURS =============
def ajouter_joueur():
    global compteur_joueur
    
    afficher_equipes()
    choix = int(input("Équipe: ")) - 1
    equipe = tournoi_actuel.get_equipes()[choix]
    
    pseudo = input("Pseudo: ")
    email = input("Email: ")
    
    niveau_map = {1: "débutant", 2: "intermédiaire", 3: "expert"}
    niveau = niveau_map[int(input("Niveau (1-3): "))]
    
    j = Joueur(compteur_joueur, pseudo, email, niveau)
    equipe.ajouter_joueur(j)
    compteur_joueur += 1

def modifier_joueur():
    afficher_equipes()
    choix = int(input("Équipe: ")) - 1
    equipe = tournoi_actuel.get_equipes()[choix]
    
    id_joueur = int(input("ID joueur: "))
    pseudo = input("Pseudo: ")
    email = input("Email: ")
    
    equipe.modifier_joueur(id_joueur, pseudo, email)

def supprimer_joueur():
    afficher_equipes()
    choix = int(input("Équipe: ")) - 1
    equipe = tournoi_actuel.get_equipes()[choix]
    
    id_joueur = int(input("ID joueur: "))
    equipe.supprimer_joueur(id_joueur)

# ============= BRACKET =============
def generer_bracket():
    global bracket_actuel, compteur_bracket
    
    bracket_actuel = Bracket(compteur_bracket, tournoi_actuel, "simple")
    compteur_bracket += 1
    bracket_actuel.generer_bracket_simple()

def afficher_bracket():
    bracket_actuel.afficher_bracket_actuel()

def simuler_matchs():
    bracket_actuel.simuler_tous_matchs_tour(bracket_actuel.get_tour_actuel())

def progresser_tournoi():
    bracket_actuel.progresser_tournoi()

def afficher_stats_bracket():
    bracket_actuel.afficher_statistiques_bracket()

# ============= STATS =============
def afficher_stats_tournoi():
    tournoi_actuel.afficher_info()

# ============= MAIN =============
def main():
    while True:
        afficher_menu_principal()
        choix = input("Choix: ")
        
        if choix == "1":
            while True:
                afficher_menu_tournois()
                c = input("Choix: ")
                if c == "1": creer_tournoi()
                elif c == "2": afficher_liste_tournois()
                elif c == "3": selectionner_tournoi()
                elif c == "4": supprimer_tournoi()
                elif c == "5": afficher_info_tournoi_actif()
                elif c == "6": break
        
        elif choix == "2":
            while True:
                afficher_sous_menu_equipes()
                c = input("Choix: ")
                if c == "1": ajouter_equipe()
                elif c == "2": afficher_equipes()
                elif c == "3": ajouter_joueur()
                elif c == "4": modifier_joueur()
                elif c == "5": supprimer_joueur()
                elif c == "6": supprimer_equipe()
                elif c == "7": break
        
        elif choix == "3":
            generer_bracket()
        
        elif choix == "4":
            while True:
                afficher_sous_menu_matchs()
                c = input("Choix: ")
                if c == "1": afficher_bracket()
                elif c == "2": simuler_matchs()
                elif c == "3": progresser_tournoi()
                elif c == "4": afficher_stats_bracket()
                elif c == "5": break
        
        elif choix == "5":
            afficher_stats_tournoi()
        
        elif choix == "6":
            break

if __name__ == "__main__":
    main()