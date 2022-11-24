
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

## Tests-Unitarions
- Para ejecutar los test unitarios, desde la raiz del proyecto se debe ejecutar el comando 
	> python -m unittest discover .\app\unit_tests\
	> .........
	> ----------------------------------------------------------------------
	> Ran 9 tests in 0.001s
	> OK


## Test-Automáticos

- Para realizar pruebas de nuestro api, instalaremos **pytest**.

	> pip install pytest
	>
	> python -m pytest (correr test)

Resultado:
	
![enter image description here](https://i.postimg.cc/gjnJg3Vv/Whats-App-Image-2022-11-07-at-1-48-25-PM.jpg)

## Code coverage

- Instalaremos **coverage**.
	> pip install coverage

- Una vez configurado pytest y coverage, ejecutamos los siguientes comandos:
	> coverage run -m pytest
	>
	> coverage  report / coverage html (correr coverage)

Resultado:

![enter image description here](https://i.postimg.cc/kXJQrz5X/Whats-App-Image-2022-11-07-at-2-04-24-PM.jpg)

## Arquitectura del proyecto

**FastAPI** proporciona una herramienta práctica para estructurar su aplicación manteniendo toda la flexibilidad, y fácil organización de aplicaciones a gran escala, todos los componentes, recursos y características de un proyecto se mantienen y organizan por separado del otro código fuente de la aplicación.

## Arquitectura Cloud
![enter image description here](https://i.postimg.cc/76gWvzm2/Whats-App-Image-2022-11-06-at-5-38-18-PM.jpg)

## Instalando Jenkins.

   1.  Ir al sitio de descargas de Jenkins: [https://www.jenkins.io/download/](https://www.jenkins.io/download/)
    2.  Revisar los requerimientos de Hardware y Software: [https://www.jenkins.io/doc/book/installing/linux/#prerequisites](https://www.jenkins.io/doc/book/installing/linux/#prerequisites)

    3.  Al confirmar que la maquina a utilizar cumple los prerrequisitos de instalación procedemos a descargar la versión a utilizar. En este caso haremos la instalación en un Sistema Operativo Windows, por ende, usamos la opción Windows.

4. Al completar la descarga, procedemos a  revisar el manual de instalación para windows: [https://www.jenkins.io/doc/book/installing/windows/](https://www.jenkins.io/doc/book/installing/windows/)

## Configurando un nuevo pipeline de integración continua en Jenkins

1. Ir a Jenkins en [http://localhost:62427](http://localhost:62427/) y autenticarse con la cuenta admin configurada previamente, en este caso carlosadmin.

2. Al ingresar, ir a la opcion New Item.

3. Al ingresar, ir a la opcion New Item.

4. Se configuran cada uno de los puntos necesarios para el proyecto, una buena descripción, la Url de GitHub y un Display  Name que será el nombre para utilizar para la interacción de Jenkins con GitHub, en este caso usaremos Carlos-JenkinsCI.

5. Adicional  vamos a agregar un parametro (String Parameter) en el proyecto Jenkins, este se llamara BRANCH_NAME, como valor por defecto usaremos main, lo usaremos para apuntar a diferentes branch sin tener que modificar la definicion del pipeline de Jenkins.

6. Ahora, vamos a agregar los distintos eventos para ejecutar el pipeline de Jenkins. Para este escenario vamos a usar el evento Poll SCM ya que nuestra implementacion de Jenkins no tiene un acceso publico. En un escenario contrario, podriamos utilizar Github hook trigger GitScm polling o Tigger builds remotely para integrarse con Github. Pare nuesto trigger Poll SCM vamos a configurar una revision de cambios cada 15 minutos, esto lo hacemos con una adaptacion de Jenkins a una expresion CRON:

![enter image description here](https://i.postimg.cc/QdDNQCGR/Screenshot-2022-11-22-at-2-38-02-PM.png)

8. Ahora vamos a asignar un Pipeline Script, que es la definicion del proceso a ejecutar. Por ahora utilizaremos un ejemplo basico de Hello World, despues tomaremos el tiempo de construir el script de Groovy para nuestro pipeline. Y damos click en Save:

![enter image description here](https://i.postimg.cc/k4TRZ896/Screenshot-2022-11-22-at-2-39-01-PM.png)

10. Ahora haremos una ejecucion manual de prueba, usando la opcion Build with Parameters.

11. Damos click en el boton Build.

12. Y dando clic en el paso Hello veremos el Stage Log, donde esta nuestro mensaje Hellow World.

13. Ahora vamos a agregar nuestras credenciales de GitHub en Jenkins para acceder al repositorio, damos en el boton Add  Credentials cuando accedemos a la URL [http://localhost:62427/manage/credentials/store/system/domain/_/](http://localhost:62427/manage/credentials/store/system/domain/_/) :

![enter image description here](https://i.postimg.cc/bYGJ0ddv/Screenshot-2022-11-22-at-2-58-00-PM.png)

14. Ahora vamos a construir el Groovy Script para nuestro proyecto, para esto vamos a la opción Configure en nuestro Pipeline.

15. Vamos a empezar con un paso (stage) de preparación, en este stage descargaremos usando GIT la última versión de código en el repositorio de GitHub, esto lo hacemos en la sección Pipeline:

![enter image description here](https://i.postimg.cc/G2yWt0hb/Screenshot-2022-11-22-at-3-00-32-PM.png)

16. Ya con esto ahora agregamos un segundo stage de Generar Imágenes de Docker, en nuestro pipeline, dentro de Configure en la seccion Pipeline. Adicionalmente en la seccion de Preparacion agregamos la instalacion de dependencias para el proyecto:

![enter image description here](https://i.postimg.cc/VsBtTDXh/Screenshot-2022-11-22-at-3-58-20-PM.png)

17. Ahora hacemos commit del jenkinsfile y push al repositorio.

18. Ahora, vamos a Jenkins y modificamos la configuración para asignar el repositorio y archivo a utilizar en la sección de Pipeline.
19. Ahora al correr el pipeline con este cambio, veremos un paso adicional antes de nuestros pasos previos que es el que usa Jenkins para descargar la definición de nuestro Jenkinsfile que tiene control de cambios dentro del repositorio de código:

![enter image description here](https://i.postimg.cc/GpqNqkqT/Screenshot-2022-11-22-at-4-01-24-PM.png)
