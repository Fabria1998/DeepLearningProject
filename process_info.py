# info.py

import tkinter as tk
from PIL import Image, ImageTk  # Asegúrate de tener instalada la librería Pillow

class InfoWindow:
    def __init__(self):
        self.info_window = tk.Tk()
        self.info_window.title("Información del Programa")

        # Configuración de colores
        bg_color = "gainsboro"  # Cambia este color según tus preferencias
        button_color = "gainsboro"  # Cambia este color según tus preferencias

        self.info_window.configure(bg=bg_color)

        # Agregar etiquetas con la información
        info_text = """
        Información del Programa:

        - YOLO (You Only Look Once): Un popular modelo de detección de objetos y 
          segmentación de imágenes, fue desarrollado por Joseph Redmon y Ali Farhadi
          en la Universidad de Washington. Lanzado en 2015, YOLO ganó popularidad 
          rápidamente por su gran velocidad y precisión.

        - YOLOv8 es la última versión de YOLO de Ultralytics. Como modelo de vanguardia
          y de última generación (SOTA), YOLOv8 se basa en el éxito de las versiones
          anteriores, introduciendo nuevas funciones y mejoras para aumentar el 
          rendimiento, la flexibilidad y la eficacia. YOLOv8 admite una gama completa 
          de tareas de IA de visión, como la detección, la segmentación, la estimación 
          de la pose, el seguimiento y la clasificación. Esta versatilidad permite a 
          los usuarios aprovechar las capacidades de YOLOv8 en diversas aplicaciones y dominios.

        - Ultralytics: Un conjunto de herramientas para la visión por 
          computadora, incluido un módulo YOLO fácil de usar.

        - Tkinter: Una biblioteca gráfica para crear interfaces de usuario 
          en Python.

        Desarrollado por [Fabricio Aldaz].
        """

        info_label = tk.Label(self.info_window, text=info_text, bg=bg_color, justify="left")
        info_label.pack(padx=20, pady=20)
        
        # Agregar imágenes
        img_ultralytics = Image.open("ultralytics_image.png")  # Reemplaza "ultralytics_image.png" con tu ruta de imagen
        img_ultralytics = ImageTk.PhotoImage(img_ultralytics)
        label_ultralytics = tk.Label(self.info_window, image=img_ultralytics, bg=bg_color)
        label_ultralytics.image = img_ultralytics
        label_ultralytics.pack()

        # Botón para cerrar la ventana de información
        close_button = tk.Button(self.info_window, text="Cerrar", command=self.close_window, bg=button_color)
        close_button.pack(pady=10)

    def close_window(self):
        self.info_window.destroy()

# Si el script se ejecuta directamente, crea una instancia de InfoWindow
if __name__ == "__main__":
    info_window = InfoWindow()
    info_window.info_window.mainloop()
