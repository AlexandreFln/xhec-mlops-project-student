# Make sure to check bin/run_services.sh, which can be used here

# Do not forget to expose the right ports! (Check the PR_4.md)

# Utiliser une image de base avec Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY src/web_service /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de l'API
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
