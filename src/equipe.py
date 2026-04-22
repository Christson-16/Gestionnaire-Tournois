# Classe pour représenter une ÉQUIPE

class Equipe:
    
    # Fonction pour créer une équipe
    def __init__(self, id_equipe, nom_equipe):
        self.id_equipe = id_equipe          # Un numéro unique pour l'équipe
        self.nom_equipe = nom_equipe        # Le nom de l'équipe
        self.liste_joueurs = []             # Liste vide au départ, on y ajoute des joueurs
        self.matchs_gagnes = 0              # Compte combien de matchs l'équipe a gagné
        self.matchs_perdus = 0              # Compte combien de matchs l'équipe a perdu
    
    # Fonction pour ajouter un joueur à l'équipe
    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)   # Ajoute le joueur à la liste
        print(f"{joueur.pseudo} a été ajouté à {self.nom_equipe}")
    
    # Fonction pour afficher tous les joueurs de l'équipe
    def afficher_joueurs(self):
        print(f"Joueurs de {self.nom_equipe}:")
        for joueur in self.liste_joueurs:   # Parcourt chaque joueur
            print(f"  - {joueur.pseudo}")
    
    # Fonction pour ajouter une victoire à l'équipe
    def ajouter_victoire(self):
        self.matchs_gagnes = self.matchs_gagnes + 1
    
    # Fonction pour ajouter une défaite à l'équipe
    def ajouter_defaite(self):
        self.matchs_perdus = self.matchs_perdus + 1
    
    # Fonction pour afficher les infos de l'équipe
    def afficher_info(self):
        print(f"Équipe: {self.nom_equipe}")
        print(f"Nombre de joueurs: {len(self.liste_joueurs)}")
        print(f"Matchs gagnés: {self.matchs_gagnes}")
        print(f"Matchs perdus: {self.matchs_perdus}")