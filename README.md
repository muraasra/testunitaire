# Django Library Management – B3 Test Unitaire

**Version 1.0 – 2025-05-27**

---
## Table des matières
1. [Présentation](#présentation)
2. [Fonctionnalités](#fonctionnalités)
3. [Pile technologique](#pile-technologique)
4. [Arborescence du dépôt](#arborescence-du-dépôt)
5. [Installation & mise en route](#installation--mise-en-route)
6. [Utilisation](#utilisation)
7. [Suite de tests & couverture](#suite-de-tests--couverture)
8. [API REST](#api-rest)
9. [Déploiement en production](#déploiement-en-production)
10. [Contribuer](#contribuer)
11. [Licence](#licence)

---

## Présentation
Ce projet est la solution complète au contrôle continu **B3 « Test Unitaire »**.  
Il s’agit d’une application **Django 4.2** permettant de gérer un catalogue de bibliothèque : livres, auteurs, catégories, emprunts et retours.  
L’accent est mis sur :
- **Tests unitaires exhaustifs** (≥ 80 % de couverture),
- **Organisation modulaire** (modèles / services / vues / API),
- **Front‑end Bootstrap** rendu côté serveur via les templates Django.

## Fonctionnalités
- CRUD complet pour : **Livres**, **Auteurs**, **Catégories**  
- **Prêt** / **Retour** avec mise à jour automatique du stock
- Recherche plein‑texte (titre / auteur / catégorie)
- **API REST** (DRF) avec permissions lecture publique, écriture authentifiée
- Interface Bootstrap 5 et pagination (20 livres par page)
- Tableau de bord d’administration Django
- Couverture **pytest‑cov** ≥ 93 % (objectif fixé ≥ 80 %)

## Pile technologique
| Outil | Version | Rôle |
|-------|---------|------|
| Python | 3.12 | Langage |
| Django | 4.2.x | Framework web |
| Django REST framework | 3.15 | API REST |
| pytest / pytest‑django | 8.x | Exécution des tests |
| pytest‑cov | 4.x | Rapport de couverture |
| django‑filter | 24.x | Filtres & recherche |
| Bootstrap | 5.3 | UI responsive |

## Arborescence du dépôt
```text
library_project/
├── manage.py
├── requirements.txt
├── pytest.ini
├── README.md          # ← ce fichier
├── library_project/   # réglages & URL racine
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── catalog/           # application principale
│   ├── models.py
│   ├── services.py
│   ├── forms.py
│   ├── views.py
│   ├── api.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests/
├── templates/
└── static/
```

## Installation & mise en route
```bash
# 1. Cloner le repo
git clone https://github.com/muraasra/testunitaire.git && cd testunitaire

# 2. Créer l’environnement virtuel
python -m venv venv
source venv/bin/activate        # Windows : .\venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Initialiser la base SQLite
python manage.py migrate
python manage.py createsuperuser

# 5. Lancer le serveur
python manage.py runserver
# → http://localhost:8000/
```

## Utilisation
- **Catalogue** : page d’accueil liste tous les livres (pagination 20).
- **Recherche** : barre de recherche en haut de la liste.
- **Ajouter / éditer** : nécessitent d’être connecté en tant qu’utilisateur.
- **Prêt / retour** : actions internes appelant `catalog.services`.

![screenshot](docs/screenshot.png)

## Suite de tests & couverture
```bash
# Exécuter toute la suite
pytest --cov=catalog

# Résultats attendus
============================= 15 passed in 2.3s =============================
---------- coverage: platform linux, Python 3.12 ----------
Name                  Stmts   Miss  Cover
-----------------------------------------
catalog/models.py        45      2    92%
catalog/services.py      25      0   94%
...
TOTAL                   158      8    93%
```
Un rapport HTML détaillé est généré :
```bash
coverage html
open htmlcov/index.html
```

## API REST
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/books/` | Liste paginée des livres |
| POST | `/api/books/` | Créer un livre *(auth)* |
| GET | `/api/books/{id}/` | Détail d’un livre |
| PUT/PATCH | `/api/books/{id}/` | Modifier un livre *(auth)* |
| DELETE | `/api/books/{id}/` | Supprimer un livre *(auth)* |


## Contribuer
1. Fork, `git checkout -b feature/ma-feature`.
2. Ajouter des tests pour toute nouvelle fonctionnalité.
3. Vérifier que `pytest` et `flake8` passent.
4. Ouvrir une Pull‑Request bien documentée.

## Licence
MIT – libre d’utilisation, modification et distribution.

---
> _Dernière mise à jour : 2025-05-27_
