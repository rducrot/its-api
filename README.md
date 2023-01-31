Issue Tracking System API
=========================
[![Python](https://badgen.net/badge/Python/3.10/blue)](https://www.python.org/)
[![Django](https://badgen.net/badge/Django/4.1/blue)](https://www.djangoproject.com/)
[![Django Rest Framework](https://badgen.net/badge/DRF/3.14/blue)](https://www.django-rest-framework.org/)

## Présentation
 Issue Tracking System API est un système de gestion de projets permettant de remonter et suivre des problèmes techniques.
## Documentation API
La documentation est disponible sur [Postman](https://www.postman.com/payload-candidate-93082268/workspace/its-api/collection/15224502-8ec6741d-8e57-4c4b-bec3-25b6a85c0316?action=share&creator=15224502).
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