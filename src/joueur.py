# Classe pour représenter un JOUEUR

class Joueur:
    
    # Fonction pour créer un joueur
    def __init__(self, id_joueur, pseudo, email, niveau):
        self.id_joueur = id_joueur      # Un numéro unique pour le joueur
        self.pseudo = pseudo            # Le surnom du joueur
        self.email = email              # L'email du joueur
        self.niveau = niveau            # Le niveau : débutant, intermédiaire ou expert
        self.matchs_gagnes = 0          # Compte combien de matchs il a gagné (0 au départ)
        self.matchs_perdus = 0          # Compte combien de matchs il a perdu (0 au départ)
    
    # Fonction pour afficher les infos du joueur
    def afficher_info(self):
        print(f"Joueur: {self.pseudo}")
        print(f"Email: {self.email}")
        print(f"Niveau: {self.niveau}")
        print(f"Matchs gagnés: {self.matchs_gagnes}")
        print(f"Matchs perdus: {self.matchs_perdus}")
    
    # Fonction pour ajouter une victoire
    def ajouter_victoire(self):
        self.matchs_gagnes = self.matchs_gagnes + 1
    
    # Fonction pour ajouter une défaite
    def ajouter_defaite(self):
        self.matchs_perdus = self.matchs_perdus + 1