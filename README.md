### 👍 Título
    ## STORE_ONLINE

### 👍 Descripción:
    ▶️ tienda e-commerce que ejecuta funciones basicas, (autenticarse, listar productos existentes, comprar, agregar al carrito, desde un punto de vista del usuario.
    un administrador puede crear,actualizar, listar y eliminar productos)

### 👍 Estado
    ▶️ En desarrollo

### 👍 Tecnologías

    ▶️ Python
    ▶️ Django
    ▶️ Git, Github
    ▶️ Postgres

### 👍 Instalación

    ▶️ Crear proyecto
        👍 clonar repositorio 
        git clone https://git.com/g120795/tienda_online.git

        👇 raiz del proyecto: 
        cd tienda_online
        
        👍 crear entorno virtual
        python -m venv venv

        👍activar entorno virtual
        source venv/bin/activate
        wich python (la salida debe apuntar al entorno virtual creado)

        👍 instalar dependencias
        pip install -r requirements.txt

        👍 crear .env para almacenar las variables de la db(opcional)
        desde la terminal de linux
        nano .env

        👍 agregar variables dentro de .env con valores creados en la base de datos, puedes usar docker, es mas facil.
        POSTGRES_DB=tienda_online
        POSTGRES_USER=tu_usuario
        POSTGRES_PASSWORD=tu_contraseña
        POSTGRES_HOST=127.0.0.1
        POSTGRES_PORT=5432 (por defecto si no tienes mas proyectos corriendo)

        recuerda que tienes que tener una base de datos activa para seguir 

        👍 ejecutar migraciones



        👍 crear superuser



        👍 iniciar servidor



        🚀 Uso
            Accede a: http://127.0.0.1:8000/
            
            Admin: /admin/ (para gestionar productos, proveedores, etc.)
            
            Login: /accounts/login/
            
            Registro: /accounts/register/

        


    
        















































