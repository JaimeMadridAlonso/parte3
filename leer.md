#Reviews es una aplicación en java y hay que compilarla
#Hay que meterse en /bookinfo/src/reviews y ejecutar lo de abajo
#En caso de que falle, meter el .war que he descargado en bookinfo-src-reviews-reviewswlp-servers-Liberty-apps-AQUÍ

docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build


#docker compose rm -f -v
docker-compose --env-file versiones/$1.env up --build

http://localhost:9080

