#Reviews es una aplicación en java y hay que compilarla
#Hay que meterse en /bookinfo/src/reviews y ejecutar la línea de abajo

cd /practica_creativa2/bookinfo/src/reviews
docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
cd /home/j.malonso/Desktop/parte3/parte3

#docker compose rm -f -v
docker-compose --env-file versiones/$1.env up --build

http://localhost:9080

