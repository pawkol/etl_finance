#!/bin/bash

# Docker network creation

if docker network ls | grep -eq "finance_network";
     then echo -e "\e[32mNetwork finance_network already exists.\e[0m"
else
     then echo -e "\e[31mNetwork finance_network is created successfully.\e[0m"
          echo "Creating docker network"
          docker network create finance_network
fi


docker compose -f db_mysql/db_mysql_docker_compose.yml up -d

docker compose -f airflow/airflow_docker_compose.yml up -d 