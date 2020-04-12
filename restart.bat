docker network rm school_system_network
docker network create school_system_network

docker stop school_system
docker rm school_system

docker stop school_system_db
docker rm school_system_db

docker build ./database -t school_system_db
docker run --name school_system_db --network school_system_network -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret! -d school_system_db

docker build . -t school_system
docker run --name school_system --network school_system_network -d -p 5000:5000 school_system
