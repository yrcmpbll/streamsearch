sudo bash down_app.sh
sudo bash docker_clean_up.sh
sudo docker build -t stream-search-app -f src/docker_app/Dockerfile .
sudo docker build -t stream-search-app-seeder -f src/docker_seeder/Dockerfile .
sudo docker compose -f src/docker_stack/docker-compose.yml up -d