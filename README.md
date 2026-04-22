# Gestionnaire de Tournois E-Sport

## Description
Application Python interactive pour organiser et gérer des tournois e-sports. Permet de créer des tournois, enregistrer des équipes et joueurs, générer automatiquement des brackets, et suivre les résultats des matchs avec statistiques.

## Objectifs du Projet
- Créer et gérer des tournois e-sports
- Enregistrer des équipes et des joueurs
- Générer automatiquement des tableaux de matchs (brackets)
- Enregistrer les résultats et afficher les statistiques
- Appliquer les principes de Programmation Orientée Objet (POO)

##  Installation

### Prérequis
- Python 3.8 ou supérieur
- Git

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/Christson-16/Gestionnaire-Tournois-ESort.git
cd Gestionnaire-Tournois-ESort
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel**
- **Windows :**
```bash
venv\Scripts\activate
```
- **Mac/Linux :**
```bash
source venv/bin/activate
```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Lancer l'application**
```bash
python src/main.py
```

## Utilisation

Une fois l'application lancée, un menu interactif s'affiche :
### Exemple d'utilisation

1. **Créer un tournoi** → Entrer le nom, date, jeu, nombre max d'équipes
2. **Ajouter des équipes** → Créer Team Alpha, Team Beta, etc.
3. **Ajouter des joueurs** → Associer les joueurs à chaque équipe
4. **Générer le bracket** → Créer automatiquement les matchs
5. **Enregistrer les résultats** → Entrer les gagnants des matchs
6. **Voir les stats** → Afficher le classement et les statistiques

##  Architecture (POO)

### Classes principales

**Joueur**
- Attributs : id, pseudo, email, niveau, matchs_gagnes, matchs_perdus
- Méthodes : ajouter_victoire(), ajouter_defaite()

**Équipe**
- Attributs : id, nom, liste_joueurs, matchs_gagnes, matchs_perdus
- Méthodes : ajouter_joueur(), afficher_joueurs()

**Match**
- Attributs : id, participant1, participant2, gagnant, statut
- Méthodes : enregistrer_resultat(), afficher_info()

**Tournoi**
- Attributs : id, nom, date, jeu, liste_equipes, liste_matchs, statut
- Méthodes : ajouter_equipe(), ajouter_match(), afficher_info()

**Bracket**
- Attributs : id, tournoi, type_elimination, liste_matchs
- Méthodes : generer_bracket_simple(), afficher_bracket()

##  Fonctionnalités en cours de développement

- [ ] **Bloc 3** : Architecture POO avancée (héritage, encapsulation)
- [ ] **Bloc 4** : Persistance des données (SQLite/JSON)
- [ ] **Bloc 5** : Gestion des exceptions et tests unitaires
- [ ] **Bloc 6** : Interface graphique (Tkinter/PyQt) ou Web (Flask)

##  Tests

```bash
python -m pytest tests/
```

(À développer)

##  Cahier des Charges

Voir le fichier `Cahier_des_Charges_Tournois_ESort.docx` pour plus de détails.

##  Auteurs

- **Christson Koessi** (@Christson-16)
- **Jupiter Chabi**

##  Deadlines

- Bloc 1 (Cahier des charges) : ✅ 20/04/2026
- Bloc 2 (Workflow & Fondations) : ✅ 22/04/2026
- Bloc 3 (Architecture POO) : 22/04/2026
- Bloc 4 (Persistance) : 24/04/2026
- Bloc 5 (Qualité) : 24/04/2026
- Bloc 6 (Interface & Livraison) : 25/04/2026

## Contact

Pour toute question : christson@email.com

---

**Fait avec  à l'IUT de Parakou**