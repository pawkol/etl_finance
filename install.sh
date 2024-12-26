#!/bin/bash


# Docker network creation
echo "Creating docker network"
docker network create finance_network

if docker network ls | grep -eq "finance_network";
     then echo -e "\e[32mNetwork finance_network is created successfully.\e[0m"
else
     then echo -e "\e[31mNetwork finance_network is created successfully.\e[0m"
fi
