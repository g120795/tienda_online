RAIZ DEL PROYECTO
/~/tienda_online
    *description:
        tienda_online, es un proyecto que tiene como proposito basico, permitir cumplir funciones basicas de una tienda e_commerce, con transacciones basicas como, navegar por una lista de productos, ver sus detalles,comprar , añadir al carrito de compras.
    
    *tecnologias usadas:
        revisar el archivo requirements.txt en la raiz del proyecto.

    *arbol de directorio
        ├── apps
        ├── config
        ├── docs
        ├── manage.py
        ├── requirements.txt
        ├── templates
        └── venv

        directorios fundamentales del proyecto en config
            apps:
            contiene las aplicaciones que creamos con el administrador de django.

            

                store: app que contiene los modelos vistas urls y formas de la tienda.(contiene la logica de negocio del proyecto)
                users: app que creada exclusivamente para desarrollar un perfil de usuario despues de que este se registrara en la aplicacion.

            config:contiene la configuracion general del proyecto, y el archivo principal es settings.py.

                arbol de directorio
                ├── __init__.py
                ├── __pycache__
                ├── asgi.py
                ├── settings.py
                ├── templates
                ├── urls.py
                ├── views.py
                └── wsgi.py


                settings:
                    INSTALLED_APPS: nombre de app internas y del proyecto
                    MIDDLEWARE:
                    ROOT_URLCONF: ruta del proyecto
                    TEMPLATES: ruta de las carpetas raiz de los templates del proyecto
                    WSGI_APPLICATION
                    DATABASES: datos de la db o variables hacia los datos de la db
                    AUTH_PASSWORD_VALIDATORS: validadores de contraseñas
                    LANGUAGE_CODE
                    TIME_ZONE
                    USE_I18N
                    USE_TZ
                    STATIC_URL
                
                urls:contiene los path raiz del proyecto


























































