# Make sure to check bin/run_services.sh, which can be used here

# Do not forget to expose the right ports! (Check the PR_4.md)

# Utiliser une image de base avec Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY src/web_service /app/src/web_service
COPY bin/run_services.sh /app/bin/run_services.sh
COPY requirements.txt /app/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Rendre le script exécutable
RUN chmod +x /app/bin/run_services.sh

# Exposer les ports de l'API et du serveur Prefect
EXPOSE 8001 4201

# Commande pour lancer les services
CMD ["/app/bin/run_services.sh"]