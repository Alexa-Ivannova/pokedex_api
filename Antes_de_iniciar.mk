# ENDPOINT PARA:
# Request:
# get recbir --> El front pide algo al backend (PEDIR PARA RECIBIR) --> Pide menú, api va po el menu, se devuelve entrega el manú
# post enviar --> (HACER PEDIDO NUEVO) --> Front pide lista de comida(body request), api lleva body request y PIDE lo que quiere el usuario, el back hace un response envia RESPUESTA
# put cambiar --> (HACE UNA ACTUALIZACION CAMBIO ANTES DE Q LLEGUE AL BACKEND)
# delete eliminar --> (CANCELA LA ORDEN)

# Response: el backend envia respuestas--- hay codigos para indicar q una respuesta es satisfactoria o no:


# PASO UNO CONFUGIRAR EL ENTORNO VIRTUAL --> 
# En la terminal:  python3 -m venv .venv

# PASO DOS ACTIVAR EL ENTORNO VIRTUAL: 
# powershell  venv\Scripts\Activate.ps1  
# cmd: .venv\Scripts\activate.bat

# PASO DOS ACTIVAR EL ENTORNO VIRTUAL: 
# deactivate

# INSTALAR PIP: Libreria que nos permite tener todas las dependencias (Manejador de paquetes-- AppStore) 
# pip install --upgrade pip 
# pip install psycopg2-binary
# pip install flask 
# pip install marshmallow
# pip install pytest
# pip install marshmallow python-dotenv

# PARA INSTALAR TODAS LAS DEPENDENCIAS, DEBO GUARDARLAS EN UN ARCHIVO LLAMADO .requirements.txt POSTERIORMENTE COLOCO EN LA TERMINAL: pip install -r requirements.txt 
# ESE comando instalara todas las dependencias que ingrese en el txt


# CREAR BASES DE DATOS



# VARIABLES DE ENTORNO: Se crean con .env ... guarda info privada, permite trabajar dentro de la api, pero no se puede compartir con nadie fuera del etorno de trabajo... ESTO TIENE LA BD... 

# VARIABLE ENTORNO: DATABASE_URL

# LEVANTAR SERVIDOR: python -m src.app 