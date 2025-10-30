Commande pour tester le endpoint healthCheck:
Après avoir lancer docker-compose up:
curl http://localhost:8090/health


Commande pour se connecter à la database:
psql -h localhost -p 5433 -U postgres -d appdb
