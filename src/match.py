# Classe pour représenter un MATCH

class Match:
    
    # Fonction pour créer un match
    def __init__(self, id_match, participant1, participant2):
        self.id_match = id_match            # Un numéro unique pour le match
        self.participant1 = participant1    # Le joueur ou équipe 1
        self.participant2 = participant2    # Le joueur ou équipe 2
        self.gagnant = None                 # Au départ, pas encore de gagnant
        self.statut = "En attente"          # Le match n'a pas commencé
    
    # Fonction pour obtenir le nom du participant
    def get_nom(self, participant):
        if hasattr(participant, 'pseudo'):      # Si c'est un joueur
            return participant.pseudo
        else:                                   # Si c'est une équipe
            return participant.nom_equipe
    
    # Fonction pour enregistrer le résultat du match
    def enregistrer_resultat(self, gagnant):
        if gagnant == self.participant1:
            self.gagnant = self.participant1
            self.participant1.ajouter_victoire()  # Ajoute une victoire au gagnant
            self.participant2.ajouter_defaite()   # Ajoute une défaite au perdant
        elif gagnant == self.participant2:
            self.gagnant = self.participant2
            self.participant2.ajouter_victoire()
            self.participant1.ajouter_defaite()
        else:
            print("Erreur: Le gagnant doit être participant1 ou participant2")
            return
        
        self.statut = "Terminé"
        nom_gagnant = self.get_nom(self.gagnant)
        print(f"Match {self.id_match}: {nom_gagnant} a gagné!")
    
    # Fonction pour afficher les infos du match
    def afficher_info(self):
        nom1 = self.get_nom(self.participant1)
        nom2 = self.get_nom(self.participant2)
        
        print(f"Match {self.id_match}:")
        print(f"  {nom1} vs {nom2}")
        print(f"  Statut: {self.statut}")
        if self.gagnant:
            nom_gagnant = self.get_nom(self.gagnant)
            print(f"  Gagnant: {nom_gagnant}")
        else:
            print(f"  Gagnant: Pas encore déterminé")