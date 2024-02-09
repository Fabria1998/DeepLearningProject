#Programa Principal
#Interfaz gráfica de nuestro proyecto
#Importamos las Librerias
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess

#Creamos la clase InterfazApp
class InterfazApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz")

        # Configuración de colores
        self.bg_color = "azure"  # Cambia este color según tus preferencias
        self.button_color = "azure"  # Cambia este color según tus preferencias

        self.master.configure(bg=self.bg_color)

        # Cargar y mostrar la imagen de fondo
        image_path = "background_image.png"  # Ajusta el nombre de la imagen según sea necesario
        if os.path.exists(image_path):
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            background_label = tk.Label(self.master, image=photo)
            background_label.image = photo
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Botones con colores personalizados
        self.camera_button = tk.Button(
            self.master, text="Iniciar Cámara", command=self.start_camera, bg=self.button_color
        )
        self.camera_button.place(x=150, y=150)

        self.video_button = tk.Button(
            self.master, text="Video", command=self.load_video, bg=self.button_color
        )
        self.video_button.place(x=250, y=150)

        self.instructions_button = tk.Button(
            self.master, text="Instrucciones", command=self.show_instructions, bg=self.button_color
        )
        self.instructions_button.place(x=300, y=150)

        self.info_button = tk.Button(
            self.master, text="Información", command=self.show_info, bg=self.button_color
        )
        self.info_button.place(x=400, y=150)

        self.exit_button = tk.Button(
            self.master, text="Salir", command=self.exit_program, bg=self.button_color
        )
        self.exit_button.place(x=500, y=150)

    #Función para llamar a process_camara.py 
    def start_camera(self):
        subprocess.Popen(["python", "process_camara.py"])

    #Función para llamar a process_videos.py
    def load_video(self):
        subprocess.Popen(["python", "process_videos.py"])

    #Función para mostrar las instrucciones
    def show_instructions(self):
        instructions = """
        Instrucciones de Uso:

        1. Para Iniciar la Cámara:
           - Presiona el botón 'Iniciar Cámara'.
           - Dibuja las áreas de interés haciendo clic en la 
             ventana.
           - Presiona la tecla "n" para dibujar una nueva área.
           - Presiona la tecla "c" para eliminar uno o varios puntos
             del área.
           - Presiona la tecla 'Enter' para finalizar la selección 
             de áreas.
           - Observa el conteo de personas en la ventana 
             emergente.
           - Presiona la tecla "q" para salir de la ventana.

        2. Para Cargar un Video:
           - Presiona el botón 'Video'.
           - Presiona la tecla "n" para dibujar una nueva área.
           - Presiona la tecla "c" para eliminar uno o varios 
             puntos del área.
           - Dibuja las áreas de interés de la misma manera que 
             con la cámara.
           - Presiona la tecla 'Enter' para finalizar la selección
             de áreas.
           - Observa el conteo de personas en la ventana 
             emergente.
           - Presiona la tecla "q" para salir de la ventana.
        """
        messagebox.showinfo("Instrucciones", instructions)

    #Función para mostrar las información
    def show_info(self):
        subprocess.Popen(["python", "process_info.py"])

    #Función para cerrar el programa
    def exit_program(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazApp(root)

 
    # Ajustar el tamaño de la ventana para que se adapte a la imagen
    image_path = "background_image.png"  # Ajusta el nombre de la imagen según sea necesario
    if os.path.exists(image_path):
        image = Image.open(image_path)
        window_width, window_height = image.size
        root.geometry(f"{window_width}x{window_height}")

    root.mainloop()
