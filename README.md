# Virgule

Virgule est un service API pour traiter des transcriptions textuelles en utilisant un modèle de langage (LLM) et retourner un résumé.

## Prérequis

- Python 3.12
- Docker (optionnel, pour le déploiement containerisé)

## Utilisation

### Installation locale

```sh
git clone https://github.com/yourusername/virgule.git
cd virgule
pip install -r requirements.txt
python virgule.py
```

### Docker

Construire et exécuter l'image Docker:

```sh
docker build -t virgule .
docker run -d --name virgule -p 5001:5001 virgule
```

## API

- **`POST /summarize`**: Recevoir un fichier texte contenant une transcription, et retourne un résumé.

## Séquence de fonctionnement

1. Point-Virgule enregistre une réunion et envoie la transcription au service de transcription.
2. La transcription est envoyée à Virgule pour être résumée.
3. Virgule retourne un résumé à Point-Virgule.