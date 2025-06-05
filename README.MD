# 🍽️ API Gateway - Projet Microservices Restaurant

Ce projet constitue l'**API Gateway** d'une application de gestion de commandes pour un restaurant. Il s'inscrit dans une architecture **microservices** répartie entre plusieurs domaines métier : client, commande, cuisine et livraison.

## 📌 Objectifs

- Servir de **point d'entrée unique** pour le Frontend.
- Centraliser les appels vers les microservices.
- Simuler les échanges avec les services pour permettre une démo complète même sans services réels.
- Gérer les erreurs et **assurer un mode dégradé**.

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
├── main.py # Point d’entrée de l’API Gateway
├── services/ # Regroupe les routes par domaine fonctionnel
│ ├── auth.py # Authentification utilisateurs
│ ├── orders.py # Commandes client
│ ├── kitchen.py # Statut préparation cuisine
│ └── delivery.py # Livraison des commandes
├── utils/
│ └── http_client.py # Gestion centralisée des requêtes HTTP (simule les microservices)
└── requirements.txt # Dépendances Python

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

| Méthode | Endpoint              | Description                                         |
|---------|-----------------------|-----------------------------------------------------|
| `POST`  | `/auth/login`         | Connexion utilisateur simulée (client, chef, livreur) |
| `GET`   | `/orders`             | Liste des commandes                                 |
| `POST`  | `/orders`             | Création d’une commande                             |
| `GET`   | `/kitchen/orders`     | Commandes à préparer                                |
| `POST`  | `/kitchen/update`     | Mettre à jour le statut cuisine                     |
| `GET`   | `/delivery/assigned`  | Liste des commandes à livrer                        |
| `POST`  | `/delivery/update`    | Mise à jour de la livraison                         |

---

## 🧪 Simulation de panne & mode dégradé

Le module `http_client.py` simule les appels vers les microservices.  
En cas de panne ou d’indisponibilité (par exemple, suppression temporaire d’une route), l’API Gateway :

- Renvoie un message d’erreur clair au frontend
- Garde les autres fonctionnalités opérationnelles

---

## ✅ Objectifs pédagogiques couverts

- ✅ Présentation claire du contexte et des services
- ✅ Démonstration fonctionnelle complète (auth, commande, cuisine, livraison)
- ✅ Architecture Microservices respectée (Gateway + découpage logique)
- ✅ Simulation panne gérée efficacement (retour JSON d’erreur)
