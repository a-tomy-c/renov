import os
from pathlib import Path
import platform
import sys
import yaml
from typing import Generator, Iterator
from PySide6.QtWidgets import (
    QWidget, QPushButton, QLineEdit, QTextEdit,
    QApplication, QVBoxLayout, QHBoxLayout
)

class MiCarpeta:
    def __init__(self, path=str):
        self.path = Path(path)

    def _content(self) -> list[Path]:
        with os.scandir(self.path.as_posix()) as fs:
            return [Path(r) for r in fs]
        
    def archivos(self) -> Generator[str]:
        return (f.as_posix() for f in self._content() if f.is_file())
    
    def carpetas(self) -> Generator[str]:
        return (f.as_posix() for f in self._content() if f.is_dir())
    
    def nombresDe(self, files:Iterator, stem:bool=True) -> Generator[str]:
        if isinstance(files, (Iterator, list, tuple)):
            return [Path(f).stem if stem else Path(f).name for f in files]
        
    def porExtension(self, ext:Iterator=['.txt']) -> Generator[str]:
        return [Path(f).as_posix() for f in self.archivos() if Path(f).suffix in ext]
    
    def imagenes(self, ext=['.jpg', '.png', '.gif']) -> Generator[str]:
        return self.porExtension(ext=ext)


class Funciones:
    def read_yaml(self, filepath:str) -> dict:
        with open(filepath, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
        
    def get_dirpath(self, path_yaml:str) -> str:
        yam = self.read_yaml(path_yaml)
        system = platform.system()
        path = ""
        if system == 'Windows':
            path = yam.get('path tags win')
        elif system == 'Linux':
            path = yam.get('path tags lnx')
        return path
    
    def get(self, key:str, defo="") -> str|int:
        d = self.read_yaml('gen_tags.yaml')
        return d.get(key, defo)
        

class GenTags(QWidget):
    def __init__(self):
        super().__init__()
        self.__config_gentags()
    
    def __config_gentags(self):
        fun = Funciones()
        self.resize(fun.get('width'), fun.get('height'))
        self.setContentsMargins(2,2,2,2)
        self.bt_gen = QPushButton(text='GEN')
        self.bt_reload = QPushButton(text='R')
        self.le_path = QLineEdit()
        self.te = QTextEdit()
        hly = QHBoxLayout()
        hly.addWidget(self.bt_gen)
        hly.addWidget(self.le_path)
        hly.addWidget(self.bt_reload)
        hly.setContentsMargins(0,0,0,0)
        vly = QVBoxLayout(self)
        vly.addLayout(hly)
        vly.addWidget(self.te)
        vly.setContentsMargins(0,0,0,0)
        hly.setSpacing(2)

        self.bt_gen.setFixedWidth(40)
        self.bt_reload.setFixedWidth(30)

        self.bt_reload.clicked.connect(self.reload_path_yaml)
        self.bt_gen.clicked.connect(self.write_tags)

    def get_path(self) -> str:
        return self.le_path.text()
    
    def reload_path_yaml(self):
        try:
            fun = Funciones()
            path = fun.get_dirpath(fun.get('path yaml'))
            self.le_path.setText(path)
        except Exception as err:
            self.te.append(f'{err}.')
        

    def write_tags(self):
        try:
            fun = Funciones()
            path = self.le_path.text()
            if path:
                mic = MiCarpeta(path=path)
                names = mic.nombresDe(files=mic._content())

                self.te.append(f'{len(names)} tags.')
                texto = '\n'.join(names)

                filepath = fun.get("name txt")
                with open(filepath, 'w') as file:
                    file.write(texto)
                self.te.append(f'el archivo {filepath} se ha creado.')

                self.te.append('')
                self.te.append(', '.join(names))
        except Exception as err:
            self.te.append(f'{err}.')
        

    def read_tags(self) -> list:
        fun = Funciones()
        path = fun.get('name txt')
        tags = None
        if path:
            with open(path, 'r') as file:
                lines = file.readlines()
                tags = [line.strip('\n') for line in lines]
        return tags


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = GenTags()
    w.show()
    sys.exit(app.exec())