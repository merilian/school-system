docker stop school_system
docker rm school_system

docker build . -t school_system
docker run --name school_system --network school_system_network -d -p 5000:5000 school_system
