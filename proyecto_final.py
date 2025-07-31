from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit,
    QTextEdit, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
import json
import os
import sys

qss_string = """
    QWidget {
        background-color: #333333; /* Fondo oscuro para toda la ventana */
        color: #F0F0F0; /* Color de texto claro por defecto */
    }

    #myLabel { /* Estilo específico para el QLabel con objectName="myLabel" */
        background-color: #555555;
        color: #ADD8E6; /* Azul claro */
        border: 1px solid #777777;
    }

    QPushButton { /* Estilo para todos los QPushButton */
        background-color: #5cb85c; /* Verde por defecto para los botones */
        color: white;
        padding: 5px;
        border-radius: 5px;
        border: none;
    }

    QPushButton:hover { /* Estilo al pasar el ratón por encima */
        background-color: #4cae4c;
    }

    #blueButton { /* Estilo específico para el botón con objectName="blueButton" */
        background-color: #007bff; /* Azul oscuro */
    }

    #blueButton:hover {
        background-color: #0056b3;
    }
    """

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
        # Julián: Esta función intenta abrir el archivo "notes.json"
        # y cargar el contenido de las notas en el diccionario 'self.notes'

        if os.path.exists("notes.json"):
            try:
                with open("notes.json", "r", encoding="utf-8") as file:
                    self.notes = json.load(file)  # Carga el JSON como diccionario

                # Llena la lista visual con los títulos de las notas
                self.notes_list.clear()
                for title in self.notes:
                    self.notes_list.addItem(title)

                self.show_message("Notas cargadas", "Las notas se cargaron correctamente.")
            except Exception as e:
                self.show_message("Error", f"No se pudieron cargar las notas: {e}")
        else:
            # Si el archivo no existe, crea un diccionario vacío
            self.notes = {}
            self.show_message("Sin notas", "No se encontró un archivo de notas. Se creará uno nuevo al guardar.")

    def save_notes_to_file(self):
        # Julián: Esta función guarda el diccionario 'self.notes' en un archivo JSON
        # para que las notas se mantengan al cerrar el programa

        try:
            with open("notes.json", "w", encoding="utf-8") as file:
                json.dump(self.notes, file, ensure_ascii=False, indent=4)

            self.show_message("Guardado exitoso", "Las notas han sido guardadas correctamente.")
        except Exception as e:
            self.show_message("Error", f"No se pudieron guardar las notas: {e}")

     def add_image(self):
        # Cristian: Esta función permite al usuario seleccionar una imagen desde su computador
        # y luego la muestra en la interfaz.

        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            # Carga la imagen con PIL y la guarda en self.current_image para futuros cambios
            self.current_image = Image.open(file_name)
            
            # Convierte la imagen a un formato que Qt pueda mostrar
            qt_image = ImageQt.ImageQt(self.current_image)
            pixmap = QPixmap.fromImage(qt_image)

            # Muestra la imagen en el QLabel
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

            # Guarda la ruta por si se necesita
            self.current_image_path = file_name
            self.show_message("Imagen cargada", "La imagen se ha cargado correctamente.")

    def make_bw(self):
        # Cristian: Esta función convierte la imagen actual en blanco y negro.

        if hasattr(self, 'current_image'):
            # Convierte la imagen a blanco y negro (modo 'L') y luego de nuevo a RGB para mostrarla
            bw_image = self.current_image.convert("L").convert("RGB")
            self.current_image = bw_image

            # Muestra la imagen procesada en el QLabel
            qt_image = ImageQt.ImageQt(bw_image)
            pixmap = QPixmap.fromImage(qt_image)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

            self.show_message("Éxito", "Imagen convertida a blanco y negro.")
        else:
            self.show_message("Error", "Primero debes cargar una imagen.")

    def make_mirror(self):
        # Cristian: Esta función voltea la imagen de manera horizontal (espejo).

        if hasattr(self, 'current_image'):
            mirrored_image = ImageOps.mirror(self.current_image)
            self.current_image = mirrored_image

            # Actualiza el QLabel con la imagen reflejada
            qt_image = ImageQt.ImageQt(mirrored_image)
            pixmap = QPixmap.fromImage(qt_image)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

            self.show_message("Éxito", "Imagen reflejada horizontalmente.")
        else:
            self.show_message("Error", "Primero debes cargar una imagen.")

    def show_message(self, title, message):
        # Esta función muestra un cuadro de diálogo informativo al usuario
        QMessageBox.information(self, title, message)

def custom_message(self, title, message):
        Custom = QMessageBox(self)
        Custom.setWindowTitle(title)
        Custom.setText(message)
        Custom.setIcon(QMessageBox.Question)

        btn_fusion = QPushButton('Fusion')
        btn_Windows = QPushButton('Windows')
        btn_WV = QPushButton('Windows Vista')

        Custom.addButton(btn_fusion, QMessageBox.NoRole)
        Custom.addButton(btn_Windows, QMessageBox.NoRole)
        Custom.addButton(btn_WV, QMessageBox.NoRole)

        Custom.exec()

        clicked_button = Custom.clickedButton()

        if clicked_button == btn_fusion:
            app.setStyle('Fusion')
        elif clicked_button == btn_Windows:
            app.setStyle('Windows')
        elif clicked_button == btn_WV:
            app.setStyle('WindosVista')

# ---------- Inicio del programa ----------
if _name_ == "_main_":
    app = QApplication(sys.argv) # Crea una aplicación
    Apparance = QMessageBox.information(None,'Apariencia','¿Quieres aplicar la apariencia oscura?',QMessageBox.Yes | QMessageBox.No )
    if Apparance == QMessageBox.Yes:
        window = NotesApp()  # Crea una ventana con nuestra app
        app.setStyleSheet(qss_string)
        window.show()  # Muestra la ventana
        sys.exit(app.exec_())  # Ejecuta la aplicación hasta que se cierre
    else:
        window = NotesApp()  # Crea una ventana con nuestra app
        NotesApp.custom_message(None, 'Estilo', '¿Qué estilo quieres?')
        window.show()  # Muestra la ventana
        sys.exit(app.exec_())  # Ejecuta la aplicación hasta que se cierre
