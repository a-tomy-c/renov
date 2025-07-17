from PySide6.QtWidgets import QWidget, QApplication, QTreeWidgetItem
from PySide6.QtGui import QIcon, QDragEnterEvent, QDropEvent
from PySide6.QtCore import Qt, QSize
from skin_renov import Ui_Renov
from funciones import MiCarpeta, FileConfig, Info
from funciones_renov import FuncionesRenov
import platform
import logging
from pathlib import Path


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Renov()
        self.ui.setupUi(self)
        self._config_Ventana()

    def _config_Ventana(self):
        self._config_tree()
        self.setAcceptDrops(True)
        self.fun = FuncionesRenov()
        self.reload_config()
        self.ui.cmb_tags.textActivated.connect(self.select_tag)
        self.ui.bt_reload_tags.clicked.connect(self.reload_tags)

    def reload_config(self):
        self.reload_tags()
        self.reload_template()

    def reload_tags(self):
        self.ui.cmb_tags.clear()
        tags = self.fun.get_tags()
        self.ui.cmb_tags.addItems(tags)
        self.msg(text=f'{len(tags)} tags cargados.\n')

    def reload_template(self):
        self.ui.le_template.clear()
        self.ui.le_template.setText(self.fun.get_template())

    def select_tag(self, tag):
        self.ui.le_tags.clear()
        self.ui.le_tags.setText(self.fun.select_tag(tag))

    def msg(self, text:str, fg:str='skyblue'):
        br = '<br>' if text.endswith('\n') else ''
        self.ui.text_edit.insertHtml(
            f'<span style=color:{fg};>{text}{br}</span>'
        )

    def dragEnterEvent(self, event:QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event:QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            filepath = urls[0].toLocalFile()
            print(filepath)
            self.setItemDrop(filepath)
        event.acceptProposedAction()

    def setItemDrop(self, filepath:str):
        path = Path(filepath)
        name_dir = path.parent.name
        name_file = path.name
        ico_dir =   QIcon('otros/folder.png')
        ico_file = QIcon('otros/video.png')
        self.ui.tree.clear()

        # if name_dir in self.dirs:
        #     item_dir = self.dirs[name_dir]
        # else:
        item_dir = QTreeWidgetItem()
        item_dir.setText(0, name_dir)
        item_dir.setIcon(0, ico_dir)
        item_dir.setData(0, Qt.UserRole, name_dir)
        
        self.ui.tree.addTopLevelItem(item_dir)
        self.dirs[name_dir] = item_dir

        item_file = QTreeWidgetItem()
        item_file.setText(0, name_file)
        item_file.setIcon(0, ico_file)
        item_file.setData(0, Qt.UserRole, path.as_posix())

        item_dir.addChild(item_file)
        item_dir.setExpanded(True)

    def _config_tree(self):
        stylesheet = """
        QTreeWidget::item:selected {
            background-color: black;
            color: white;
        }

        QTreeWidget::item:selected:active {
            background-color: black;
            color: white;
        }

        QTreeWidget::item:selected:!active {
            background-color: black;
            color: white;
        }

        QTreeWidget::item:hover {
            background-color: #444444;
            color: white;
        }
        """
        self.ui.tree.setStyleSheet(stylesheet)
        self.dirs = {}
        self.ui.tree.itemClicked.connect(self.select_item_tree)
        self.ui.splitter.setSizes([1, 10])
        self.ui.splitter.setStretchFactor(0, 0)
        self.ui.splitter.setStretchFactor(1, 1)
        # self.ui.tree.setFixedHeight(45)

    def select_item_tree(self, item:QTreeWidgetItem, ncol:int):
        data = item.data(0, Qt.UserRole)
        name = item.text(0)

        print(data)
        print(name)



if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    vn = Ventana()
    vn.show()
    sys.exit(app.exec())