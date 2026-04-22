import random

class Match:
    
    def __init__(self, id_match, participant1, participant2, tour=""):
    
        self._id_match = id_match
        self._participant1 = participant1
        self._participant2 = participant2
        self._gagnant = None
        self._tour = tour
        self._statut = "En attente"  # En attente, Simulé, Joué
        self._score_p1 = 0
        self._score_p2 = 0
    
    # ============= GETTERS =============
    def get_id(self):
        
        return self._id_match
    
    def get_participant1(self):
        
        return self._participant1
    
    def get_participant2(self):
         
        return self._participant2
    
    def get_gagnant(self):
     
        return self._gagnant
    
    def get_statut(self):
         
        return self._statut
    
    def get_tour(self):
        
        return self._tour
    
    def get_nom(self, participant):
       
        if hasattr(participant, 'get_nom'):  # C'est une Équipe
            return participant.get_nom()
        elif hasattr(participant, 'get_pseudo'):  # C'est un Joueur
            return participant.get_pseudo()
        else:
            return str(participant)
    
    def get_niveau(self, participant):
       
        if hasattr(participant, 'get_niveau'):
            return participant.get_niveau()
        return 0
    
    # ============= SIMULATION DU MATCH =============
    def simuler_match(self):
       
        # Récupérer les niveaux
        niveau_p1 = self.get_niveau(self._participant1)
        niveau_p2 = self.get_niveau(self._participant2)
        
        # Calculer le total
        total = niveau_p1 + niveau_p2
        
        # Si total est 0 (cas edge) → match aléatoire
        if total == 0:
            total = 1
            niveau_p1 = 0.5
            niveau_p2 = 0.5
        
        # Générer un nombre aléatoire entre 0 et total
        nombre_aleatoire = random.uniform(0, total)
        
        # Déterminer le gagnant
        if nombre_aleatoire <= niveau_p1:
            self._gagnant = self._participant1
            probabilite = (niveau_p1 / total) * 100
        else:
            self._gagnant = self._participant2
            probabilite = (niveau_p2 / total) * 100
        
        # Enregistrer les résultats
        self._participant1.ajouter_victoire(self._id_match) if self._gagnant == self._participant1 else self._participant1.ajouter_defaite(self._id_match)
        self._participant2.ajouter_victoire(self._id_match) if self._gagnant == self._participant2 else self._participant2.ajouter_defaite(self._id_match)
        
        self._statut = "Simulé"
        
        return self._gagnant
    
    def enregistrer_resultat_manuel(self, gagnant):
       
        if gagnant == self._participant1:
            self._gagnant = self._participant1
            self._participant1.ajouter_victoire(self._id_match)
            self._participant2.ajouter_defaite(self._id_match)
            self._statut = "Joué"
            return True
        elif gagnant == self._participant2:
            self._gagnant = self._participant2
            self._participant2.ajouter_victoire(self._id_match)
            self._participant1.ajouter_defaite(self._id_match)
            self._statut = "Joué"
            return True
        else:
            print("Le gagnant doit être un des participants")
            return False
    
    # ============= AFFICHAGE =============
    def afficher_info(self):
        
        nom1 = self.get_nom(self._participant1)
        nom2 = self.get_nom(self._participant2)
        niveau1 = self.get_niveau(self._participant1)
        niveau2 = self.get_niveau(self._participant2)
        
        print(f"\n{'='*60}")
        print(f" MATCH {self._id_match} {self._tour}")
        print(f"{'='*60}")
        print(f"{nom1:20} ({niveau1:3}/100) vs {nom2:20} ({niveau2:3}/100)")
        print(f"Statut: {self._statut}")
        
        if self._gagnant:
            nom_gagnant = self.get_nom(self._gagnant)
            print(f" Gagnant: {nom_gagnant}")
        else:
            print(f"Gagnant: Pas encore déterminé")
    
    def afficher_compact(self):
        
        nom1 = self.get_nom(self._participant1)
        nom2 = self.get_nom(self._participant2)
        
        if self._gagnant:
            nom_gagnant = self.get_nom(self._gagnant)
            print(f"  {nom1:25} vs {nom2:25} →  {nom_gagnant}")
        else:
            print(f"  {nom1:25} vs {nom2:25} → [En attente]")
    
    def __str__(self):

        nom1 = self.get_nom(self._participant1)
        nom2 = self.get_nom(self._participant2)
        return f"Match {self._id_match}: {nom1} vs {nom2}"
    
    def __repr__(self):
        
        return f"Match(id={self._id_match}, statut='{self._statut}')"