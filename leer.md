#Reviews es una aplicación en java y hay que compilarla
#Hay que meterse en /bookinfo/src/reviews y ejecutar lo siguiente:

cd practica_creativa2/bookinfo/src/reviews
docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
cd /home/j.malonso/Desktop/parte3/parte3

#docker compose rm -f -v

#Sustituir X por la versión 2 o 3, en caso de la versión 1 quitar la X
docker-compose -f docker-composeX.yml up --build


