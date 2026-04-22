## Gestionnaire de Tournois E-Sport
#  Description

Application Python interactive pour organiser et gérer des **tournois e-sports complets**. 
Permet de :
-  Créer plusieurs tournois indépendants
-  Gérer les équipes et les joueurs
-  Générer automatiquement les matchs (brackets)
-  Simuler les matchs selon le niveau des équipes
-  Gérer l'élimination directe avec règle du **BYE** (qualification automatique)
-  Suivre les statistiques en temps réel

##  Objectifs du Projet

- Créer et gérer **plusieurs tournois** simultanément
- Enregistrer des **équipes et joueurs** avec leurs niveaux
- Générer automatiquement des **tableaux de matchs** (brackets)
- **Simuler les matchs** basés sur les niveaux des équipes
- Appliquer la **Programmation Orientée Objet (POO)** avancée
- Respecter les **règles d'élimination directe** avec BYE pour les nombres impairs

## Structure du Projet
Gestionnaire-Tournois-ESort/
├── src/
│   ├── bracket.py           
│   ├── data_manager.py         
│   ├── equipe.py          
│   ├── joueur.py       
│   ├── main.py       
│   ├── match.py
├── requirements.txt          
│   └──   tournoi.py  
├── tests/
│   └── test_joueur.py
├── .gitignore                 
└── README.md              

## Installation

### Prérequis
- Python 3.8 ou supérieur
- Git

### Étapes

1. **Cloner le repository**
```bash
git clone https://github.com/Christson-16/Gestionnaire-Tournois-ESort.git
cd Gestionnaire-Tournois-ESort
```

2. **Créer l'environnement virtuel**
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel**

**Windows :**
```bash
venv\Scripts\activate
```

**Mac/Linux :**
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

### Menu Principal

Une fois lancée, l'application affiche :
## GESTIONNAIRE DE TOURNOIS E-SPORT
## Tournoi actif: [Nom du tournoi]
## MENU PRINCIPAL:
Gérer les tournois (créer, sélectionner, supprimer)
Gérer équipes et joueurs
Générer le bracket
Simuler les matchs
Afficher statistiques
Quitter


### Workflow Complet

#### **Étape 1 : Créer un Tournoi**
- Menu 1 → Option 1
- Entrer : nom, date, jeu, nombre max d'équipes

#### **Étape 2 : Ajouter des Équipes**
- Menu 2 → Option 1
- Choisir le tournoi actif
- Créer des équipes avec leur **niveau de force (0-100)**

#### **Étape 3 : Ajouter des Joueurs aux Équipes**
- Menu 2 → Option 3
- Sélectionner une équipe
- Ajouter des joueurs avec pseudo, email et niveau

#### **Étape 4 : Générer le Bracket**
- Menu 3
- Le tournoi doit être **COMPLET** (nombre d'équipes = max)
- Les matchs se génèrent automatiquement

#### **Étape 5 : Simuler les Matchs**
- Menu 4 → Option 2
- Tous les matchs du tour se simulent
- Les gagnants avancent au tour suivant

#### **Étape 6 : Progression du Tournoi**
- Menu 4 → Option 3
- Passer au tour suivant
- Le système gère automatiquement le **BYE** pour les nombres impairs

##  Logique du Système

### Création d'un Tournoi

Un tournoi contient :
- **Nom**, **Date**, **Jeu**, **Nombre max de participants**

**Règles :**
-  Un tournoi peut être modifié **SEULEMENT s'il n'a aucune équipe**
-  Dès qu'une équipe est ajoutée → modification interdite
-  Le tournoi ne peut être lancé que s'il est **COMPLET**

### Simulation des Matchs

**Logique de calcul des probabilités :**

Chaque équipe possède un **niveau (0-100)**.
## Exemple:

- Équipe A: niveau 30
- Équipe B: niveau 70
- Total: 100

## Probabilités:

- A gagne: 30/100 = 30%
- B gagne: 70/100 = 70%

## Résultat:

## Générer nombre aléatoire entre 0 et 100
- Si nombre ≤ 30 → A gagne
- Sinon → B gagne
### Gestion du BYE (Élimination Directe)

## Quand le nombre d'équipes est **IMPAIR** : Exemple: 9 équipes
# TOUR 1:

- Une équipe choisie AU HASARD → BYE (pas de match)
8 autres équipes → 4 matchs
Résultat: 5 équipes qualifiées (4 gagnants + 1 BYE)

TOUR 2:

Nouvelle équipe choisie AU HASARD pour le BYE
Les autres jouent leurs matchs
Résultat: 3 équipes qualifiées

TOUR 3:

Encore une équipe pour le BYE
1 match final → détermine le gagnant
**Points importants :**
-  Le BYE est **aléatoire** à chaque tour
-  Le BYE est **recalculé** à chaque tour
-  Une équipe peut avoir 0, 1 ou plusieurs BYE
-  Le tournoi reste **équitable**

## Architecture POO

### Classes et Relations
Joueur
├── Attributs: id, pseudo, email, niveau
├── Méthodes: ajouter_victoire(), ajouter_defaite()
└── Getters/Setters pour encapsulation
Équipe
├── Attributs: id, nom, niveau, liste_joueurs
├── Méthodes: ajouter_joueur(), supprimer_joueur()
└── Gère les résultats des matchs
Match
├── Attributs: id, participant1, participant2, gagnant
├── Méthodes: simuler_match() [LOGIQUE DE SIMULATION]
└── Enregistre les résultats
Tournoi
├── Attributs: id, nom, date, jeu, liste_equipes
├── Méthodes: ajouter_equipe(), lancer_tournoi()
└── Gère les restrictions et l'état
Bracket
├── Attributs: id, tournoi, matchs_par_tour
├── Méthodes: generer_bracket_simple(), progresser_tournoi()
└── Gère l'élimination directe et le BYE
### Encapsulation

- **Attributs privés** : `_nom`, `_email`, etc.
- **Getters** : `get_nom()`, `get_email()`
- **Setters** : `modifier_nom()`, `modifier_email()`
- **Validation** : Chaque setter vérifie les données

## Exemple d'Utilisation Complète

### Scénario : Tournoi FIFA avec 8 Équipes
Créer tournoi "FIFA 2026"

Nom: FIFA 2026
Date: 25/04/2026
Jeu: FIFA
Max équipes: 8


# Ajouter 8 équipes

Team Alpha (niveau 75)
Team Beta (niveau 60)
Team Gamma (niveau 80)
... (5 autres équipes)


# Ajouter joueurs à chaque équipe

# Chaque équipe a 3-5 joueurs


# Générer bracket

8 équipes = 4 matchs au tour 1


# Simuler tour 1

4 matchs se jouent
4 équipes qualifiées


# Passer au tour 2

4 équipes = 2 matchs (semi-finales)
2 gagnants


# Passer au tour 3

2 équipes = 1 match (finale)
1 vainqueur final

## Auteurs

- **Christson Koessi** 
- **Jupiter Chabi**

Université de Parakou - Institut Universitaire de Technologie (IUT)

## Contact

Pour toute question :
- Email: koessichristson@gmail.com
- GitHub: https://github.com/Christson-16/Gestionnaire-Tournois-ESort

---

**Fait pour les e-sports**