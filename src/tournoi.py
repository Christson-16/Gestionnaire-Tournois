"""
MODULE TOURNOI
Gère les tournois e-sport avec validation des règles
"""

class Tournoi:
    """
    Classe représentant un TOURNOI e-sport
    
    RÈGLES IMPORTANTES:
        1. Un tournoi peut être modifié SEULEMENT s'il n'a aucune équipe
        2. Dès qu'une équipe est ajoutée → modification interdite ❌
        3. Un tournoi ne peut être lancé que s'il est complet
           (nombre d'équipes = maximum)
        4. Après lancement → aucune modification possible
    
    Attributs privés:
        - _id_tournoi : Identifiant unique
        - _nom : Nom du tournoi
        - _date : Date du tournoi
        - _jeu : Jeu joué
        - _max_equipes : Nombre maximum d'équipes
        - _liste_equipes : Équipes inscrites
        - _liste_matchs : Matchs du tournoi
        - _statut : État du tournoi
    """
    
    def __init__(self, id_tournoi, nom, date, jeu, max_equipes):
        """
        Initialise un nouveau tournoi
        
        Args:
            id_tournoi (int): Identifiant unique
            nom (str): Nom du tournoi
            date (str): Date (format: JJ/MM/YYYY)
            jeu (str): Jeu joué
            max_equipes (int): Nombre maximum d'équipes
        """
        self._id_tournoi = id_tournoi
        self._nom = nom
        self._date = date
        self._jeu = jeu
        self._max_equipes = max(2, max_equipes)  # Au minimum 2
        self._liste_equipes = []
        self._liste_matchs = []
        self._statut = "Création"  # Création, Enregistrement, En Cours, Terminé
        self._vainqueur = None
        self._tour_actuel = 0
    
    # ============= GETTERS =============
    def get_id(self):
        """Retourne l'ID du tournoi"""
        return self._id_tournoi
    
    def get_nom(self):
        """Retourne le nom du tournoi"""
        return self._nom
    
    def get_date(self):
        """Retourne la date du tournoi"""
        return self._date
    
    def get_jeu(self):
        """Retourne le jeu joué"""
        return self._jeu
    
    def get_max_equipes(self):
        """Retourne le nombre maximum d'équipes"""
        return self._max_equipes
    
    def get_places_restantes(self):
        """
        Calcule le nombre de places restantes
        
        LOGIQUE:
            places_restantes = max_equipes - nombre_equipes_inscrites
        """
        return self._max_equipes - len(self._liste_equipes)
    
    def get_equipes(self):
        """Retourne la liste des équipes"""
        return self._liste_equipes
    
    def get_nombre_equipes(self):
        """Retourne le nombre d'équipes inscrites"""
        return len(self._liste_equipes)
    
    def get_matchs(self):
        """Retourne la liste des matchs"""
        return self._liste_matchs
    
    def get_nombre_matchs(self):
        """Retourne le nombre de matchs"""
        return len(self._liste_matchs)
    
    def get_statut(self):
        """Retourne le statut du tournoi"""
        return self._statut
    
    def get_vainqueur(self):
        """Retourne le vainqueur final (ou None)"""
        return self._vainqueur
    
    def est_complet(self):
        """
        Vérifie si le tournoi est complet
        
        LOGIQUE:
            complet = nombre_equipes == max_equipes
        """
        return self.get_nombre_equipes() == self._max_equipes
    
    def peut_etre_modifie(self):
        """
        Vérifie si le tournoi peut être modifié
        
        RÈGLE: Modification possible SEULEMENT si:
            - Aucune équipe inscrite
            - Statut = "Création"
        """
        return self.get_nombre_equipes() == 0 and self._statut == "Création"
    
    # ============= SETTERS =============
    def modifier_nom(self, nouveau_nom):
        """
        Change le nom du tournoi (SEULEMENT si possible de modifier)
        
        LOGIQUE:
            1. Vérifier si le tournoi peut être modifié
            2. Si oui → changer le nom
            3. Si non → afficher erreur
        """
        if not self.peut_etre_modifie():
            print("⚠ Impossible de modifier le tournoi (équipes déjà inscrites)")
            return False
        
        if nouveau_nom and len(nouveau_nom) > 0:
            self._nom = nouveau_nom
            return True
        return False
    
    def modifier_date(self, nouvelle_date):
        """Change la date (SEULEMENT si possible de modifier)"""
        if not self.peut_etre_modifie():
            print("⚠ Impossible de modifier le tournoi")
            return False
        
        self._date = nouvelle_date
        return True
    
    def modifier_jeu(self, nouveau_jeu):
        """Change le jeu (SEULEMENT si possible de modifier)"""
        if not self.peut_etre_modifie():
            print("⚠ Impossible de modifier le tournoi")
            return False
        
        self._jeu = nouveau_jeu
        return True
    
    def modifier_max_equipes(self, nouveau_max):
        """Change le nombre max d'équipes (SEULEMENT si possible de modifier)"""
        if not self.peut_etre_modifie():
            print("⚠ Impossible de modifier le tournoi")
            return False
        
        if nouveau_max >= 2:
            self._max_equipes = nouveau_max
            return True
        return False
    
    def changer_statut(self, nouveau_statut):
        """Change le statut du tournoi"""
        statuts_valides = ["Création", "Enregistrement", "En Cours", "Terminé"]
        if nouveau_statut in statuts_valides:
            self._statut = nouveau_statut
            return True
        return False
    
    # ============= GESTION DES ÉQUIPES =============
    def ajouter_equipe(self, equipe):
        """
        Ajoute une équipe au tournoi
        
        LOGIQUE:
            1. Vérifier qu'il reste des places
            2. Vérifier que l'équipe n'existe pas déjà
            3. Ajouter l'équipe
            4. Afficher confirmation
        
        Args:
            equipe (Equipe): L'équipe à ajouter
            
        Returns:
            bool: True si ajout réussi
        """
        # Vérifier les places
        if len(self._liste_equipes) >= self._max_equipes:
            print(f"⚠ Le tournoi est complet ({self._max_equipes} équipes max)")
            return False
        
        # Vérifier que l'équipe n'existe pas déjà
        for e in self._liste_equipes:
            if e.get_id() == equipe.get_id():
                print(f"⚠ L'équipe {equipe.get_nom()} est déjà inscrite")
                return False
        
        self._liste_equipes.append(equipe)
        places_restantes = self.get_places_restantes()
        
        print(f"✓ Équipe '{equipe.get_nom()}' ajoutée")
        print(f"  {len(self._liste_equipes)}/{self._max_equipes} équipes inscrites")
        
        if places_restantes == 0:
            print(f"✓ Le tournoi est maintenant COMPLET!")
            self._statut = "Enregistrement"
        
        return True
    
    def supprimer_equipe(self, id_equipe):
        """
        Supprime une équipe du tournoi
        
        LOGIQUE:
            1. Chercher l'équipe par ID
            2. Vérifier que le tournoi n'a pas commencé
            3. Supprimer
        """
        if self._statut != "Création" and self._statut != "Enregistrement":
            print("⚠ Impossible de supprimer une équipe (tournoi déjà lancé)")
            return False
        
        for i, equipe in enumerate(self._liste_equipes):
            if equipe.get_id() == id_equipe:
                equipe_supprimee = self._liste_equipes.pop(i)
                print(f"✓ Équipe {equipe_supprimee.get_nom()} supprimée")
                return True
        
        print(f"⚠ Équipe {id_equipe} non trouvée")
        return False
    
    def ajouter_match(self, match):
        """Ajoute un match au tournoi"""
        self._liste_matchs.append(match)
    
    def lancer_tournoi(self):
        """
        Lance le tournoi (SEULEMENT s'il est complet)
        
        RÈGLE: Le tournoi ne peut être lancé que si:
            - Nombre d'équipes = Max d'équipes
            - Statut = "Enregistrement"
        """
        if not self.est_complet():
            print(f"⚠ Le tournoi n'est pas complet ({self.get_nombre_equipes()}/{self._max_equipes})")
            return False
        
        self._statut = "En Cours"
        self._tour_actuel = 1
        print(f"✓ Tournoi lancé! {self.get_nombre_equipes()} équipes en lice")
        return True
    
    def terminer_tournoi(self, vainqueur):
        """Termine le tournoi et enregistre le vainqueur"""
        self._statut = "Terminé"
        self._vainqueur = vainqueur
        vainqueur.changer_statut("Champion")
        print(f"🏆 TOURNOI TERMINÉ!")
        print(f"🏆 Vainqueur: {vainqueur.get_nom()}")
    
    # ============= AFFICHAGE =============
    def afficher_info(self):
        """Affiche les informations complètes du tournoi"""
        print(f"\n{'='*60}")
        print(f"🎮 TOURNOI: {self._nom}")
        print(f"{'='*60}")
        print(f"ID: {self._id_tournoi}")
        print(f"Date: {self._date}")
        print(f"Jeu: {self._jeu}")
        print(f"Équipes: {self.get_nombre_equipes()}/{self._max_equipes}")
        print(f"Places restantes: {self.get_places_restantes()}")
        print(f"Matchs: {self.get_nombre_matchs()}")
        print(f"Statut: {self._statut}")
        if self._vainqueur:
            print(f"Vainqueur: {self._vainqueur.get_nom()}")
    
    def afficher_equipes(self):
        """Affiche toutes les équipes inscrites"""
        print(f"\n📋 ÉQUIPES DU TOURNOI {self._nom}:")
        if len(self._liste_equipes) == 0:
            print("   (Aucune équipe)")
            return
        
        for i, equipe in enumerate(self._liste_equipes, 1):
            statut_emoji = "🔴" if equipe.get_statut() == "Éliminée" else "🟢"
            print(f"   {i}. {statut_emoji} {equipe.get_nom()} (Niveau: {equipe.get_niveau()})")
    
    def afficher_matchs(self):
        """Affiche tous les matchs du tournoi"""
        print(f"\n⚽ MATCHS DU TOURNOI {self._nom}:")
        if len(self._liste_matchs) == 0:
            print("   (Aucun match)")
            return
        
        for match in self._liste_matchs:
            match.afficher_compact()
    
    def __str__(self):
        """Représentation textuelle courte"""
        return f"Tournoi '{self._nom}' ({self.get_nombre_equipes()}/{self._max_equipes} équipes)"
    
    def __repr__(self):
        """Représentation pour débogage"""
        return f"Tournoi(id={self._id_tournoi}, nom='{self._nom}')"