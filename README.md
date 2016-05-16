### Introducción
Proyecto 1 (_En desarrollo_):

Una pequeña aplicación web en Django (1.9.5) para gestionar el proceso de reparación de equipos electrónicos, manteniendo registro de:
* clientes
* ingreso y egreso de equipos electrónicos
* fallas y diagnósticos de equipos
* progreso de la reparación



### Entorno
* Debian Jessie
* PostgreSQL (sugerido)

### Instalación
1. Crear la base de datos para el proyecto
2. Instalar las dependencias de sistema
   
   ```
   # apt-get install $(cat build-dependencies.txt | awk '{print $1}') -y
   ```
3. Instalar los módulos de python
   
   ```
   $ pip install -r py-requirements.txt
   ```
4. Establecer las variables de entorno enumeradas en `env-vars`, necesarias para el archivo `settings.py` de Django
Como alternativa se puede editar el archivo y definirlas directamente allí, y luego exportarlas con el siguiente comando:
   ```
   export $(cat env-vars | xargs)
   ```

### Alternativa con docker en un container
1. Reemplazar `sources.list` y `bashrc` por archivos propios
2. Crear la imagen (llámese por ej: _miniappservice_)
   
   ```
   $ docker build -t miniappservice .
   ```
3. Editar y definir las variables en el archivo ```env-vars```
4. Correr un container a partir de la imagen creada, cargando las variables de entorno (`--env-file`) y bindeando un volumen al directorio de la aplicación (`-v`). Ejemplo:
   
   ```
   $ docker run -it --rm -p 8000:8000 -h host-miniappservice --env-file [<ruta_absoluta>/]env-vars -v <ruta_absoluta>/miniappservice:<ruta_dentro_de_container> miniappservice bash
   ```
   opcionalmente, si la base de datos PostgreSQL corre en otro container*:
   
   ```
   --link <nombre_container_postgres>:postgres 
   ```