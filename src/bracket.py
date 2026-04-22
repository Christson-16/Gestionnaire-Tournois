 # Classe pour générer et gérer le BRACKET (tableau des matchs)

class Bracket:
    
    # Fonction pour créer un bracket
    def __init__(self, id_bracket, tournoi, type_elimination):
        self.id_bracket = id_bracket            # Un numéro unique pour le bracket
        self.tournoi = tournoi                  # Le tournoi auquel appartient ce bracket
        self.type_elimination = type_elimination  # Type: "simple" ou "double"
        self.liste_matchs = []                  # Liste des matchs générés
    
    # Fonction pour générer les matchs automatiquement (élimination simple)
    def generer_bracket_simple(self):
        equipes = self.tournoi.liste_equipes
        
        # Vérifier qu'on a au moins 2 équipes
        if len(equipes) < 2:
            print("Erreur: Il faut au moins 2 équipes pour créer un bracket")
            return
        
        # Créer les matchs : équipe 0 vs équipe 1, équipe 2 vs équipe 3, etc.
        id_match = 1
        for i in range(0, len(equipes), 2):
            if i + 1 < len(equipes):
                # Importer Match (on le fait ici pour éviter les problèmes)
                from match import Match
                
                # Créer un match entre deux équipes
                match = Match(id_match, equipes[i], equipes[i+1])
                self.liste_matchs.append(match)
                self.tournoi.ajouter_match(match)
                
                id_match = id_match + 1
        
        print(f"Bracket généré avec {len(self.liste_matchs)} matchs")
    
    # Fonction pour afficher le bracket
    def afficher_bracket(self):
        print(f"Bracket {self.id_bracket} - Type: {self.type_elimination}")
        print("=" * 50)
        for match in self.liste_matchs:
            match.afficher_info()
            print("-" * 50)
    
    # Fonction pour obtenir le nombre de matchs
    def get_nombre_matchs(self):
        return len(self.liste_matchs)
