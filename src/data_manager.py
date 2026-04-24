"""
MODULE DATA_MANAGER
Gère la persistance des données avec SQLite
"""

import sqlite3
import os
from joueur import Joueur
from equipe import Equipe
from tournoi import Tournoi
from match import Match
from bracket import Bracket

class DataManager:
    """
    Classe pour gérer la persistance des données en SQLite
    
    LOGIQUE:
        1. Créer une base de données "tournois.db"
        2. Créer les tables (tournois, equipes, joueurs, matchs)
        3. Sauvegarder les objets dans la base
        4. Charger les objets depuis la base au démarrage
    
    Attributs:
        - _db_path : Chemin du fichier .db
        - _connexion : Connexion SQLite
    """
    
    def __init__(self, db_name="tournois.db"):
        """
        Initialise le gestionnaire de données
        
        Args:
            db_name (str): Nom du fichier de base de données
        """
        self._db_path = db_name
        self._connexion = None
        self._initialiser_base()
    
    def _initialiser_base(self):
        """
        Initialise la connexion et crée les tables
        
        LOGIQUE:
            1. Connecter à SQLite
            2. Créer les tables si elles n'existent pas
            3. Garder la connexion ouverte
        """
        try:
            self._connexion = sqlite3.connect(self._db_path)
            self._connexion.row_factory = sqlite3.Row
            self._creer_tables()
            print(f"✅ Base de données '{self._db_path}' initialisée")
        except sqlite3.Error as e:
            print(f"⚠ Erreur SQLite: {e}")
    
    def _creer_tables(self):
        """Crée les tables si elles n'existent pas"""
        cursor = self._connexion.cursor()
        
        # Table TOURNOIS
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tournois (
                id INTEGER PRIMARY KEY,
                nom TEXT NOT NULL,
                date TEXT NOT NULL,
                jeu TEXT NOT NULL,
                max_equipes INTEGER NOT NULL,
                statut TEXT NOT NULL,
                vainqueur_id INTEGER
            )
        """)
        
        # Table ÉQUIPES
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipes (
                id INTEGER PRIMARY KEY,
                tournoi_id INTEGER NOT NULL,
                nom TEXT NOT NULL,
                niveau INTEGER NOT NULL,
                matchs_gagnes INTEGER DEFAULT 0,
                matchs_perdus INTEGER DEFAULT 0,
                statut TEXT NOT NULL,
                FOREIGN KEY(tournoi_id) REFERENCES tournois(id)
            )
        """)
        
        # Table JOUEURS
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS joueurs (
                id INTEGER PRIMARY KEY,
                equipe_id INTEGER NOT NULL,
                pseudo TEXT NOT NULL,
                email TEXT NOT NULL,
                niveau TEXT NOT NULL,
                matchs_gagnes INTEGER DEFAULT 0,
                matchs_perdus INTEGER DEFAULT 0,
                FOREIGN KEY(equipe_id) REFERENCES equipes(id)
            )
        """)
        
        # Table MATCHS
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS matchs (
                id INTEGER PRIMARY KEY,
                tournoi_id INTEGER NOT NULL,
                participant1_id INTEGER NOT NULL,
                participant2_id INTEGER NOT NULL,
                gagnant_id INTEGER,
                tour TEXT NOT NULL,
                statut TEXT NOT NULL,
                FOREIGN KEY(tournoi_id) REFERENCES tournois(id),
                FOREIGN KEY(participant1_id) REFERENCES equipes(id),
                FOREIGN KEY(participant2_id) REFERENCES equipes(id),
                FOREIGN KEY(gagnant_id) REFERENCES equipes(id)
            )
        """)
        
        self._connexion.commit()
    
    def sauvegarder_tournoi(self, tournoi):
        """
        Sauvegarde un tournoi dans la base
        
        LOGIQUE:
            1. Si le tournoi existe (id != None) → UPDATE
            2. Sinon → INSERT
            3. Retourner l'ID
        
        Args:
            tournoi (Tournoi): Le tournoi à sauvegarder
            
        Returns:
            int: L'ID du tournoi dans la base
        """
        cursor = self._connexion.cursor()
        
        vainqueur_id = None
        if tournoi.get_vainqueur():
            vainqueur_id = tournoi.get_vainqueur().get_id()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO tournois 
                (id, nom, date, jeu, max_equipes, statut, vainqueur_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                tournoi.get_id(),
                tournoi.get_nom(),
                tournoi.get_date(),
                tournoi.get_jeu(),
                tournoi.get_max_equipes(),
                tournoi.get_statut(),
                vainqueur_id
            ))
            self._connexion.commit()
            return tournoi.get_id()
        except sqlite3.Error as e:
            print(f"⚠ Erreur en sauvegardant le tournoi: {e}")
            return None
    
    def sauvegarder_equipe(self, equipe, tournoi_id):
        """Sauvegarde une équipe"""
        cursor = self._connexion.cursor()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO equipes 
                (id, tournoi_id, nom, niveau, matchs_gagnes, matchs_perdus, statut)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                equipe.get_id(),
                tournoi_id,
                equipe.get_nom(),
                equipe.get_niveau(),
                equipe.get_matchs_gagnes(),
                equipe.get_matchs_perdus(),
                equipe.get_statut()
            ))
            self._connexion.commit()
            return equipe.get_id()
        except sqlite3.Error as e:
            print(f"⚠ Erreur en sauvegardant l'équipe: {e}")
            return None
    
    def sauvegarder_joueur(self, joueur, equipe_id):
        """Sauvegarde un joueur"""
        cursor = self._connexion.cursor()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO joueurs 
                (id, equipe_id, pseudo, email, niveau, matchs_gagnes, matchs_perdus)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                joueur.get_id(),
                equipe_id,
                joueur.get_pseudo(),
                joueur.get_email(),
                joueur.get_niveau(),
                joueur.get_matchs_gagnes(),
                joueur.get_matchs_perdus()
            ))
            self._connexion.commit()
            return joueur.get_id()
        except sqlite3.Error as e:
            print(f"⚠ Erreur en sauvegardant le joueur: {e}")
            return None
    
    def sauvegarder_match(self, match, tournoi_id):
        """Sauvegarde un match"""
        cursor = self._connexion.cursor()
        
        gagnant_id = None
        if match.get_gagnant():
            gagnant_id = match.get_gagnant().get_id()
        
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO matchs 
                (id, tournoi_id, participant1_id, participant2_id, gagnant_id, tour, statut)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                match.get_id(),
                tournoi_id,
                match.get_participant1().get_id(),
                match.get_participant2().get_id(),
                gagnant_id,
                match.get_tour(),
                match.get_statut()
            ))
            self._connexion.commit()
            return match.get_id()
        except sqlite3.Error as e:
            print(f"⚠ Erreur en sauvegardant le match: {e}")
            return None
    
    def sauvegarder_tout(self, liste_tournois):
        """
        Sauvegarde TOUS les tournois et leurs données
        
        LOGIQUE:
            1. Pour chaque tournoi:
               - Sauvegarder le tournoi
               - Pour chaque équipe:
                 - Sauvegarder l'équipe
                 - Pour chaque joueur:
                   - Sauvegarder le joueur
               - Pour chaque match:
                 - Sauvegarder le match
        
        Args:
            liste_tournois (list): Liste de tous les tournois
        """
        for tournoi in liste_tournois:
            # Sauvegarder le tournoi
            self.sauvegarder_tournoi(tournoi)
            
            # Sauvegarder les équipes et joueurs
            for equipe in tournoi.get_equipes():
                self.sauvegarder_equipe(equipe, tournoi.get_id())
                
                for joueur in equipe.get_joueurs():
                    self.sauvegarder_joueur(joueur, equipe.get_id())
            
            # Sauvegarder les matchs
            for match in tournoi.get_matchs():
                self.sauvegarder_match(match, tournoi.get_id())
        
        print("✅ Toutes les données ont été sauvegardées!")
    
    def charger_tournois(self):
        """
        Charge tous les tournois depuis la base
        
        LOGIQUE:
            1. Récupérer tous les tournois
            2. Pour chaque tournoi:
               - Charger les équipes
               - Pour chaque équipe:
                 - Charger les joueurs
               - Charger les matchs
            3. Reconstruire les objets Python
        
        Returns:
            list: Liste des tournois chargés
        """
        cursor = self._connexion.cursor()
        liste_tournois = []
        
        try:
            cursor.execute("SELECT * FROM tournois")
            tournois_data = cursor.fetchall()
            
            for t_data in tournois_data:
                # Recréer l'objet Tournoi
                tournoi = Tournoi(
                    t_data['id'],
                    t_data['nom'],
                    t_data['date'],
                    t_data['jeu'],
                    t_data['max_equipes']
                )
                tournoi.changer_statut(t_data['statut'])
                
                # Charger les équipes
                cursor.execute(
                    "SELECT * FROM equipes WHERE tournoi_id = ?",
                    (t_data['id'],)
                )
                equipes_data = cursor.fetchall()
                
                for e_data in equipes_data:
                    equipe = Equipe(
                        e_data['id'],
                        e_data['nom'],
                        e_data['niveau']
                    )
                    equipe.changer_statut(e_data['statut'])
                    
                    # Charger les joueurs de l'équipe
                    cursor.execute(
                        "SELECT * FROM joueurs WHERE equipe_id = ?",
                        (e_data['id'],)
                    )
                    joueurs_data = cursor.fetchall()
                    
                    for j_data in joueurs_data:
                        joueur = Joueur(
                            j_data['id'],
                            j_data['pseudo'],
                            j_data['email'],
                            j_data['niveau']
                        )
                        equipe.ajouter_joueur(joueur)
                    
                    tournoi._liste_equipes.append(equipe)
                
                liste_tournois.append(tournoi)
            
            if len(liste_tournois) > 0:
                print(f"✅ {len(liste_tournois)} tournoi(s) chargé(s) depuis la base")
            
            return liste_tournois
        
        except sqlite3.Error as e:
            print(f"⚠ Erreur en chargeant les tournois: {e}")
            return []
    
    def supprimer_tournoi(self, tournoi_id):
        """Supprime un tournoi et toutes ses données"""
        cursor = self._connexion.cursor()
        
        try:
            cursor.execute("DELETE FROM matchs WHERE tournoi_id = ?", (tournoi_id,))
            cursor.execute(
                "DELETE FROM joueurs WHERE equipe_id IN (SELECT id FROM equipes WHERE tournoi_id = ?)",
                (tournoi_id,)
            )
            cursor.execute("DELETE FROM equipes WHERE tournoi_id = ?", (tournoi_id,))
            cursor.execute("DELETE FROM tournois WHERE id = ?", (tournoi_id,))
            
            self._connexion.commit()
            print(f"✅ Tournoi {tournoi_id} supprimé de la base")
            return True
        except sqlite3.Error as e:
            print(f"⚠ Erreur en supprimant le tournoi: {e}")
            return False
    
    def compter_tournois(self):
        """Retourne le nombre de tournois dans la base"""
        cursor = self._connexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM tournois")
        return cursor.fetchone()[0]
    
    def fermer_connexion(self):
        """Ferme la connexion SQLite"""
        if self._connexion:
            self._connexion.close()
            print("✅ Connexion à la base fermée")
    
    def __del__(self):
        """Ferme la connexion au moment de la suppression de l'objet"""
        self.fermer_connexion()