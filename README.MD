# 🍽️ API Gateway - Projet Microservices Restaurant

Ce projet constitue l'**API Gateway** d'une application de gestion de commandes pour un restaurant. Il s'inscrit dans une architecture **microservices** répartie entre plusieurs domaines métier : client, commande, cuisine et livraison.

---

## 📌 Objectifs

- Servir de **point d'entrée unique** pour le Frontend.
- Centraliser les appels vers les microservices.
- Intégrer les **services réels** (clients, commandes).
- Simuler les échanges pour les services non disponibles.
- Gérer les erreurs et assurer un **mode dégradé**.

---

## 🛠️ Technologies utilisées

| Composant     | Techno      |
|---------------|-------------|
| API Gateway   | FastAPI     |
| HTTP Client   | HTTPX       |
| Langage       | Python 3.10+|

---

## 📁 Architecture


api_gateway/
├── main.py                          # Point d’entrée de l’API Gateway
├── requirements.txt                 # Dépendances Python
├── services/                        # Regroupe les routes par domaine fonctionnel
│   ├── auth.py                      # Authentification fictive (démo/testing)
│   ├── client_api.py                # Redirection vers le microservice Gestion-client-ms
│   ├── order_api.py                 # Redirection vers le microservice de gestion des commandes
│   ├── orders.py                    # Commandes simulées (ancien mock, facultatif)
│   ├── kitchen.py                   # Module cuisine simulé (statut des plats)
│   └── delivery.py                  # Module livraison simulé
├── utils/
    └── http_client.py               # Outil générique pour les appels HTTP simulés (test/local)


---

## 🚀 Lancer le projet

### 1. Cloner le dépôt
```bash
git clone <url_du_repo>
cd api_gateway
```
### 2. Créer et activer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # sur Windows : venv\Scripts\activate
```
### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```
### 4. Lancer l'API Gateway
```bash
uvicorn main:app --reload --port 8000
```

## 🔗 Endpoints disponibles

### 🔐 Authentification (réelle, déléguée à `Gestion-client-ms`)
> L'authentification est **entièrement fonctionnelle** : la Gateway redirige toutes les requêtes vers le microservice `Gestion-client-ms`, qui gère les **JWT**, les **rôles** et les **sessions**.
>  
> 📌 La Gateway ne valide pas les tokens elle-même, mais relaie les headers `Authorization: Bearer <token>` au microservice qui, lui, fait les contrôles.

| Méthode | Endpoint                          | Description                                 | Auth requise |
|--------:|-----------------------------------|---------------------------------------------|--------------|
| `POST`  | `/client-api/login`               | Connexion d'un client (retourne JWT)        | ❌           |
| `POST`  | `/client-api/clients`             | Créer un nouveau client                     | ❌           |
| `GET`   | `/client-api/clients`             | Lister les clients                          | ❌           |
| `GET`   | `/client-api/clients/{id}`        | Récupérer un client par ID                  | ❌           |
| `DELETE`| `/client-api/clients/{id}`        | Supprimer un client                         | ❌           |
| `POST`  | `/client-api/logout`              | Déconnexion (invalide le JWT)               | ✅           |
| `POST`  | `/client-api/logout-all`          | Déconnexion toutes sessions                 | ✅           |
| `GET`   | `/client-api/sessions`            | Lister les sessions actives                 | ✅           |

---

### 📖 Menu et commandes (Service Commandes - réel)

| Méthode | Endpoint                                         | Description                            |
|--------:|--------------------------------------------------|----------------------------------------|
| `GET`   | `/order-api/menu`                                | Lister tous les plats                  |
| `GET`   | `/order-api/menu/filter?categorie=...`           | Filtrer les plats par catégorie        |
| `POST`  | `/order-api/commandes`                           | Créer une commande                     |
| `GET`   | `/order-api/commandes`                           | Lister toutes les commandes            |
| `GET`   | `/order-api/commandes/{id}`                      | Détail d'une commande                  |
| `PATCH` | `/order-api/commandes/{id}/status`               | Mettre à jour le statut d'une commande|

---

### 🍳 Cuisine (simulée localement)
| Méthode | Endpoint               | Description                            |
|--------:|------------------------|----------------------------------------|
| `GET`   | `/kitchen/orders`      | Commandes en cours côté cuisine        |
| `POST`  | `/kitchen/update`      | Marquer une commande comme "prête"     |

---

### 🚚 Livraison (simulée localement)
| Méthode | Endpoint               | Description                            |
|--------:|------------------------|----------------------------------------|
| `GET`   | `/delivery/assigned`   | Liste des commandes à livrer           |
| `POST`  | `/delivery/update`     | Marquer une commande comme livrée      |


## 🧪 Simulation de panne & mode dégradé

Le module `http_client.py` est toujours présent dans le projet.  
Il permet de **simuler les appels aux microservices** en mode fallback local, mais n'est **plus utilisé activement**.
En cas de panne ou d’indisponibilité (par exemple, suppression temporaire d’une route), l’API Gateway :

- Renvoie un message d’erreur clair au frontend
- Garde les autres fonctionnalités opérationnelles

---

## ✅ Objectifs pédagogiques couverts

- ✅ Présentation claire du contexte et des services
- ✅ Démonstration fonctionnelle complète (auth, commande, cuisine, livraison)
- ✅ Architecture Microservices respectée (Gateway + découpage logique)
- ✅ Simulation panne gérée efficacement (retour JSON d’erreur)
