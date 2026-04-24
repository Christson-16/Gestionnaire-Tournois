"""
MENU PRINCIPAL - GESTIONNAIRE DE TOURNOIS E-SPORT
Application interactive avec gestion de PLUSIEURS tournois
Avec persistance des données en SQLite
"""

from joueur import Joueur
from equipe import Equipe
from match import Match
from tournoi import Tournoi
from bracket import Bracket
from data_manager import DataManager

# ============= VARIABLES GLOBALES =============
liste_tournois = []
tournoi_actuel = None
bracket_actuel = None

compteur_joueur = 1
compteur_equipe = 1
compteur_tournoi = 1
compteur_bracket = 1

# ✅ INITIALISER LE GESTIONNAIRE DE DONNÉES
data_manager = DataManager("tournois.db")

# ============= MENU PRINCIPAL =============
def afficher_menu_principal():
    print("\n" + "="*70)
    print("         🎮 GESTIONNAIRE DE TOURNOIS E-SPORT 🎮")
    print("="*70)
    
    if tournoi_actuel:
        print(f"🔴 Tournoi actif: {tournoi_actuel.get_nom()} ({tournoi_actuel.get_statut()})")
    else:
        print("⚪ Aucun tournoi sélectionné")
    
    print("\n🏠 MENU PRINCIPAL:")
    print("  1. Gérer les tournois (créer, sélectionner, supprimer)")
    print("  2. Gérer équipes et joueurs")
    print("  3. Générer le bracket")
    print("  4. Simuler les matchs")
    print("  5. Afficher statistiques")
    print("  6. 💾 Sauvegarder les données")
    print("  7. 📂 Charger les données")
    print("  8. Quitter")
    print("="*70)

def afficher_menu_tournois():
    print("\n" + "="*70)
    print("         🏆 GESTION DES TOURNOIS")
    print("="*70)
    print("  1. Créer un nouveau tournoi")
    print("  2. Afficher la liste des tournois")
    print("  3. Sélectionner un tournoi")
    print("  4. Supprimer un tournoi")
    print("  5. Afficher infos du tournoi actif")
    print("  6. Retour au menu principal")
    print("="*70)

def afficher_sous_menu_equipes():
    print("\n" + "="*70)
    print("         👥 GESTION DES ÉQUIPES ET JOUEURS")
    print("="*70)
    print("  1. Ajouter une équipe")
    print("  2. Afficher les équipes")
    print("  3. Ajouter un joueur à une équipe")
    print("  4. Modifier un joueur")
    print("  5. Supprimer un joueur")
    print("  6. Supprimer une équipe")
    print("  7. Retour au menu principal")
    print("="*70)

def afficher_sous_menu_matchs():
    print("\n" + "="*70)
    print("         ⚽ GESTION DES MATCHS")
    print("="*70)
    print("  1. Afficher le bracket actuel")
    print("  2. Simuler tous les matchs du tour")
    print("  3. Passer au tour suivant")
    print("  4. Afficher statistiques du bracket")
    print("  5. Retour au menu principal")
    print("="*70)

# ============= GESTION DES TOURNOIS =============
def creer_tournoi():
    global tournoi_actuel, compteur_tournoi
    
    print("\n" + "="*70)
    print("         🏆 CRÉER UN NOUVEAU TOURNOI")
    print("="*70)
    
    nom = input("\n📝 Nom du tournoi: ").strip()
    if not nom:
        print("⚠ Le nom ne peut pas être vide")
        return
    
    date = input("📅 Date (JJ/MM/YYYY): ").strip()
    if not date:
        print("⚠ La date ne peut pas être vide")
        return
    
    jeu = input("🎮 Jeu joué (ex: League of Legends): ").strip()
    if not jeu:
        print("⚠ Le jeu ne peut pas être vide")
        return
    
    try:
        max_equipes = int(input("👥 Nombre maximum d'équipes (minimum 2): "))
        if max_equipes < 2:
            print("⚠ Le minimum est 2 équipes")
            return
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")
        return
    
    nouveau_tournoi = Tournoi(compteur_tournoi, nom, date, jeu, max_equipes)
    liste_tournois.append(nouveau_tournoi)
    tournoi_actuel = nouveau_tournoi
    compteur_tournoi += 1
    
    print(f"\n✅ Tournoi '{nom}' créé avec succès!")
    nouveau_tournoi.afficher_info()

def afficher_liste_tournois():
    if len(liste_tournois) == 0:
        print("\n⚠ Aucun tournoi créé")
        return
    
    print("\n" + "="*70)
    print("         📋 LISTE DES TOURNOIS")
    print("="*70)
    
    for i, t in enumerate(liste_tournois, 1):
        statut_emoji = "🟢" if t.get_statut() == "En Cours" else "🟡" if t.get_statut() == "Enregistrement" else "🔴"
        actif = "⭐ ACTIF" if t == tournoi_actuel else ""
        print(f"\n{i}. {statut_emoji} {t.get_nom()} {actif}")
        print(f"   Jeu: {t.get_jeu()}")
        print(f"   Équipes: {t.get_nombre_equipes()}/{t.get_max_equipes()}")
        print(f"   Statut: {t.get_statut()}")

def selectionner_tournoi():
    global tournoi_actuel
    
    if len(liste_tournois) == 0:
        print("\n⚠ Aucun tournoi créé")
        return
    
    afficher_liste_tournois()
    
    try:
        choix = int(input("\n🎯 Choisir un tournoi (numéro): ")) - 1
        if 0 <= choix < len(liste_tournois):
            tournoi_actuel = liste_tournois[choix]
            print(f"\n✅ Tournoi '{tournoi_actuel.get_nom()}' sélectionné!")
        else:
            print("⚠ Choix invalide!")
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")

def supprimer_tournoi():
    global tournoi_actuel
    
    if len(liste_tournois) == 0:
        print("\n⚠ Aucun tournoi créé")
        return
    
    afficher_liste_tournois()
    
    try:
        choix = int(input("\n🗑️ Choisir un tournoi à supprimer (numéro): ")) - 1
        if 0 <= choix < len(liste_tournois):
            tournoi_supprime = liste_tournois.pop(choix)
            print(f"\n✅ Tournoi '{tournoi_supprime.get_nom()}' supprimé!")
            
            if tournoi_actuel == tournoi_supprime:
                tournoi_actuel = liste_tournois[0] if liste_tournois else None
        else:
            print("⚠ Choix invalide!")
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")

def afficher_info_tournoi_actif():
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    print("\n")
    tournoi_actuel.afficher_info()

# ============= GESTION DES ÉQUIPES =============
def ajouter_equipe():
    global compteur_equipe
    
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    if tournoi_actuel.get_statut() == "En Cours":
        print("\n⚠ ❌ Impossible d'ajouter une équipe (tournoi en cours)")
        return
    
    print("\n" + "="*70)
    print("         ➕ AJOUTER UNE ÉQUIPE")
    print("="*70)
    
    nom_equipe = input("\n📝 Nom de l'équipe: ").strip()
    if not nom_equipe:
        print("⚠ Le nom ne peut pas être vide")
        return
    
    try:
        niveau = int(input("💪 Niveau de force (0-100): "))
        if not (0 <= niveau <= 100):
            print("⚠ Le niveau doit être entre 0 et 100")
            return
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")
        return
    
    equipe = Equipe(compteur_equipe, nom_equipe, niveau)
    tournoi_actuel.ajouter_equipe(equipe)
    compteur_equipe += 1

def afficher_equipes():
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    print("\n")
    tournoi_actuel.afficher_equipes()

def supprimer_equipe():
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    afficher_equipes()
    
    try:
        id_equipe = int(input("\n🗑️ ID de l'équipe à supprimer: "))
        tournoi_actuel.supprimer_equipe(id_equipe)
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")

# ============= GESTION DES JOUEURS =============
def ajouter_joueur():
    global compteur_joueur
    
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    if tournoi_actuel.get_nombre_equipes() == 0:
        print("\n⚠ ❌ Créez d'abord une équipe!")
        return
    
    print("\n" + "="*70)
    print("         ➕ AJOUTER UN JOUEUR À UNE ÉQUIPE")
    print("="*70)
    
    afficher_equipes()
    
    try:
        choix = int(input("\n👥 Choisir une équipe (numéro): ")) - 1
        if choix < 0 or choix >= tournoi_actuel.get_nombre_equipes():
            print("⚠ Choix invalide!")
            return
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")
        return
    
    equipe_selectionnee = tournoi_actuel.get_equipes()[choix]
    
    pseudo = input("\n📝 Pseudo du joueur: ").strip()
    if not pseudo:
        print("⚠ Le pseudo ne peut pas être vide")
        return
    
    email = input("📧 Email du joueur: ").strip()
    if "@" not in email:
        print("⚠ Email invalide")
        return
    
    print("\n💪 Niveau du joueur:")
    print("  1. Débutant")
    print("  2. Intermédiaire")
    print("  3. Expert")
    
    try:
        niveau_choix = int(input("Choisir le niveau (1-3): "))
        niveaux = {1: "débutant", 2: "intermédiaire", 3: "expert"}
        if niveau_choix not in niveaux:
            print("⚠ Choix invalide!")
            return
        niveau = niveaux[niveau_choix]
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")
        return
    
    joueur = Joueur(compteur_joueur, pseudo, email, niveau)
    equipe_selectionnee.ajouter_joueur(joueur)
    compteur_joueur += 1

def modifier_joueur():
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    print("\n" + "="*70)
    print("         ✏️ MODIFIER UN JOUEUR")
    print("="*70)
    
    afficher_equipes()
    
    try:
        choix_equipe = int(input("\n👥 Choisir une équipe (numéro): ")) - 1
        if choix_equipe < 0 or choix_equipe >= tournoi_actuel.get_nombre_equipes():
            print("⚠ Choix invalide!")
            return
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")
        return
    
    equipe = tournoi_actuel.get_equipes()[choix_equipe]
    equipe.afficher_joueurs()
    
    try:
        id_joueur = int(input("\n👤 ID du joueur à modifier: "))
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")
        return
    
    nouveau_pseudo = input("Nouveau pseudo (vide pour ne pas modifier): ").strip()
    nouvel_email = input("Nouvel email (vide pour ne pas modifier): ").strip()
    
    equipe.modifier_joueur(id_joueur, nouveau_pseudo if nouveau_pseudo else None,
                          nouvel_email if nouvel_email else None)

def supprimer_joueur():
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    print("\n" + "="*70)
    print("         🗑️ SUPPRIMER UN JOUEUR")
    print("="*70)
    
    afficher_equipes()
    
    try:
        choix_equipe = int(input("\n👥 Choisir une équipe (numéro): ")) - 1
        if choix_equipe < 0 or choix_equipe >= tournoi_actuel.get_nombre_equipes():
            print("⚠ Choix invalide!")
            return
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")
        return
    
    equipe = tournoi_actuel.get_equipes()[choix_equipe]
    equipe.afficher_joueurs()
    
    try:
        id_joueur = int(input("\n🗑️ ID du joueur à supprimer: "))
        equipe.supprimer_joueur(id_joueur)
    except ValueError:
        print("⚠ Veuillez entrer un nombre valide")

# ============= GESTION DU BRACKET =============
def generer_bracket():
    global bracket_actuel, compteur_bracket
    
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    if not tournoi_actuel.est_complet():
        print(f"\n⚠ ❌ Le tournoi n'est pas complet")
        print(f"   {tournoi_actuel.get_nombre_equipes()}/{tournoi_actuel.get_max_equipes()} équipes")
        return
    
    if not tournoi_actuel.lancer_tournoi():
        return
    
    bracket_actuel = Bracket(compteur_bracket, tournoi_actuel, "simple")
    compteur_bracket += 1
    
    bracket_actuel.generer_bracket_simple()

def afficher_bracket():
    if bracket_actuel is None:
        print("\n⚠ ❌ Générez d'abord un bracket!")
        return
    
    bracket_actuel.afficher_bracket_actuel()

def simuler_matchs():
    if bracket_actuel is None:
        print("\n⚠ ❌ Générez d'abord un bracket!")
        return
    
    gagnants = bracket_actuel.simuler_tous_matchs_tour(bracket_actuel.get_tour_actuel())
    
    if len(gagnants) > 1:
        print("\n✅ Tour simulé avec succès!")
    else:
        print("\n🏆 TOURNOI TERMINÉ!")

def progresser_tournoi():
    if bracket_actuel is None:
        print("\n⚠ ❌ Générez d'abord un bracket!")
        return
    
    if bracket_actuel.progresser_tournoi():
        print(f"\n✅ Passé au tour {bracket_actuel.get_tour_actuel()}")
        bracket_actuel.afficher_bracket_actuel()
    else:
        print("\n🏆 Tournoi terminé!")

def afficher_stats_bracket():
    if bracket_actuel is None:
        print("\n⚠ ❌ Générez d'abord un bracket!")
        return
    
    bracket_actuel.afficher_statistiques_bracket()

# ============= STATISTIQUES =============
def afficher_stats_tournoi():
    if tournoi_actuel is None:
        print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
        return
    
    print("\n" + "="*70)
    print("         📊 STATISTIQUES DU TOURNOI")
    print("="*70)
    
    tournoi_actuel.afficher_info()
    
    print("\n📋 DÉTAILS DES ÉQUIPES:")
    for equipe in tournoi_actuel.get_equipes():
        print(f"\n  ⚽ {equipe.get_nom()}:")
        print(f"     Niveau: {equipe.get_niveau()}/100")
        print(f"     Joueurs: {equipe.get_nombre_joueurs()}")
        print(f"     Matchs gagnés: {equipe.get_matchs_gagnes()}")
        print(f"     Taux victoire: {equipe.get_taux_victoire():.1f}%")

# ============= SAUVEGARDE ET CHARGEMENT =============
def sauvegarder_donnees():
    """Sauvegarde tous les tournois et leurs données"""
    print("\n" + "="*70)
    print("         💾 SAUVEGARDE DES DONNÉES")
    print("="*70)
    
    if len(liste_tournois) == 0:
        print("\n⚠ Aucun tournoi à sauvegarder")
        return
    
    data_manager.sauvegarder_tout(liste_tournois)
    print(f"✅ {len(liste_tournois)} tournoi(s) sauvegardé(s) dans 'tournois.db'")

def charger_donnees():
    """Charge les tournois depuis la base de données"""
    global liste_tournois, tournoi_actuel
    
    print("\n" + "="*70)
    print("         📂 CHARGEMENT DES DONNÉES")
    print("="*70)
    
    tournois_charges = data_manager.charger_tournois()
    
    if len(tournois_charges) > 0:
        liste_tournois = tournois_charges
        tournoi_actuel = liste_tournois[0]
        print(f"✅ {len(tournois_charges)} tournoi(s) chargé(s)")
    else:
        print("\n⚠ Aucun tournoi trouvé dans la base")

# ============= FONCTION PRINCIPALE =============
def main():
    while True:
        afficher_menu_principal()
        choix = input("Votre choix (1-8): ").strip()
        
        if choix == "1":
            while True:
                afficher_menu_tournois()
                sous_choix = input("Votre choix (1-6): ").strip()
                
                if sous_choix == "1":
                    creer_tournoi()
                elif sous_choix == "2":
                    afficher_liste_tournois()
                elif sous_choix == "3":
                    selectionner_tournoi()
                elif sous_choix == "4":
                    supprimer_tournoi()
                elif sous_choix == "5":
                    afficher_info_tournoi_actif()
                elif sous_choix == "6":
                    break
                else:
                    print("⚠ Choix invalide!")
        
        elif choix == "2":
            if tournoi_actuel is None:
                print("\n⚠ ❌ Sélectionnez d'abord un tournoi!")
                continue
            
            while True:
                afficher_sous_menu_equipes()
                sous_choix = input("Votre choix (1-7): ").strip()
                
                if sous_choix == "1":
                    ajouter_equipe()
                elif sous_choix == "2":
                    afficher_equipes()
                elif sous_choix == "3":
                    ajouter_joueur()
                elif sous_choix == "4":
                    modifier_joueur()
                elif sous_choix == "5":
                    supprimer_joueur()
                elif sous_choix == "6":
                    supprimer_equipe()
                elif sous_choix == "7":
                    break
                else:
                    print("⚠ Choix invalide!")
        
        elif choix == "3":
            generer_bracket()
        
        elif choix == "4":
            if bracket_actuel is None:
                print("\n⚠ ❌ Générez d'abord un bracket!")
                continue
            
            while True:
                afficher_sous_menu_matchs()
                sous_choix = input("Votre choix (1-5): ").strip()
                
                if sous_choix == "1":
                    afficher_bracket()
                elif sous_choix == "2":
                    simuler_matchs()
                elif sous_choix == "3":
                    progresser_tournoi()
                elif sous_choix == "4":
                    afficher_stats_bracket()
                elif sous_choix == "5":
                    break
                else:
                    print("⚠ Choix invalide!")
        
        elif choix == "5":
            afficher_stats_tournoi()
        
        elif choix == "6":
            sauvegarder_donnees()
        
        elif choix == "7":
            charger_donnees()
        
        elif choix == "8":
            print("\n👋 Au revoir!")
            print("💾 Sauvegarde automatique en cours...")
            sauvegarder_donnees()
            break
        
        else:
            print("\n⚠ Choix invalide!")

# ============= POINT D'ENTRÉE =============
if __name__ == "__main__":
    print("\n🎮 Bienvenue dans le Gestionnaire de Tournois E-Sport!")
    print("   Appuyez sur Entrée pour commencer...")
    input()
    main()