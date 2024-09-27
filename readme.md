# Proyecto Urban Routes 
## Brandon Alejandro Montalvo García 
## Cohort:13
## Sprint 8

### Descripción

Este proyecto implementa una serie de pruebas automatizadas utilizando pytest y selenium webDriver para una plataforma de viajes. 

El objetivo principal es verificar el correcto funcionamiento de las funcionalidades clave relacionadas con la definición de rutas, seleccionar tipos de viaje, metodos de pago y requisitos extras al conductor.

### Documentación
Unicamente se contaba con la Urban Routes URL ya que los localizadores se obtuvieron gracias a la herramienta DevTools.
https://cnt-5723fb89-f73b-4f99-a6c9-ecc8820522a1.containerhub.tripleten-services.com?lng=es

### Tecnlogías usadas
####  Pycharm: 
Para elaborar el correspondiente script de esta actividad.

##### Instalación de PyCharm:

1. Dirígete al sitio oficial de PyCharm: JetBrains PyCharm.
2. Descarga la versión Community (gratuita) o Professional (de pago).
3. Ejecuta el archivo descargado e instala PyCharm siguiendo las instrucciones del instalador.
4. Abre PyCharm y crea un proyecto o abre uno existente.

#### Pytest:
Para la ejecución de las pruebas.

##### Instalación de Pytest

1. Abre PyCharm o una terminal (como Git Bash o el CMD de Windows).
2. Verifica que Python esté instalado ejecutando python --version.
3. Instala pytest ejecutando el siguiente comando en la terminal o consola de PyCharm: _pip install pytest_.
4. Verifica la instalación ejecutando: _pytest --version_

#### Selenium WebDriver:

Es un controlador de navegador. Su principal uso es implementar el código de control del navegador y para emular las acciones de usuario.

##### Instalación de Selenium WebDriver

Para trabajar con Selenium WebDriver, necesitas conectarlo con tu IDE.
1. Instala el controlador del navegador
* Acceder al sitio oficial de Selenium donde se encuentran los drivers 
* Selecciona la versión del controlador que coincida con tu versión de navegador. 
* Hay varios archivos comprimidos en la carpeta. Descarga el que coincida con tu sistema operativo. 
* Descomprime el archivo. Crea una carpeta llamada WebDriver/bin y guarda el archivo allí. 
* Agrega la ruta a bin a la variable de entorno PATH. El algoritmo depende del sistema operativo.
2. Instala Selenium para Python
* Abrir la Consola o Terminal Terminal desde las aplicaciones o usando el buscador de aplicaciones.
* Ejecutar el Comando de Instalación
* Escribe el siguiente comando para instalar el paquete de Selenium: _pip install selenium_
3. Abre el navegador con PyCharm
* Importa el paquete Selenium WebDriver:
_from selenium import webdriver_
* Importa el paquete time:
_import time_
* Activa el controlador del navegador. Así es como lo hicimos para Chrome:
_webdriver.Chrome()_

#### Ejecución de test.

Mediante la interfaz de PyCharm:

1. En el menú "Run", selecciona "Edit Configurations" (Editar configuraciones).
2. Haz clic en "+ (Add New Configuration)" (Agregar nueva configuración) en una ventana nueva.
3. Selecciona "Python tests → pytest" (Pruebas de Python → Pytest) en la lista de configuraciones.
4. Aparecerá una ventana nueva. El "Script path" está seleccionado en la línea "Target" de forma predeterminada. No cambies nada aquí.
5. Selecciona el archivo con tus pruebas en el campo debajo de "Target". Puedes hacerlo haciendo clic en el ícono con forma de carpeta.
6. Haz clic en "Apply" (Aplicar) y luego en "OK" (Aceptar).
7. Ahora haz clic en el ícono de la flecha verde para iniciar la configuración y observa los resultados:

De esta manera se ejecutaran las pruebas en el archivo y se podrán visualizar las pruebas ejecutadas en pantalla.
