# DeepLearningProject
# Conteo de Personas con YOLO y Ultralytics

Este proyecto utiliza el modelo YOLO (You Only Look Once) y la biblioteca Ultralytics para realizar el conteo de personas en áreas seleccionadas a partir de imágenes de video o la cámara en tiempo real. Este proyecto implementa un sistema de conteo de personas basado en el modelo YOLO y la biblioteca Ultralytics. Los usuarios tienen la capacidad de seleccionar áreas de interés mediante la interfaz gráfica, permitiendo la detección y seguimiento eficiente de personas en tiempo real a través de un video o la cámara. La visualización gráfica ofrece información detallada, incluyendo áreas destacadas, conteo actualizado de personas y detalles visuales sobre las personas detectadas. La interfaz de usuario, diseñada para ser intuitiva, facilita la interacción del usuario para un control sencillo del programa. El archivo README.md proporciona información completa sobre requisitos, instalación, uso y contribuciones al proyecto. Este sistema ofrece una solución efectiva y accesible para el conteo de personas en áreas específicas, aprovechando la potencia de YOLO y Ultralytics.

## Requisitos

- Python 3.x
- Bibliotecas:
  Opencv-python
  Pillow (PIL)
  Shapely
  Ultralytics YOLO
  Tkinter
  NumPy

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Fabria1998/DeepLearningProject
   cd DeepLearningProject


## Requisitos

- Lista de requisitos y dependencias.

## Instalación

Instrucciones para instalar y configurar el proyecto.
Intstalacion de bibliotecas:
    ```bash
    pip install opencv-python
    pip install shapely
    pip install ultralytics
    pip install numpy
    pip install pillow
    pip install tkinter



## Uso
## Con el Explorador de Archivos de Windos:
1. Abrimos el Explorador de archivos.
2. Buscamos el lugar donde guardamos el .zip descargado.
3. Extraemos.
4. ingresamos a la carpeta 'DeepLearningProject-main'
5. damos Click en er archivo main.py
## Con el simbolo del sistema:
1. Despues de descomprimir el .zip descargado, abrimos el simbolo de sistema y ponemos:
   ```bash
   cd --> copiamos el directoria de la carpeta descomprimida donde estan nuestro programa.
7. Ejecutar el archivo main.py
   ```bash
   python main.py

## Funcionamiento
Este manual proporciona instrucciones detalladas sobre cómo utilizar el programa para el conteo de personas basado en YOLO y Ultralytics. El proceso se divide en tres secciones: Interfaz, Detección con Cámara y Detección con Video.

Interfaz:
Botón "Iniciar Cámara":
Al presionar el botón "Iniciar Cámara", se abrirá una interfaz gráfica.
Dibuja áreas de interés haciendo clic en la ventana de la cámara.
Presiona la tecla "n" para iniciar una nueva área.
Utiliza la tecla "c" para eliminar puntos del área.
Presiona la tecla 'Enter' para finalizar la selección de áreas.
Observa el conteo de personas en una ventana emergente

Botón "Cargar Video":
Al presionar el botón "Cargar Video", selecciona un archivo de video (formatos webm o mp4).
Dibuja áreas de interés siguiendo los mismos pasos mencionados anteriormente.
Presiona la tecla 'Enter' para finalizar la selección de áreas.
Observa el conteo de personas en una ventana emergente.

Botón "Instrucciones":
Al presionar el botón "Instrucciones", se muestra la forma correcta de como utilizar el programa.

Botón "Información":
Al presionar el botón "Información", se podra observar informacion de las librerias importantes utilizadas en este programa.

Botón "Salir":
Cerrar el Programa.



