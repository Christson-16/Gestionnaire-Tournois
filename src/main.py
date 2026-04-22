# Point d'entrée du programme - Menu interactif

from joueur import Joueur
from equipe import Equipe
from match import Match
from tournoi import Tournoi
from bracket import Bracket

# Variables globales
tournoi_actuel = None
compteur_joueur = 1
compteur_equipe = 1
compteur_match = 1
compteur_bracket = 1

# Fonction pour afficher le menu principal
def afficher_menu_principal():
    print("\n" + "="*60)
    print("       GESTIONNAIRE DE TOURNOIS E-SPORT")
    print("="*60)
    print("1. Créer un nouveau tournoi")
    print("2. Ajouter une équipe au tournoi")
    print("3. Ajouter un joueur à une équipe")
    print("4. Afficher les équipes du tournoi")
    print("5. Générer le bracket")
    print("6. Afficher le bracket et les matchs")
    print("7. Enregistrer un résultat de match")
    print("8. Afficher les statistiques du tournoi")
    print("9. Quitter")
    print("="*60)

# Fonction pour créer un tournoi
def creer_tournoi():
    global tournoi_actuel
    
    print("\n--- CRÉER UN NOUVEAU TOURNOI ---")
    nom = input("Nom du tournoi: ")
    date = input("Date du tournoi (JJ/MM/YYYY): ")
    jeu = input("Jeu joué (ex: League of Legends): ")
    
    try:
        max_participants = int(input("Nombre maximum d'équipes: "))
    except:
        print("Erreur: Veuillez entrer un nombre valide")
        return
    
    tournoi_actuel = Tournoi(1, nom, date, jeu, max_participants)
    print(f"\n✓ Tournoi '{nom}' créé avec succès!")

# Fonction pour ajouter une équipe
def ajouter_equipe():
    global tournoi_actuel, compteur_equipe
    
    if tournoi_actuel is None:
        print("\n⚠ Erreur: Créez d'abord un tournoi!")
        return
    
    print("\n--- AJOUTER UNE ÉQUIPE ---")
    nom_equipe = input("Nom de l'équipe: ")
    
    equipe = Equipe(compteur_equipe, nom_equipe)
    tournoi_actuel.ajouter_equipe(equipe)
    compteur_equipe += 1
    print(f"✓ Équipe '{nom_equipe}' ajoutée!")

# Fonction pour ajouter un joueur à une équipe
def ajouter_joueur():
    global tournoi_actuel, compteur_joueur
    
    if tournoi_actuel is None:
        print("\n⚠ Erreur: Créez d'abord un tournoi!")
        return
    
    if len(tournoi_actuel.liste_equipes) == 0:
        print("\n⚠ Erreur: Créez d'abord une équipe!")
        return
    
    print("\n--- AJOUTER UN JOUEUR À UNE ÉQUIPE ---")
    
    # Afficher les équipes disponibles
    print("\nÉquipes disponibles:")
    for i, equipe in enumerate(tournoi_actuel.liste_equipes):
        print(f"{i+1}. {equipe.nom_equipe}")
    
    try:
        choix = int(input("Choisir une équipe (numéro): ")) - 1
        if choix < 0 or choix >= len(tournoi_actuel.liste_equipes):
            print("⚠ Choix invalide!")
            return
    except:
        print("⚠ Erreur: Veuillez entrer un nombre valide")
        return
    
    equipe_selectionnee = tournoi_actuel.liste_equipes[choix]
    
    # Créer le joueur
    pseudo = input("Pseudo du joueur: ")
    email = input("Email du joueur: ")
    
    print("Niveau du joueur:")
    print("1. Débutant")
    print("2. Intermédiaire")
    print("3. Expert")
    
    try:
        niveau_choix = int(input("Choisir le niveau (1-3): "))
        niveaux = {1: "débutant", 2: "intermédiaire", 3: "expert"}
        if niveau_choix not in niveaux:
            print("⚠ Choix invalide!")
            return
        niveau = niveaux[niveau_choix]
    except:
        print("⚠ Erreur: Veuillez entrer un nombre valide")
        return
    
    joueur = Joueur(compteur_joueur, pseudo, email, niveau)
    equipe_selectionnee.ajouter_joueur(joueur)
    compteur_joueur += 1
    print(f"\n✓ Joueur '{pseudo}' ajouté à '{equipe_selectionnee.nom_equipe}'!")

# Fonction pour afficher les équipes
def afficher_equipes():
    global tournoi_actuel
    
    if tournoi_actuel is None:
        print("\n⚠ Erreur: Créez d'abord un tournoi!")
        return
    
    print("\n--- ÉQUIPES DU TOURNOI ---")
    if len(tournoi_actuel.liste_equipes) == 0:
        print("⚠ Aucune équipe pour le moment")
        return
    
    for equipe in tournoi_actuel.liste_equipes:
        print(f"\n📋 {equipe.nom_equipe}:")
        if len(equipe.liste_joueurs) == 0:
            print("   (Aucun joueur)")
        else:
            for joueur in equipe.liste_joueurs:
                print(f"   - {joueur.pseudo} ({joueur.niveau})")

# Fonction pour générer le bracket
def generer_bracket():
    global tournoi_actuel, compteur_bracket
    
    if tournoi_actuel is None:
        print("\n⚠ Erreur: Créez d'abord un tournoi!")
        return
    
    if len(tournoi_actuel.liste_equipes) < 2:
        print("\n⚠ Erreur: Il faut au moins 2 équipes!")
        return
    
    print("\n--- GÉNÉRER LE BRACKET ---")
    bracket = Bracket(compteur_bracket, tournoi_actuel, "simple")
    bracket.generer_bracket_simple()
    compteur_bracket += 1
    print("✓ Bracket généré avec succès!")

# Fonction pour afficher le bracket
def afficher_bracket():
    global tournoi_actuel
    
    if tournoi_actuel is None:
        print("\n⚠ Erreur: Créez d'abord un tournoi!")
        return
    
    if len(tournoi_actuel.liste_matchs) == 0:
        print("\n⚠ Aucun match pour le moment. Générez d'abord le bracket!")
        return
    
    print("\n" + "="*60)
    print("                     BRACKET DU TOURNOI")
    print("="*60)
    
    for match in tournoi_actuel.liste_matchs:
        match.afficher_info()
        print("-"*60)

# Fonction pour enregistrer un résultat
def enregistrer_resultat():
    global tournoi_actuel
    
    if tournoi_actuel is None:
        print("\n⚠ Erreur: Créez d'abord un tournoi!")
        return
    
    if len(tournoi_actuel.liste_matchs) == 0:
        print("\n⚠ Aucun match disponible!")
        return
    
    print("\n--- ENREGISTRER UN RÉSULTAT ---")
    print("\nMatchs en attente:")
    
    matchs_en_attente = [m for m in tournoi_actuel.liste_matchs if m.statut == "En attente"]
    
    if len(matchs_en_attente) == 0:
        print("⚠ Tous les matchs sont terminés!")
        return
    
    for i, match in enumerate(matchs_en_attente):
        nom1 = match.get_nom(match.participant1)
        nom2 = match.get_nom(match.participant2)
        print(f"{i+1}. Match {match.id_match}: {nom1} vs {nom2}")
    
    try:
        choix_match = int(input("Choisir un match (numéro): ")) - 1
        if choix_match < 0 or choix_match >= len(matchs_en_attente):
            print("⚠ Choix invalide!")
            return
    except:
        print("⚠ Erreur: Veuillez entrer un nombre valide")
        return
    
    match = matchs_en_attente[choix_match]
    
    nom1 = match.get_nom(match.participant1)
    nom2 = match.get_nom(match.participant2)
    
    print(f"\nMatch: {nom1} vs {nom2}")
    print("1. Victoire de " + nom1)
    print("2. Victoire de " + nom2)
    
    try:
        choix_gagnant = int(input("Choisir le gagnant (1 ou 2): "))
        if choix_gagnant == 1:
            gagnant = match.participant1
        elif choix_gagnant == 2:
            gagnant = match.participant2
        else:
            print("⚠ Choix invalide!")
            return
    except:
        print("⚠ Erreur: Veuillez entrer un nombre valide")
        return
    
    match.enregistrer_resultat(gagnant)
    print("✓ Résultat enregistré!")

# Fonction pour afficher les statistiques
def afficher_statistiques():
    global tournoi_actuel
    
    if tournoi_actuel is None:
        print("\n⚠ Erreur: Créez d'abord un tournoi!")
        return
    
    print("\n" + "="*60)
    print("               STATISTIQUES DU TOURNOI")
    print("="*60)
    tournoi_actuel.afficher_info()
    
    print("\n--- CLASSEMENT PAR ÉQUIPE ---")
    equipes_triees = sorted(tournoi_actuel.liste_equipes, 
                           key=lambda e: e.matchs_gagnes, 
                           reverse=True)
    
    for i, equipe in enumerate(equipes_triees, 1):
        taux = (equipe.matchs_gagnes / (equipe.matchs_gagnes + equipe.matchs_perdus) * 100 
                if (equipe.matchs_gagnes + equipe.matchs_perdus) > 0 else 0)
        print(f"{i}. {equipe.nom_equipe}: {equipe.matchs_gagnes}V - {equipe.matchs_perdus}D ({taux:.1f}%)")

# Fonction principale
def main():
    while True:
        afficher_menu_principal()
        choix = input("Votre choix (1-9): ")
        
        if choix == "1":
            creer_tournoi()
        elif choix == "2":
            ajouter_equipe()
        elif choix == "3":
            ajouter_joueur()
        elif choix == "4":
            afficher_equipes()
        elif choix == "5":
            generer_bracket()
        elif choix == "6":
            afficher_bracket()
        elif choix == "7":
            enregistrer_resultat()
        elif choix == "8":
            afficher_statistiques()
        elif choix == "9":
            print("\n✓ Au revoir!")
            break
        else:
            print("\n⚠ Choix invalide! Veuillez réessayer.")

# Exécuter le programme
if __name__ == "__main__":
    main()