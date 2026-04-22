

class Joueur:
    
    def __init__(self, id_joueur, pseudo, email, niveau):
       
        self._id_joueur = id_joueur
        self._pseudo = pseudo
        self._email = email
        self._niveau = niveau
        self._matchs_gagnes = 0
        self._matchs_perdus = 0
        self._historique_matchs = []
    
    # ============= GETTERS (Lecteurs) =============
    def get_id(self):

        return self._id_joueur
    
    def get_pseudo(self):
       
        return self._pseudo
    
    def get_email(self):
       
        return self._email
    
    def get_niveau(self):
        
        return self._niveau
    
    def get_matchs_gagnes(self):
       
        return self._matchs_gagnes
    
    def get_matchs_perdus(self):
       
        return self._matchs_perdus
    
    def get_total_matchs(self):
        
        return self._matchs_gagnes + self._matchs_perdus
    
    def get_taux_victoire(self):
        
        total = self.get_total_matchs()
        if total == 0:
            return 0.0
        return (self._matchs_gagnes / total) * 100
    
    def get_historique(self):
       
        return self._historique_matchs
    
    # ============= SETTERS (Modificateurs) =============
    def modifier_pseudo(self, nouveau_pseudo):
       
        if nouveau_pseudo and len(nouveau_pseudo) > 0:
            self._pseudo = nouveau_pseudo
            return True
        return False
    
    def modifier_email(self, nouvel_email):
        
        if nouvel_email and "@" in nouvel_email:
            self._email = nouvel_email
            return True
        return False
    
    def modifier_niveau(self, nouveau_niveau):
        
        niveaux_valides = ["débutant", "intermédiaire", "expert"]
        if nouveau_niveau.lower() in niveaux_valides:
            self._niveau = nouveau_niveau.lower()
            return True
        return False
    
    # ============= MÉTHODES MÉTIER =============
    def ajouter_victoire(self, match_id=None):
        
        self._matchs_gagnes += 1
        if match_id:
            self._historique_matchs.append({
                "match_id": match_id,
                "resultat": "✓ Victoire",
                "type": "victoire"
            })
    
    def ajouter_defaite(self, match_id=None):
        
        self._matchs_perdus += 1
        if match_id:
            self._historique_matchs.append({
                "match_id": match_id,
                "resultat": "✗ Défaite",
                "type": "defaite"
            })
    
    def afficher_info(self):
       
        print(f"\n{'='*50}")
        print(f"JOUEUR: {self._pseudo}")
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
       
        return f"{self._pseudo} ({self._niveau})"
    
    def __repr__(self):
        
        return f"Joueur(id={self._id_joueur}, pseudo='{self._pseudo}')"