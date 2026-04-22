"""
MODULE JOUEUR
Gère les joueurs dans le système de tournois e-sport
"""

class Joueur:
    """
    Classe représentant un JOUEUR dans le tournoi
    
    Attributs privés:
        - _id_joueur : Identifiant unique
        - _pseudo : Surnom du joueur
        - _email : Email du joueur
        - _niveau : Niveau de compétence
        - _matchs_gagnes : Nombre de matchs gagnés
        - _matchs_perdus : Nombre de matchs perdus
        - _historique_matchs : Liste des résultats
    """
    
    def __init__(self, id_joueur, pseudo, email, niveau):
        """
        Initialise un nouveau joueur
        
        Args:
            id_joueur (int): Identifiant unique
            pseudo (str): Surnom du joueur
            email (str): Email du joueur
            niveau (str): Niveau (débutant, intermédiaire, expert)
        """
        self._id_joueur = id_joueur
        self._pseudo = pseudo
        self._email = email
        self._niveau = niveau
        self._matchs_gagnes = 0
        self._matchs_perdus = 0
        self._historique_matchs = []
    
    # ============= GETTERS (Lecteurs) =============
    def get_id(self):
        """Retourne l'ID du joueur"""
        return self._id_joueur
    
    def get_pseudo(self):
        """Retourne le pseudo du joueur"""
        return self._pseudo
    
    def get_email(self):
        """Retourne l'email du joueur"""
        return self._email
    
    def get_niveau(self):
        """Retourne le niveau du joueur"""
        return self._niveau
    
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
        """
        Calcule le taux de victoire en pourcentage
        
        Logique:
            - Si aucun match joué → 0%
            - Sinon → (victoires / total) * 100
        """
        total = self.get_total_matchs()
        if total == 0:
            return 0.0
        return (self._matchs_gagnes / total) * 100
    
    def get_historique(self):
        """Retourne l'historique complet des matchs"""
        return self._historique_matchs
    
    # ============= SETTERS (Modificateurs) =============
    def modifier_pseudo(self, nouveau_pseudo):
        """
        Change le pseudo du joueur
        
        Args:
            nouveau_pseudo (str): Nouveau pseudo
            
        Returns:
            bool: True si succès, False sinon
        """
        if nouveau_pseudo and len(nouveau_pseudo) > 0:
            self._pseudo = nouveau_pseudo
            return True
        return False
    
    def modifier_email(self, nouvel_email):
        """
        Change l'email du joueur (avec vérification)
        
        Args:
            nouvel_email (str): Nouvel email
            
        Returns:
            bool: True si succès, False sinon
        """
        if nouvel_email and "@" in nouvel_email:
            self._email = nouvel_email
            return True
        return False
    
    def modifier_niveau(self, nouveau_niveau):
        """
        Change le niveau du joueur
        
        Args:
            nouveau_niveau (str): Nouveau niveau
            
        Returns:
            bool: True si succès, False sinon
        """
        niveaux_valides = ["débutant", "intermédiaire", "expert"]
        if nouveau_niveau.lower() in niveaux_valides:
            self._niveau = nouveau_niveau.lower()
            return True
        return False
    
    # ============= MÉTHODES MÉTIER =============
    def ajouter_victoire(self, match_id=None):
        """
        Enregistre une victoire
        
        LOGIQUE:
            1. Incrémenter le compteur de victoires
            2. Ajouter à l'historique
        
        Args:
            match_id (int): ID du match (optionnel)
        """
        self._matchs_gagnes += 1
        if match_id:
            self._historique_matchs.append({
                "match_id": match_id,
                "resultat": "✓ Victoire",
                "type": "victoire"
            })
    
    def ajouter_defaite(self, match_id=None):
        """
        Enregistre une défaite
        
        LOGIQUE:
            1. Incrémenter le compteur de défaites
            2. Ajouter à l'historique
        
        Args:
            match_id (int): ID du match (optionnel)
        """
        self._matchs_perdus += 1
        if match_id:
            self._historique_matchs.append({
                "match_id": match_id,
                "resultat": "✗ Défaite",
                "type": "defaite"
            })
    
    def afficher_info(self):
        """Affiche toutes les informations du joueur"""
        print(f"\n{'='*50}")
        print(f"👤 JOUEUR: {self._pseudo}")
        print(f"{'='*50}")
        print(f"ID: {self._id_joueur}")
        print(f"Email: {self._email}")
        print(f"Niveau: {self._niveau.upper()}")
        print(f"Matchs gagnés: {self._matchs_gagnes}")
        print(f"Matchs perdus: {self._matchs_perdus}")
        print(f"Taux de victoire: {self.get_taux_victoire():.1f}%")
        
        if self._historique_matchs:
            print(f"\nHistorique ({len(self._historique_matchs)} matchs):")
            for i, match in enumerate(self._historique_matchs, 1):
                print(f"  {i}. Match {match['match_id']}: {match['resultat']}")
    
    def __str__(self):
        """Représentation textuelle courte du joueur"""
        return f"{self._pseudo} ({self._niveau})"
    
    def __repr__(self):
        """Représentation pour débogage"""
        return f"Joueur(id={self._id_joueur}, pseudo='{self._pseudo}')"