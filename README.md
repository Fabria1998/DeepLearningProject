# DeepLearningProject
# Conteo de Personas con YOLO y Ultralytics

Este proyecto utiliza el modelo YOLO (You Only Look Once) y la biblioteca Ultralytics para realizar el conteo de personas en áreas seleccionadas a partir de imágenes de video o la cámara en tiempo real. Este proyecto implementa un sistema de conteo de personas basado en el modelo YOLO y la biblioteca Ultralytics. Los usuarios tienen la capacidad de seleccionar áreas de interés mediante la interfaz gráfica, permitiendo la detección y seguimiento eficiente de personas en tiempo real a través de un video o la cámara. La visualización gráfica ofrece información detallada, incluyendo áreas destacadas, conteo actualizado de personas y detalles visuales sobre las personas detectadas. La interfaz de usuario, diseñada para ser intuitiva, facilita la interacción del usuario para un control sencillo del programa. El archivo README.md proporciona información completa sobre requisitos, instalación, uso y contribuciones al proyecto. Este sistema ofrece una solución efectiva y accesible para el conteo de personas en áreas específicas, aprovechando la potencia de YOLO y Ultralytics.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Fabria1998/DeepLearningProject
2. luego:
   
   ```bash
   cd DeepLearningProject
   
4. Para ejecutar:

   ```bash
   python main.py


## Requisitos

Los requisitos para ejecutar el programa de conteo de personas con YOLO y Ultralytics son los siguientes:

- Python:
Asegúrate de tener Python instalado en tu sistema. El programa está diseñado para funcionar con Python 3.
  - Python 3.x
- Bibliotecas:
  - Opencv-python
  - Pillow (PIL)
  - Shapely
  - Ultralytics YOLO
  - Tkinter
  - NumPy


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
![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/67569b69-50d3-42e4-b660-75be4b274f5b)

3. Buscamos el lugar donde guardamos el .zip descargado.
![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/64847906-3ddc-472a-af0b-d94c94c91e3e)

5. Extraemos.
![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/989aa331-71f6-4756-9e18-a32c93a7bb38)

7. ingresamos a la carpeta 'DeepLearningProject-main'
![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/62fd634f-3571-44f8-89a4-c75d61b07e69)

9. damos Click en er archivo main.py
![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/c71f2574-e622-4263-92ea-d27b33b0215c)

10. Observamos el Interfaz de nuestro programa:
![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/888f678a-e8cc-4661-acf4-f921d9b889df)



## Con el simbolo del sistema:
1. Despues de descomprimir el .zip descargado, abrimos el simbolo de sistema y ponemos:
   ```bash
   cd --> copiamos el directoria de la carpeta descomprimida donde estan nuestro programa.
2. Ejecutar el archivo main.py
   ```bash
   python main.py

![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/80c33356-6b9a-4c38-82de-439f74e28fbb)

3. Observamos:
![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/6ad4bb59-4a8d-4cfd-9e58-f84a947f988f)



## Funcionamiento
Este manual proporciona instrucciones detalladas sobre cómo utilizar el programa para el conteo de personas basado en YOLO y Ultralytics. El proceso se divide en tres secciones: Interfaz, Detección con Cámara y Detección con Video.

  ## Interfaz:
  Botón "Iniciar Cámara":
  - Al presionar el botón "Iniciar Cámara", se abrirá una interfaz gráfica.
    
  ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/44fd2497-b701-4673-b6dc-8f1b0b93f03e)

  ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/53827c68-dff5-4f33-9958-aadbccb2a44e)

  - Dibuja áreas de interés haciendo clic en la ventana de la cámara.
    
  ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/80138ffd-4457-4afd-b54b-97b4ba8b87dd)
  

  - Presiona la tecla "n" para iniciar una nueva área.
  - Utiliza la tecla "c" para eliminar puntos del área.
  - Presiona la tecla 'Enter' para finalizar la selección de áreas.
    
  ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/fd976251-b3b3-41f8-83fd-83220e6d87bc)


  - Observa el conteo de personas en una ventana emergente:
    
    ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/5845a59d-9269-45d7-ad5a-599103c0b409)

  Botón "Video":
  - Al presionar el botón " Video", selecciona un archivo de video (formatos webm o mp4).
    
    ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/92410c80-3a9f-4190-8d4b-6eca3f4cfdc5)

  - Dibuja áreas de interés siguiendo los mismos pasos mencionados anteriormente.
    
    ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/50244252-f75e-407e-80e1-00d3d4866d62)
    
  - Presiona la tecla 'Enter' para finalizar la selección de áreas.

    ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/de913b3c-da3d-427e-abe2-d05ed27aebf0)

  - Observa el conteo de personas en una ventana emergente.

    ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/074036c5-a419-4f5d-9c72-9190d680d7b1)


  Botón "Instrucciones":
  
   ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/f2b13f08-a761-4ead-85a0-23c1ddcbd642)

  Al presionar el botón "Instrucciones", se muestra la forma correcta de como utilizar el programa.
  
  ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/b2ced120-ef05-42d4-8493-517944d52ec1)


  Botón "Información":
  
  ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/4005e6ed-90e6-4beb-8c0b-e8582ab30599)
  
  Al presionar el botón "Información", se podra observar informacion de las librerias importantes utilizadas en este programa.
  
  ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/dfbb1103-b201-41fe-8669-792130bfe6ff)

  

  Botón "Salir":

  
  ![image](https://github.com/Fabria1998/DeepLearningProject/assets/159462180/60748bb8-d018-4608-9f44-6d1a64ae492f)

  Cerrar el Programa.



