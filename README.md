# Repositorio Propiedades de los alpes

Repositorio con implementación de servicios de propiedades de los alpes siguiendo los principios y patrones de DDD.


## Estructura del proyecto

El repositorio en su raíz está estructurado de la siguiente forma:

- **.github**: Directorio donde se localizan templates para Github y los CI/CD workflows 
- **src**: En este directorio encuentra el código fuente para proyecto, propiedades de los alpes.
- **tests**: Directorio con todos los archivos de prueba, tanto unitarios como de integración. Sigue el estándar [recomendado por pytest](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html) y usado por [boto](https://github.com/boto/boto).
- **.gitignore**: Archivo con la definición de archivos que se deben ignorar en el repositorio GIT
- **.gitpod.yml**: Archivo que define las tareas/pasos a ejecutar para configurar su workspace en Gitpod
- **README.md**: El archivo que está leyendo :)
- **requirements.txt**: Archivo con los requerimientos para el correcto funcionamiento del proyecto (librerias Python)


## Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/pda/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/pda/api --debug run
```


## Request de ejemplo

Los siguientes JSON pueden ser usados para probar el API:

### Crear Propiedad

- **Endpoint**: `/propiedad`
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

### Consultar propiedad

- **Endpoint**: `/propiedad/{id}`
- **Método**: `GET`
- **Headers**: `Content-Type='aplication/json'`

## Ejecutar pruebas

```bash
coverage run -m pytest
```

# Ver reporte de cobertura
```bash
coverage report
```
