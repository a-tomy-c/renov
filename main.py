from PySide6.QtWidgets import QWidget, QApplication, QTreeWidgetItem, QAbstractItemView
from PySide6.QtGui import QIcon, QDragEnterEvent, QDropEvent
from PySide6.QtCore import Qt, QSize
from skin_renov import Ui_Renov
from funciones import MiCarpeta, FileConfig, Info
from funciones_renov import FuncionesRenov
# import platform
# import logging
import os
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
        self.ui.bt_preview.clicked.connect(self.preview_name)
        self.ui.bt_info.clicked.connect(self.show_info)
        self.ui.bt_reload_template.clicked.connect(self.reload_config)
        self.ui.bt_renamer.clicked.connect(self.rename_file)

    def reload_config(self):
        self.PATH_OLD = None
        self.PATH_NEW = None
        self.reload_tags()
        self.reload_template()
        self.ui.bt_renamer.setEnabled(False)

        self.ui.text_edit.clear()
        self.ui.tree.clear()

    def reload_tags(self):
        self.ui.cmb_tags.clear()
        tags = self.fun.get_tags()
        self.ui.cmb_tags.addItems(tags)
        self.msg(text=f'{len(tags)} tags cargados.\n', fg='gray')

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
        scrollbar = self.ui.text_edit.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def dragEnterEvent(self, event:QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event:QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            filepath = urls[0].toLocalFile()
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
        self.ui.tree.setCurrentItem(item_file)
        self.msg(f'{path.parent.as_posix()}\n', fg='gray')
        self.msg('FILE: ')
        self.msg(f'{name_file}\n', fg='white')

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
        # self.ui.tree.itemClicked.connect(self.select_item_tree)
        self.ui.splitter.setSizes([1, 10])
        self.ui.splitter.setStretchFactor(0, 0)
        self.ui.splitter.setStretchFactor(1, 1)
        # self.ui.tree.setFixedHeight(45)
        self.ui.text_edit.setReadOnly(True)
        self.ui.le_tags.setDragEnabled(False)
        self.ui.tree.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

    def select_item_tree(self, item:QTreeWidgetItem, ncol:int):
        data = item.data(0, Qt.UserRole)
        name = item.text(0)
        # print(data)
        # print(name)

    def preview_name(self):
        item = self.ui.tree.currentItem()
        if item:
            filepath = item.data(0, Qt.UserRole)
            file = Path(filepath)
            if file.is_file():
                stem = file.stem
                template = self.ui.le_template.text()
                iv = Info(filepath, template)
                template_info = iv.get_data()

                tgs = self.ui.le_tags.text()
                tags = f' {tgs}' if tgs else ''
                template_info = template_info.replace('$tags$', tags)

                stem_new = f'{stem} {template_info}'
                self.ui.le_newname.setText(stem_new)
                path = file.with_stem(stem_new).as_posix()
                self.ui.bt_renamer.setEnabled(True)

                self.PATH_OLD = filepath
                self.PATH_NEW = path

                self.show_info()
                self.msg('\n')
                self.msg(f'{self.PATH_OLD}\n', fg='gray')
                self.msg(f'{self.PATH_NEW}\n', fg='white')

    def show_info(self):
        try:
            filepath = self._get_path_from_item()
            if filepath:
                iv = Info(filepath, "")
                res = iv.get_info_text()
                self.msg(f'\n')
                for line in res.split('\n'):
                    self.msg(f'{line}\n', fg='azure')
        except Exception as e:
            self.msg(f'{e}')

    def _get_path_from_item(self) -> str|None:
        path = None
        item = self.ui.tree.currentItem()
        if item:
            filepath = item.data(0, Qt.UserRole)
            file = Path(filepath)
            if file.is_file():
                path = filepath
        return path
    
    def rename_file(self):
        old = Path(self.PATH_OLD)
        if old.is_file():
            path_new = Path(self.PATH_NEW)
            stem = path_new.stem
            stem_mod = self.ui.le_newname.text()
            if stem != stem_mod and stem_mod:
                self.PATH_NEW = path_new.with_stem(stem_mod)
                self.msg(f'el "stem" esta modificado\n', fg='orange')
            if Path(self.PATH_NEW).is_file():
                self.msg('el archivo ya existe.\n', fg='orange')
            else:
                os.rename(self.PATH_OLD, self.PATH_NEW)
                self.msg(f'Archivo Renombrado exitosamente', fg='lightgreen')
                self.ui.bt_renamer.setEnabled(False)
        else:
            self.msg('no es un archivo.\n')
            self.msg(f'{self.PATH_OLD}')


if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    vn = Ventana()
    vn.show()
    sys.exit(app.exec())