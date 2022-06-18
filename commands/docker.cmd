docker pull mariadb:10.4
docker images
docker run --name mariadbcountries -e MYSQL_ROOT_PASSWORD=mypas1s2 -p 3306:3306 -d docker.io/library/mariadb:10.4
docker run --name mariadbcountries -e MYSQL_ROOT_PASSWORD=my#pa$s1s2 -p 3306:3306 -d mariadb:10.4 --log-bin --binlog-format=MIXED

docker ps
docker restart mariadbcountries
docker stop mariadbcountries
docker start mariadbcountries
docker stop --time=30 mariadbcountries
docker kill mariadbcountries
docker rm mariadbcountries
docker rm -v mariadbcountries

docker exec -it -u 0 mariadbcountries sh
mysql -u root -p

docker exec -u 0 mariadbcountries whoami
apt-get update
apt-get install vim


docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadbcountries
172.17.0.02