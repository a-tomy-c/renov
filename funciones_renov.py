from funciones import MiCarpeta, FileConfig, Info
import platform
import logging



class FuncionesRenov:
    def __init__(self):
        file_config = FileConfig()
        self.cf = file_config.read_yaml(filepath='configs_renov.yaml')
        self.tags = []

    def get(self, key:str) -> str:
        return self.cf.get(key)

    def get_tags(self) -> list[str]:
        system = platform.system()
        if system == "Windows":
            path = self.get('path tags win')
        elif system == "Linux":
            path = self.get('path tags lnx')
        micarpeta = MiCarpeta(path=path)
        images = micarpeta.imagenes(ext=self.get('format images'))
        tags = micarpeta.nombresDe(images)
        return tags

    def get_template(self) -> str:
        return self.get('template')
    
    def get_sep(self) -> str:
        return self.get('sep tags')
    
    def select_tag(self, tag:str):
        sep = self.get_sep()
        if not tag in self.tags:
            self.tags.append(tag)
        return sep.join(self.tags)
            



