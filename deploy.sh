#!/bin/bash


IMAGE_NAME="django:api"

CONTAINER_NAME="central-api"


echo "Construindo a imagem Docker..."
docker build --tag $IMAGE_NAME .


if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Parando e removendo o contêiner existente..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

echo "Iniciando um novo contêiner..."
docker run --name $CONTAINER_NAME -d -p 3333:3333 $IMAGE_NAME