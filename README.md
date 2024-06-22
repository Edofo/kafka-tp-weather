# Procédure de lancement du projet

### 1. Clôner ce projet

```bash
git clone https://github.com/edofo/kafka-tp-weather.git ./my-app
```

### 2. Obtenir une clé d'API

Créer un compte sur https://www.weatherapi.com/.

Une fois que vous aurez créé votre compte, vous disposerez d'une clé d'API affichée dans votre compte utilisateur.
Pas de clé ? 
Renseigner la clé dans le fichier `setup.sh`

```bash
API_KEY = "XXX" 

```

## [Linux] Lancer l'application depuis un script bash

```bash
cd ./my-app
chmod +x setup.sh
./setup.sh
```

L'application est disponible à l'adresse suivante : `http://localhost:8501/`

## Setup manuel

### 1. Clôner ce projet

```bash
git clone https://github.com/edofo/kafka-tp-weather.git ./my-app
```

### 2. Lancer le docker-compose en mode détaché

```bash
cd my-app/tp-kafka/docker-compose/kafka-kafdrop
```

```bash
docker compose build
```

```bash
docker compose up -d
```

### 3. Rendre le container `kafka-kafdrop-kafka-1` interactif

```bash
docker exec -it kafka-kafdrop-kafka-1 /bin/bash
```

### 4. [Conteneur] Installer Python et kafka-python

```bash
apk add --no-cache python3 py3-pip; pip3 install kafka-python
```

### 5. [Conteneur] Lancer `velib-get-stations.py`

```bash
python3 opt/kafka/bin/resources/weather-get-paris.py
```

L'application est disponible à l'adresse suivante : http://localhost:8501/ avec les données en temps réel
