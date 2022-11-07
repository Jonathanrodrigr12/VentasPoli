# Ventas Poli

En este punto se ha creado el proyecto dentro de los repositorios Github. Esta semana se
emplea una de las herramientas más valiosas para la integración continua: Docker. Para, a
través de esta herramienta, construir dos contenedores los cuales deben estar comunicados
entre sí.

# Instalación y configuración

Requisitos previos

- Python 3.10+.
- Framework FastAip.
- Ubicarse en la raiz del proyecto.

Una vez configurado python, estará listo para comenzar:

- Para gestionar los paquetes de software para Python, instalaremos **pip**.

	> sudo apt install -y python3-pip
	> 
	> pip3 install package_name
	> 
	> pip3 install package_name
	> 
	> sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

Configurar un entorno virtual:

- Los entornos virtuales le permiten tener un espacio aislado en su servidor para proyectos de Python.
	> sudo apt install -y python3-venv
	> 
	> sudo apt install -y python3-venv
	> 
	> python3 -m venv my_env

- Para utilizar este entorno, debe activarlo escribiendo el siguiente comando que llama a la secuencia de comandos **active**:
	> source my_env/bin/activate
	> 
       Activa: (venv) admin@Sebas011 BackendVentasPoli % :
       Inactiva: admin@Sebas011 BackendVentasPoli % : 	

- Con nuestro entorno virtual activo ahora procedemos a instalar FastAPI framework:
	> pip install fastapi
	> 
	> pip install "uvicorn[standard]"

- Ahora instalaremos las librerías que están en el documento requirements.txt:
	> pip install -r requirements.txt
 
 - Por ultimo, Iniciar servidor:
	> uvicorn main:app --reload
	>
        Ejemplo que el servidor inicio: INFO: Will watch for changes in these directories:
        INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
        INFO:     Started reloader process [82405] using watchgod
        INFO:     Started server process [82409]
        INFO:     Waiting for application startup.
        INFO:     Application startup complete.
        
## Test-Automáticos

- Para realizar pruebas de nuestro api, instalaremos **pytest**.

	> pip install pytest
	>
	> python -m pytest (correr test)

Resultado:
	
![enter image description here](https://i.postimg.cc/gjnJg3Vv/Whats-App-Image-2022-11-07-at-1-48-25-PM.jpg)

## Arquitectura del proyecto

**FastAPI** proporciona una herramienta práctica para estructurar su aplicación manteniendo toda la flexibilidad, y fácil organización de aplicaciones a gran escala, todos los componentes, recursos y características de un proyecto se mantienen y organizan por separado del otro código fuente de la aplicación.

## Arquitectura Cloud
![enter image description here](https://i.postimg.cc/76gWvzm2/Whats-App-Image-2022-11-06-at-5-38-18-PM.jpg)
