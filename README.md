Issue Tracking System API
=========================
[![Python](https://badgen.net/badge/Python/3.10/blue)](https://www.python.org/)
[![Django](https://badgen.net/badge/Django/4.1/blue)](https://www.djangoproject.com/)
[![Django Rest Framework](https://badgen.net/badge/DRF/3.14/blue)](https://www.django-rest-framework.org/)

## Présentation
 Issue Tracking System API est un système de gestion de projets permettant de remonter et suivre des problèmes techniques.
## Documentation API
La documentation est disponible sur [Postman](https://documenter.getpostman.com/view/15224502/2s935poNEt).
## Installation
1. Cloner le répertoire depuis Github, puis se placer dans le répertoire principal.
```shell
git clone https://github.com/rducrot/its-api
cd its-api
```
2. Mettre en place l'environnement virtuel.
```shell
python3 -m venv venv
source venv/bin/activate
```
3. Installer les dépendances depuis l'environnement virtuel.
```shell
pip3 install -r requirements.txt
```
## Exécution
Lancer la commande depuis le répertoire de l'application :
```shell
python3 manage.py runserver
```