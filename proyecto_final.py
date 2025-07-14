from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit,
    QTextEdit, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
import json
import os
import sys

# ---------- Estructura de datos principal ----------
# Aquí se guardarán las notas en forma de diccionario. Cada entrada debe tener un título, contenido y opcionalmente etiquetas.
# Ejemplo: notes["Mi Nota"] = {"contenido": "texto de la nota", "etiquetas": ["importante"]}
notes = {}  # TODO [Triana/Castaño]: Implementar estructura para almacenar múltiples notas

# ---------- Clase principal de la aplicación ----------
class NotesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mis Notas Pro")  # Título de la ventana
        self.resize(800, 600)  # Tamaño de la ventana

        # ---------- Widgets: Elementos visuales ----------
        self.label = QLabel("Mis notas:")  # Etiqueta de la lista de notas
        self.notes_list = QListWidget()  # Lista donde se mostrarán los títulos de las notas
        self.text = QTextEdit()  # Área de texto para escribir o leer el contenido de la nota

        self.note_name = QLineEdit()  # Caja para escribir el nombre/título de la nota
        self.note_name.setPlaceholderText("Nombre de la nota")

        # Botones para gestionar las notas
        self.btn_new = QPushButton("Nueva nota")
        self.btn_save = QPushButton("Guardar nota")
        self.btn_delete = QPushButton("Eliminar nota")
        self.btn_load = QPushButton("Cargar notas")

        # Botones para la edición de imagen
        self.btn_add_image = QPushButton("Agregar imagen")
        self.btn_bw = QPushButton("Blanco y negro")
        self.btn_mirror = QPushButton("Espejo")
        self.image_label = QLabel("Vista previa de imagen")
        self.image_label.setPixmap(QPixmap())  # Imagen vacía al inicio

        # ---------- Diseño de la interfaz (Juan Felipe puede embellecer o mejorar estructura visual) ----------
        layout_left = QVBoxLayout()  # Layout vertical izquierdo
        layout_left.addWidget(self.label)
        layout_left.addWidget(self.notes_list)
        layout_left.addWidget(self.note_name)
        layout_left.addWidget(self.btn_new)
        layout_left.addWidget(self.btn_save)
        layout_left.addWidget(self.btn_delete)
        layout_left.addWidget(self.btn_load)

        layout_right = QVBoxLayout()  # Layout vertical derecho
        layout_right.addWidget(QLabel("Contenido de la nota:"))
        layout_right.addWidget(self.text)
        layout_right.addWidget(self.btn_add_image)
        layout_right.addWidget(self.btn_bw)
        layout_right.addWidget(self.btn_mirror)
        layout_right.addWidget(self.image_label)

        main_layout = QHBoxLayout()  # Layout horizontal general
        main_layout.addLayout(layout_left, 2)
        main_layout.addLayout(layout_right, 3)

        self.setLayout(main_layout)  # Establecer diseño principal

        # ---------- Conexión de botones con funciones ----------
        self.btn_new.clicked.connect(self.new_note)      # Crear nueva nota
        self.btn_save.clicked.connect(self.save_note)    # Guardar nota
        self.btn_delete.clicked.connect(self.delete_note)  # Eliminar nota
        self.btn_load.clicked.connect(self.load_notes)   # Cargar notas guardadas desde archivo

        self.btn_add_image.clicked.connect(self.add_image)  # Abrir imagen
        self.btn_bw.clicked.connect(self.make_bw)           # Convertir a blanco y negro
        self.btn_mirror.clicked.connect(self.make_mirror)   # Reflejar imagen

    # ---------- FUNCIONES A COMPLETAR por estudiantes ----------

    def new_note(self):
        # Limpia los campos para iniciar una nueva nota
        self.note_name.clear()
        self.text.clear()

    def save_note(self):
        name = self.note_name.text()
        content = self.text.toPlainText()

        # TODO [Triana/Castaño]:
        # Validar que 'name' no esté vacío
        # Guardar la nota en el diccionario global 'notes'
        # Si la nota es nueva, agregarla también a la lista visual self.notes_list
        # Finalmente, llamar a save_notes_to_file() para guardarla en archivo JSON
        pass

    def delete_note(self):
        # TODO [Triana/Castaño]:
        # Obtener el nombre de la nota seleccionada en self.notes_list
        # Eliminarla del diccionario 'notes'
        # Quitarla de la lista visual
        # Guardar cambios en archivo con save_notes_to_file()
        pass

    def load_notes(self):
        # TODO [Julián]:
        # Abrir el archivo "notes.json" si existe
        # Cargar el contenido dentro del diccionario 'notes'
        # Llenar la lista visual self.notes_list con los títulos cargados
        pass

    def save_notes_to_file(self):
        # TODO [Julián]:
        # Guardar el diccionario 'notes' como JSON en un archivo "notes.json"
        pass

    def add_image(self):
        # TODO [Cristian]:
        # Abrir un explorador de archivos para seleccionar una imagen
        # Mostrar la imagen seleccionada en self.image_label usando QPixmap
        pass

    def make_bw(self):
        # TODO [Cristian]:
        # Convertir la imagen actual a blanco y negro utilizando PIL
        # Actualizar la imagen en la interfaz
        pass

    def make_mirror(self):
        # TODO [Cristian]:
        # Reflejar horizontalmente la imagen utilizando PIL
        # Actualizar vista previa
        pass

    def show_message(self, title, message):
        # Muestra un mensaje emergente con un título y contenido
        QMessageBox.information(self, title, message)

# ---------- Inicio del programa ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea una aplicación
    window = NotesApp()  # Crea una ventana con nuestra app
    window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta la aplicación hasta que se cierre
