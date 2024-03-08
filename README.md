# Repositorio Propiedades de los alpes

Repositorio con implementación de servicios de propiedades de los alpes siguiendo los principios y patrones de DDD.

## Requerimientos
- Python 
- docker
- docker-compose
- python3.9


## Estructura del proyecto

El repositorio en su raíz está estructurado de la siguiente forma:

- **.github**: Directorio donde se localizan templates para Github y los CI/CD workflows 
- **src**: En este directorio encuentra el código fuente para proyecto, propiedades de los alpes.
  - pda-propiedades-command : Microservicio de propiedades command
  - pda-propiedades-query : Microservicio de propiedades query
  - pda-transacciones-command : Microservicio de transacciones command
  - pda-transacciones-query : Microservicio de transacciones query
- **deployment**: Definicion de despliegue en kubernetes
- **.gitignore**: Archivo con la definición de archivos que se deben ignorar en el repositorio GIT
- **.gitpod.yml**: Archivo que define las tareas/pasos a ejecutar para configurar su workspace en Gitpod
- **README.md**: El archivo que está leyendo :)
- **requirements.txt**: Archivo con los requerimientos para el correcto funcionamiento del proyecto (librerias Python)


### Inicializar pulsar 

Desde el directorio principal ejecute el siguiente comando desde la terminal de comandos.

```bash
docker-compose  --profile pulsar up
```

una vez este arriba los servicios procedemos a crear los topics

```bash
docker exec -it broker ./bin/pulsar-admin topics create-partitioned-topic --partitions 1 transaccionespda
docker exec -it broker ./bin/pulsar-admin topics create-partitioned-topic --partitions 1 propiedades
docker exec -it broker ./bin/pulsar-admin topics create-partitioned-topic --partitions 1 saga-log
docker exec -it broker ./bin/pulsar-admin topics list-partitioned-topics public/default
```
lo anterior creara los topics necesarios para el proyecto y listara los mismos


Opcional puede leer los topics 
docker exec -it broker ./bin/pulsar-client consume -s sub apache/pulsar

despues de esto procedemos a crear los esquemas 



```bash
curl -i -X POST \
  http://35.222.56.106:8080/admin/v2/schemas/public/35.222.56.106/schema \
  -H "Content-Type: application/json" \
  --data-binary "@schemas/transacciones.json"

curl -i -X POST \
  http://35.222.56.106:8080/admin/v2/schemas/public/default/propiedades/schema \
  -H "Content-Type: application/json" \
  --data-binary "@schemas/propiedades.json"

  curl -i -X POST \
  http://35.222.56.106:8080/admin/v2/schemas/public/default/saga-log/schema \
  -H "Content-Type: application/json" \
  --data-binary "@schemas/saga_log.json"



```


## Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/pda-propiedades-command/api run
flask --app src/pda-propiedades-query/api run
flask --app src/pda-transacciones-command/api run
flask --app src/pda-transacciones-query/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/pda-propiedades-command/api --debug run
flask --app src/pda-propiedades-query/api --debug run
flask --app src/pda-transacciones-command/api --debug run
flask --app src/pda-transacciones-query/api --debug run
```

## start project 

Procederemos a crear un ambiente virtual para poder ejecutar nuestras dependencias

```bash
python3 -m venv venv    
source venv/bin/activate 
python3 -m pip install -r requirements.txt

```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker-compose --profile pulsar up
```

## Request de ejemplo

Los siguientes JSON pueden ser usados para probar el API:

### Crear Propiedad

- **Endpoint**: `/propiedades/propiedad`
- **Método**: `POST`
- **Headers**: `Content-Type='aplication/json'`

```json
{
        "nombre":"nombre de la propiedad",
        "informacion_geoespacial":{
            "direccion": "",
            "ciudad": "ciudad",
            "departamento":"",
            "pais":""
        }, 
        "informacion_compania": {
            "nombre_propietario":"",
            "nit":"",
            "telefono":""
        },
        "informacion_contractual":{
            "fotografias":["url","url2","url3"]
        },
        "informacion_catastral":{
            "tipo":"Oficina,Industial, uso_especializado",
            "tamano":"m2",
            "tipo_construccion":"casa,edificio",
            "numero_pisos":""
        }
}
```

### Asignar Transaccion

- **Endpoint**: `/propiedades/propiedad/transaccion`
- **Método**: `POST`
- **Headers**: `Content-Type='aplication/json'`

```json
{
    "id_propiedad":"0e81c002-d514-4409-89d5-95822c332618",
    "nombre_tomador": "Ricardo Tellez",
    "nombre_propietario":"Evaristo Rendon"
}
```


### Consulta Transaccion

- **Endpoint**: `/transacciones/{idTransaccion}`
- **Método**: `GET`
- **Headers**: `Content-Type='aplication/json'`

host gpc http://34.135.217.167.nip.io
