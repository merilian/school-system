docker network create school_network

docker build ./database -t students_db
docker run --name students_db --network school_network -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret! -d students_db

docker build . -t school_system
docker run --name school_system --network school_network -d -p 5000:5000 school_system
