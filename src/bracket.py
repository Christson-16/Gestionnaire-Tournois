import random
from match import Match

class Bracket:
    
    
    def __init__(self, id_bracket, tournoi, type_elimination="simple"):
      
        self._id_bracket = id_bracket
        self._tournoi = tournoi
        self._type_elimination = type_elimination
        self._matchs_par_tour = {}  # {tour: [matches]}
        self._equipes_actives = []  # Équipes encore en lice
        self._vainqueurs_tours = {}  # {tour: [gagnants]}
        self._tour_actuel = 0
        self._id_match_counter = 1
    
    # ============= GETTERS =============
    def get_id(self):
      
        return self._id_bracket
    
    def get_type(self):
      
        return self._type_elimination
    
    def get_equipes_actives(self):
       
        return self._equipes_actives
    
    def get_matchs_tour(self, num_tour):
     
        return self._matchs_par_tour.get(num_tour, [])
    
    def get_tour_actuel(self):
        
        return self._tour_actuel
    
    # ============= GÉNÉRATION DU BRACKET =============
    def generer_bracket_simple(self):
    
        if not self._tournoi.est_complet():
            print(" Le tournoi n'est pas complet")
            return False
        
        # Initialiser les équipes actives
        self._equipes_actives = list(self._tournoi.get_equipes())
        self._tour_actuel = 1
        
        # Générer les matchs du premier tour
        self._generer_matchs_tour(self._tour_actuel)
        
        print(f"\n✓ Bracket généré!")
        self.afficher_bracket_actuel()
        
        return True
    
    def _generer_matchs_tour(self, num_tour):
        
        equipes = list(self._equipes_actives)
        matchs_tour = []
        gagnants_tour = []
        
        # Nombre d'équipes
        nb_equipes = len(equipes)
        
        # Cas IMPAIR: ajouter un BYE
        equipe_bye = None
        if nb_equipes % 2 == 1:
            equipe_bye = random.choice(equipes)
            equipes.remove(equipe_bye)
            gagnants_tour.append(equipe_bye)
            print(f"\n BYE TOUR {num_tour}: {equipe_bye.get_nom()} passe directement")
        
        # Créer les matchs pour les équipes restantes
        for i in range(0, len(equipes), 2):
            if i + 1 < len(equipes):
                match = Match(
                    self._id_match_counter,
                    equipes[i],
                    equipes[i + 1],
                    f"Tour {num_tour}"
                )
                matchs_tour.append(match)
                self._tournoi.ajouter_match(match)
                self._id_match_counter += 1
        
        # Enregistrer dans le dictionnaire
        self._matchs_par_tour[num_tour] = matchs_tour
        self._vainqueurs_tours[num_tour] = gagnants_tour
    
    # ============= SIMULATION ET PROGRESSION =============
    def simuler_tous_matchs_tour(self, num_tour):
     
        matchs = self.get_matchs_tour(num_tour)
        gagnants = list(self._vainqueurs_tours.get(num_tour, []))  # Inclure les BYE
        
        print(f"\n{'='*60}")
        print(f"SIMULATION TOUR {num_tour}")
        print(f"{'='*60}\n")
        
        for match in matchs:
            # Simuler
            gagnant = match.simuler_match()
            gagnants.append(gagnant)
            
            # Afficher
            nom1 = match.get_nom(match.get_participant1())
            nom2 = match.get_nom(match.get_participant2())
            nom_gagnant = match.get_nom(gagnant)
            print(f"  {nom1:20} vs {nom2:20} → ✓ {nom_gagnant}")
        
        # Mettre à jour les équipes actives
        self._equipes_actives = gagnants
        
        print(f"\n→ {len(gagnants)} équipes qualifiées pour le prochain tour")
        
        return gagnants
    
    def progresser_tournoi(self):
       
        nb_equipes = len(self._equipes_actives)
        
        if nb_equipes == 1:
            # Tournoi terminé!
            vainqueur = self._equipes_actives[0]
            self._tournoi.terminer_tournoi(vainqueur)
            return False
        
        # Passer au tour suivant
        self._tour_actuel += 1
        self._generer_matchs_tour(self._tour_actuel)
        
        return True
    
    # ============= AFFICHAGE =============
    def afficher_bracket_actuel(self):
   
        matchs = self.get_matchs_tour(self._tour_actuel)
        gagnants_bye = self._vainqueurs_tours.get(self._tour_actuel, [])
        
        print(f"\n{'='*60}")
        print(f"TOUR {self._tour_actuel}")
        print(f"{'='*60}")
        
        # Afficher BYE s'il y en a
        if gagnants_bye:
            print(f"\n ÉQUIPE EN BYE:")
            for equipe in gagnants_bye:
                if equipe not in [m.get_participant1() for m in matchs] and \
                   equipe not in [m.get_participant2() for m in matchs]:
                    print(f"   {equipe.get_nom()}")
        
        # Afficher les matchs
        if matchs:
            print(f"\n MATCHS:")
            for match in matchs:
                match.afficher_compact()
        else:
            print("\n   (Aucun match)")
    
    def afficher_bracket_complet(self):
      
        print(f"\n{'='*60}")
        print(f"BRACKET COMPLET")
        print(f"{'='*60}")
        
        for tour in sorted(self._matchs_par_tour.keys()):
            print(f"\nTOUR {tour}:")
            self.afficher_bracket_actuel()
    
    def afficher_statistiques_bracket(self):
    
        print(f"\n{'='*60}")
        print(f"STATISTIQUES DU BRACKET")
        print(f"{'='*60}")
        print(f"Équipes restantes: {len(self._equipes_actives)}")
        print(f"Tour actuel: {self._tour_actuel}")
        print(f"Nombre total de matchs: {sum(len(m) for m in self._matchs_par_tour.values())}")
        
        print(f"\nÉquipes encore en lice:")
        for equipe in self._equipes_actives:
            print(f"  - {equipe.get_nom()} (Gagnés: {equipe.get_matchs_gagnes()})")
    
    def __str__(self):
       
        return f"Bracket (Tour {self._tour_actuel}, {len(self._equipes_actives)} équipes actives)"