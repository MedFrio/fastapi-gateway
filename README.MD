# FastAPI Gateway

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Gateway-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-2C5BB4)](https://www.uvicorn.org/)

Passerelle API basée sur FastAPI pour centraliser, sécuriser et router les appels vers des services backend.

## Fonctionnalités

- Point d'entrée unique pour les services API
- Routage et agrégation de requêtes
- Standardisation des réponses
- Base extensible pour authentification et observabilité

## Stack technique

- Python
- FastAPI
- Uvicorn
- Requests

## Prérequis

- Python 3.10+
- pip

## Démarrage rapide

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn api_gateway.main:app --reload
```

## Commandes utiles

```bash
uvicorn api_gateway.main:app --reload
```

## Licence

Projet publié sous licence MIT, sauf indication contraire dans le dépôt.

