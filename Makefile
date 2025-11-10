psql-up:
docker compose -f .docker/docker-compose.yml up -d --build --force-recreate --remove-orphans db

psql-down:
sudo docker compose -f .docker/docker-compose.yml down -v --remove-orphans