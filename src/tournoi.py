 # Classe pour représenter un TOURNOI

class Tournoi:
    
    # Fonction pour créer un tournoi
    def __init__(self, id_tournoi, nom, date, jeu, nombre_max_participants):
        self.id_tournoi = id_tournoi                    # Un numéro unique pour le tournoi
        self.nom = nom                                  # Le nom du tournoi
        self.date = date                                # La date du tournoi
        self.jeu = jeu                                  # Le jeu joué (ex: League of Legends)
        self.nombre_max_participants = nombre_max_participants  # Nombre maximum de joueurs
        self.liste_equipes = []                         # Liste vide pour les équipes
        self.liste_matchs = []                          # Liste vide pour les matchs
        self.statut = "Création"                        # Au départ, le tournoi est en création
    
    # Fonction pour ajouter une équipe au tournoi
    def ajouter_equipe(self, equipe):
        if len(self.liste_equipes) < self.nombre_max_participants:
            self.liste_equipes.append(equipe)
            print(f"Équipe {equipe.nom_equipe} ajoutée au tournoi")
        else:
            print("Erreur: Le nombre maximum de participants est atteint")
    
    # Fonction pour ajouter un match au tournoi
    def ajouter_match(self, match):
        self.liste_matchs.append(match)
        print(f"Match {match.id_match} ajouté au tournoi")
    
    # Fonction pour afficher tous les équipes du tournoi
    def afficher_equipes(self):
        print(f"Équipes du tournoi {self.nom}:")
        for equipe in self.liste_equipes:
            print(f"  - {equipe.nom_equipe}")
    
    # Fonction pour afficher tous les matchs du tournoi
    def afficher_matchs(self):
        print(f"Matchs du tournoi {self.nom}:")
        for match in self.liste_matchs:
            match.afficher_info()
    
    # Fonction pour changer le statut du tournoi
    def changer_statut(self, nouveau_statut):
        self.statut = nouveau_statut
        print(f"Le tournoi est maintenant: {self.statut}")
    
    # Fonction pour afficher les infos du tournoi
    def afficher_info(self):
        print(f"Tournoi: {self.nom}")
        print(f"Date: {self.date}")
        print(f"Jeu: {self.jeu}")
        print(f"Nombre d'équipes: {len(self.liste_equipes)}")
        print(f"Nombre de matchs: {len(self.liste_matchs)}")
        print(f"Statut: {self.statut}")
