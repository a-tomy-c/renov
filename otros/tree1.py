import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                               QWidget, QTreeView, QLabel, QHBoxLayout)
from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QStandardItemModel, QStandardItem, QIcon

class VentanaTreeViewDragDrop(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
        self.configurar_modelo()
        
    def inicializar_ui(self):
        self.setWindowTitle("TreeView con Drag and Drop - PySide6")
        self.setGeometry(100, 100, 600, 400)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Etiqueta de instrucciones
        instrucciones = QLabel("Arrastra archivos de video a la ventana")
        instrucciones.setStyleSheet("""
            QLabel {
                background-color: #e3f2fd;
                border: 1px solid #2196f3;
                border-radius: 5px;
                padding: 10px;
                font-size: 12px;
                color: #1976d2;
            }
        """)
        layout.addWidget(instrucciones)
        
        # TreeView
        self.tree_view = QTreeView()
        stylesheet = """
        QTreeView::item:selected {
            background-color: black;
            color: white;
        }

        QTreeView::item:selected:active {
            background-color: black;
            color: white;
        }

        QTreeView::item:selected:!active {
            background-color: black;
            color: white;
        }

        QTreeView::item:hover {
            color: yellow;
        }
        """       

        self.tree_view.setStyleSheet(stylesheet)
        


        self.tree_view.setHeaderHidden(True)
        self.tree_view.setRootIsDecorated(True)
        self.tree_view.setAlternatingRowColors(True)
        layout.addWidget(self.tree_view)
        
        # Layout inferior con información
        info_layout = QHBoxLayout()
        
        self.label_info = QLabel("Archivos aparecerán aquí")
        self.label_info.setStyleSheet("""
            QLabel {
                background-color: #f5f5f5;
                padding: 5px;
                border-radius: 3px;
                font-size: 11px;
                color: #666;
            }
        """)
        info_layout.addWidget(self.label_info)
        
        info_layout.addStretch()
        layout.addLayout(info_layout)
        
        # Habilitar drag and drop
        self.setAcceptDrops(True)
        
    def configurar_modelo(self):
        """Configura el modelo del TreeView"""
        self.model = QStandardItemModel()
        self.tree_view.setModel(self.model)
        
        # Diccionario para mantener referencia a las carpetas
        self.carpetas = {}
        
    def crear_icono_folder(self):
        """Crea un icono de folder básico si no existe el archivo"""
        try:
            # Intentar cargar el icono desde archivo
            icon = QIcon("otros/folder.png")
            if not icon.isNull():
                return icon
        except:
            pass
            
        # Si no se puede cargar, crear un icono básico usando texto
        from PySide6.QtGui import QPixmap, QPainter, QColor, QFont
        
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor(255, 206, 84))  # Color amarillo para folder
        
        painter = QPainter(pixmap)
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont("Arial", 8))
        painter.drawText(0, 0, 16, 16, Qt.AlignCenter, "📁")
        painter.end()
        
        return QIcon(pixmap)
        
    def crear_icono_video(self):
        """Crea un icono de video básico si no existe el archivo"""
        try:
            # Intentar cargar el icono desde archivo
            icon = QIcon("otros/video.png")
            if not icon.isNull():
                return icon
        except:
            pass
            
        # Si no se puede cargar, crear un icono básico usando texto
        from PySide6.QtGui import QPixmap, QPainter, QColor, QFont
        
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor(255, 99, 71))  # Color rojo para video
        
        painter = QPainter(pixmap)
        painter.setPen(QColor(255, 255, 255))
        painter.setFont(QFont("Arial", 8))
        painter.drawText(0, 0, 16, 16, Qt.AlignCenter, "🎬")
        painter.end()
        
        return QIcon(pixmap)
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Valida si se pueden aceptar los archivos arrastrados"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.label_info.setText("Suelta los archivos aquí...")
            self.label_info.setStyleSheet("""
                QLabel {
                    background-color: #e8f5e8;
                    border: 1px solid #4caf50;
                    padding: 5px;
                    border-radius: 3px;
                    font-size: 11px;
                    color: #2e7d32;
                }
            """)
        else:
            event.ignore()
            
    def dragLeaveEvent(self, event):
        """Restaura la apariencia cuando se sale sin soltar"""
        self.label_info.setText("Archivos aparecerán aquí")
        self.label_info.setStyleSheet("""
            QLabel {
                background-color: #f5f5f5;
                padding: 5px;
                border-radius: 3px;
                font-size: 11px;
                color: #666;
            }
        """)
        
    def dropEvent(self, event: QDropEvent):
        """Procesa los archivos soltados"""
        urls = event.mimeData().urls()
        archivos_procesados = 0
        
        for url in urls:
            ruta_archivo = url.toLocalFile()
            
            if os.path.isfile(ruta_archivo):
                self.agregar_archivo_al_tree(ruta_archivo)
                archivos_procesados += 1
                
        # Actualizar información
        self.label_info.setText(f"Procesados: {archivos_procesados} archivo(s)")
        self.label_info.setStyleSheet("""
            QLabel {
                background-color: #e8f5e8;
                border: 1px solid #4caf50;
                padding: 5px;
                border-radius: 3px;
                font-size: 11px;
                color: #2e7d32;
            }
        """)
        
        event.acceptProposedAction()
        
    def agregar_archivo_al_tree(self, ruta_archivo):
        """Agrega un archivo al TreeView"""
        # Obtener información del archivo
        directorio_padre = os.path.dirname(ruta_archivo)
        nombre_carpeta = os.path.basename(directorio_padre)
        nombre_archivo = os.path.basename(ruta_archivo)
        
        # Crear iconos
        icono_folder = self.crear_icono_folder()
        icono_video = self.crear_icono_video()
        
        # Verificar si ya existe el item de la carpeta
        item_carpeta = None
        
        if nombre_carpeta in self.carpetas:
            item_carpeta = self.carpetas[nombre_carpeta]
        else:
            # Crear nuevo item de carpeta
            item_carpeta = QStandardItem(icono_folder, nombre_carpeta)
            item_carpeta.setData(directorio_padre, Qt.UserRole)  # Guardar ruta completa
            item_carpeta.setToolTip(f"Carpeta: {directorio_padre}")
            
            # Agregar al modelo
            self.model.appendRow(item_carpeta)
            self.carpetas[nombre_carpeta] = item_carpeta
            
        # Crear item del archivo
        item_archivo = QStandardItem(icono_video, nombre_archivo)
        item_archivo.setData(ruta_archivo, Qt.UserRole)  # Guardar ruta completa
        item_archivo.setToolTip(f"Archivo: {ruta_archivo}")
        
        # Verificar si el archivo ya existe en esta carpeta
        archivo_existe = False
        for i in range(item_carpeta.rowCount()):
            child = item_carpeta.child(i)
            if child.text() == nombre_archivo:
                archivo_existe = True
                break
                
        if not archivo_existe:
            # Agregar el archivo como hijo de la carpeta
            item_carpeta.appendRow(item_archivo)
            
        # Expandir la carpeta para mostrar el archivo
        index_carpeta = self.model.indexFromItem(item_carpeta)
        self.tree_view.expand(index_carpeta)
        
        # Imprimir información en consola
        print(f"Archivo agregado:")
        print(f"  Carpeta: {nombre_carpeta}")
        print(f"  Archivo: {nombre_archivo}")
        print(f"  Ruta completa: {ruta_archivo}")
        print("-" * 50)
        
    def obtener_ruta_seleccionada(self):
        """Obtiene la ruta del elemento seleccionado"""
        indexes = self.tree_view.selectedIndexes()
        if indexes:
            index = indexes[0]
            item = self.model.itemFromIndex(index)
            ruta = item.data(Qt.UserRole)
            return ruta
        return None

# Ejemplo de uso con conexión a selección
class VentanaConSeleccion(VentanaTreeViewDragDrop):
    def __init__(self):
        super().__init__()
        self.conectar_seleccion()
        
    def conectar_seleccion(self):
        """Conecta el evento de selección del TreeView"""
        self.tree_view.clicked.connect(self.item_seleccionado)
        
    def item_seleccionado(self, index):
        """Se ejecuta cuando se selecciona un item"""
        item = self.model.itemFromIndex(index)
        ruta = item.data(Qt.UserRole)
        nombre = item.text()
        
        if item.parent() is None:
            # Es una carpeta
            self.label_info.setText(f"Carpeta seleccionada: {nombre}")
            print(f"Carpeta seleccionada: {ruta}")
        else:
            # Es un archivo
            self.label_info.setText(f"Archivo seleccionado: {nombre}")
            print(f"Archivo seleccionado: {ruta}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Usar la versión con selección
    ventana = VentanaConSeleccion()
    ventana.show()
    
    sys.exit(app.exec())