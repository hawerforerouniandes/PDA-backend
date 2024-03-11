docker build --platform=linux/amd64 -t propiedades-command:3.0.0 -f pda-propiedades-command.Dockerfile .  
docker build --platform=linux/amd64 -t propiedades-query:3.0.0 -f pda-propiedades-query.Dockerfile . 
docker build --platform=linux/amd64 -t transacciones-command:3.0.0 -f pda-transacciones-command.Dockerfile . 
docker build --platform=linux/amd64 -t transacciones-query:3.0.0 -f pda-transacciones-query.Dockerfile . 




docker tag propiedades-command:3.0.0 us-central1-docker.pkg.dev/alpes-propiedades/alpes-propiedades/propiedades-command:3.0.0
docker tag propiedades-query:3.0.0 us-central1-docker.pkg.dev/alpes-propiedades/alpes-propiedades/propiedades-query:3.0.0
docker tag transacciones-command:3.0.0 us-central1-docker.pkg.dev/alpes-propiedades/alpes-propiedades/transacciones-command:3.0.0
docker tag transacciones-query:3.0.0 us-central1-docker.pkg.dev/alpes-propiedades/alpes-propiedades/transacciones-query:3.0.0

docker push us-central1-docker.pkg.dev/alpes-propiedades/alpes-propiedades/propiedades-command:3.0.0
docker push us-central1-docker.pkg.dev/alpes-propiedades/alpes-propiedades/propiedades-query:3.0.0
docker push us-central1-docker.pkg.dev/alpes-propiedades/alpes-propiedades/transacciones-command:3.0.0
docker push us-central1-docker.pkg.dev/alpes-propiedades/alpes-propiedades/transacciones-query:3.0.0