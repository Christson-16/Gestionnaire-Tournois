"""
MODULE ÉQUIPE
Gère les équipes dans le système de tournois e-sport
"""

class Equipe:
    """
    Classe représentant une ÉQUIPE dans le tournoi
    
    Attributs privés:
        - _id_equipe : Identifiant unique
        - _nom_equipe : Nom de l'équipe
        - _liste_joueurs : Liste des joueurs
        - _niveau : Force de l'équipe (0-100)
        - _matchs_gagnes : Matchs gagnés
        - _matchs_perdus : Matchs perdus
        - _historique_matchs : Résultats des matchs
        - _statut : État de l'équipe
    """
    
    def __init__(self, id_equipe, nom_equipe, niveau=50):
        """
        Initialise une nouvelle équipe
        
        Args:
            id_equipe (int): Identifiant unique
            nom_equipe (str): Nom de l'équipe
            niveau (int): Niveau de force (0-100, par défaut 50)
        """
        self._id_equipe = id_equipe
        self._nom_equipe = nom_equipe
        self._liste_joueurs = []
        self._niveau = max(0, min(100, niveau))  # Entre 0 et 100
        self._matchs_gagnes = 0
        self._matchs_perdus = 0
        self._historique_matchs = []
        self._statut = "Active"  # Active, Éliminée, Champion
    
    # ============= GETTERS =============
    def get_id(self):
        """Retourne l'ID de l'équipe"""
        return self._id_equipe
    
    def get_nom(self):
        """Retourne le nom de l'équipe"""
        return self._nom_equipe
    
    def get_niveau(self):
        """Retourne le niveau de force (0-100)"""
        return self._niveau
    
    def get_joueurs(self):
        """Retourne la liste des joueurs"""
        return self._liste_joueurs
    
    def get_nombre_joueurs(self):
        """Retourne le nombre de joueurs dans l'équipe"""
        return len(self._liste_joueurs)
    
    def get_matchs_gagnes(self):
        """Retourne le nombre de matchs gagnés"""
        return self._matchs_gagnes
    
    def get_matchs_perdus(self):
        """Retourne le nombre de matchs perdus"""
        return self._matchs_perdus
    
    def get_total_matchs(self):
        """Retourne le nombre total de matchs joués"""
        return self._matchs_gagnes + self._matchs_perdus
    
    def get_taux_victoire(self):
        """Calcule le taux de victoire de l'équipe"""
        total = self.get_total_matchs()
        if total == 0:
            return 0.0
        return (self._matchs_gagnes / total) * 100
    
    def get_statut(self):
        """Retourne le statut actuel de l'équipe"""
        return self._statut
    
    def get_historique(self):
        """Retourne l'historique des matchs de l'équipe"""
        return self._historique_matchs
    
    # ============= SETTERS =============
    def modifier_nom(self, nouveau_nom):
        """
        Change le nom de l'équipe
        
        Args:
            nouveau_nom (str): Nouveau nom
            
        Returns:
            bool: True si succès
        """
        if nouveau_nom and len(nouveau_nom) > 0:
            self._nom_equipe = nouveau_nom
            return True
        return False
    
    def modifier_niveau(self, nouveau_niveau):
        """
        Change le niveau de force de l'équipe
        
        Args:
            nouveau_niveau (int): Niveau (0-100)
            
        Returns:
            bool: True si succès
        """
        if 0 <= nouveau_niveau <= 100:
            self._niveau = nouveau_niveau
            return True
        return False
    
    def changer_statut(self, nouveau_statut):
        """
        Change le statut de l'équipe
        
        Args:
            nouveau_statut (str): 'Active', 'Éliminée' ou 'Champion'
            
        Returns:
            bool: True si succès
        """
        statuts_valides = ["Active", "Éliminée", "Champion"]
        if nouveau_statut in statuts_valides:
            self._statut = nouveau_statut
            return True
        return False
    
    # ============= GESTION DES JOUEURS =============
    def ajouter_joueur(self, joueur):
        """
        Ajoute un joueur à l'équipe
        
        LOGIQUE:
            1. Vérifier que le joueur n'est pas déjà dans l'équipe
            2. Ajouter à la liste
            3. Afficher confirmation
        
        Args:
            joueur (Joueur): Le joueur à ajouter
            
        Returns:
            bool: True si succès
        """
        # Vérifier que le joueur n'existe pas déjà
        for j in self._liste_joueurs:
            if j.get_id() == joueur.get_id():
                print(f"⚠ {joueur.get_pseudo()} est déjà dans {self._nom_equipe}")
                return False
        
        self._liste_joueurs.append(joueur)
        print(f"✓ {joueur.get_pseudo()} ajouté à {self._nom_equipe}")
        return True
    
    def supprimer_joueur(self, id_joueur):
        """
        Supprime un joueur de l'équipe
        
        LOGIQUE:
            1. Chercher le joueur par ID
            2. Si trouvé → supprimer
            3. Si non trouvé → message d'erreur
        
        Args:
            id_joueur (int): ID du joueur à supprimer
            
        Returns:
            bool: True si suppression réussie
        """
        for i, joueur in enumerate(self._liste_joueurs):
            if joueur.get_id() == id_joueur:
                joueur_supprime = self._liste_joueurs.pop(i)
                print(f"✓ {joueur_supprime.get_pseudo()} supprimé de {self._nom_equipe}")
                return True
        
        print(f"⚠ Joueur {id_joueur} non trouvé")
        return False
    
    def modifier_joueur(self, id_joueur, nouveau_pseudo=None, nouvel_email=None):
        """
        Modifie les infos d'un joueur dans l'équipe
        
        Args:
            id_joueur (int): ID du joueur
            nouveau_pseudo (str): Nouveau pseudo (optionnel)
            nouvel_email (str): Nouvel email (optionnel)
            
        Returns:
            bool: True si modification réussie
        """
        for joueur in self._liste_joueurs:
            if joueur.get_id() == id_joueur:
                if nouveau_pseudo:
                    joueur.modifier_pseudo(nouveau_pseudo)
                if nouvel_email:
                    joueur.modifier_email(nouvel_email)
                print(f"✓ Joueur {id_joueur} modifié")
                return True
        
        print(f"⚠ Joueur {id_joueur} non trouvé")
        return False
    
    def afficher_joueurs(self):
        """Affiche tous les joueurs de l'équipe"""
        print(f"\n👥 JOUEURS DE {self._nom_equipe}:")
        if len(self._liste_joueurs) == 0:
            print("   (Aucun joueur)")
            return
        
        for i, joueur in enumerate(self._liste_joueurs, 1):
            print(f"   {i}. {joueur.get_pseudo()} ({joueur.get_niveau()})")
    
    # ============= MÉTHODES MÉTIER =============
    def ajouter_victoire(self, match_id=None):
        """Enregistre une victoire de l'équipe"""
        self._matchs_gagnes += 1
        if match_id:
            self._historique_matchs.append({
                "match_id": match_id,
                "resultat": "✓ Victoire"
            })
    
    def ajouter_defaite(self, match_id=None):
        """Enregistre une défaite de l'équipe"""
        self._matchs_perdus += 1
        if match_id:
            self._historique_matchs.append({
                "match_id": match_id,
                "resultat": "✗ Défaite"
            })
    
    # ============= AFFICHAGE =============
    def afficher_info(self):
        """Affiche toutes les informations de l'équipe"""
        print(f"\n{'='*50}")
        print(f"⚽ ÉQUIPE: {self._nom_equipe}")
        print(f"{'='*50}")
        print(f"ID: {self._id_equipe}")
        print(f"Niveau: {self._niveau}/100")
        print(f"Statut: {self._statut}")
        print(f"Nombre de joueurs: {self.get_nombre_joueurs()}")
        print(f"Matchs gagnés: {self._matchs_gagnes}")
        print(f"Matchs perdus: {self._matchs_perdus}")
        print(f"Taux de victoire: {self.get_taux_victoire():.1f}%")
        
        self.afficher_joueurs()
    
    def __str__(self):
        """Représentation textuelle courte"""
        return f"{self._nom_equipe} (Niveau: {self._niveau})"
    
    def __repr__(self):
        """Représentation pour débogage"""
        return f"Equipe(id={self._id_equipe}, nom='{self._nom_equipe}')"