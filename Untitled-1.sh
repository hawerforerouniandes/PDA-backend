sudo docker exec -it broker ./bin/pulsar-admin topics create-partitioned-topic --partitions 1 transaccionespda
sudo docker exec -it broker ./bin/pulsar-admin topics create-partitioned-topic --partitions 1 propiedades
sudo docker exec -it broker ./bin/pulsar-admin topics list-partitioned-topics public/default