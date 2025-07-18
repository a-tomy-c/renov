import tkinter as tk
from tkinter import ttk
from pathlib import Path
import os, yaml, platform
from typing import Generator, Iterator


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
    
def reload_path_yaml():
    try:
        fun = Funciones()
        path = fun.get_dirpath(fun.get('path yaml'))
        var_path.set(path)
    except Exception as err:
        tex.insert(tk.END, str(err))
    tex.see(tk.END)

def write_tags():
    try:
        fun = Funciones()
        path = var_path.get()
        if path:
            mic = MiCarpeta(path=path)
            names = mic.nombresDe(files=mic._content())
            tex.insert(tk.END, f'{len(names)} tags.\n')
            texto = '\n'.join(names)

            filepath = fun.get("name txt")
            with open(filepath, 'w') as file:
                file.write(texto)
            tex.insert(tk.END, f'el archivo {filepath} se ha creado.\n')

            tex.insert(tk.END, '\n')
            tex.insert(tk.END, ', '.join(names))
            tex.insert(tk.END, '\n')
    except Exception as err:
        tex.insert(tk.END, str(err))
    tex.see(tk.END)


vn = tk.Tk()
fm = tk.Frame(vn)
fm.grid(row=0, column=0, sticky='we')
bt_gen = ttk.Button(fm, text='GEN', width=5, padding=0, command=write_tags)
var_path = tk.StringVar()
en_path = ttk.Entry(fm, textvariable=var_path)
bt_reload = ttk.Button(fm, text='R', width=3, padding=0, command=reload_path_yaml)

bt_gen.grid(row=0, column=0)
en_path.grid(row=0, column=1, sticky='we', padx=2)
bt_reload.grid(row=0, column=2)
vn.rowconfigure(1, weight=1)
vn.columnconfigure(0, weight=1)
fm.grid(row=0, column=0, sticky='we')
fm.rowconfigure(0, weight=1)
fm.columnconfigure(1, weight=1)

tex = tk.Text(
    vn, relief='flat', selectbackground='lightgreen',
    highlightthickness=0, border=0, bd=0
)
tex.grid(row=1, column=0, sticky='wens')

s = ttk.Style()
s.theme_use('default')
bgp = 'black'
bga = 'gray20'
fgp = 'yellow'
fga = 'orange'
fg = 'white'
bg = 'gray30'
s.configure(
    'TButton',
    background=bg,
    foreground=fg,
    relief='flat'
)
nom_s = 'mib'
s.map(
    f"{nom_s}.TButton",
    background=[
        ('pressed', bgp), ('active',bga),
    ],
    foreground=[
        ('pressed', fgp), ('active',fga),
        ('disabled', '#59564D'), ('!disabled', fg)
    ],
)
bt_gen.config(style=f'{nom_s}.TButton')
bt_reload.config(style=f'{nom_s}.TButton')
fm.config(bg=bga)
tex.config(
    background=bga, foreground=fg,
    highlightcolor=fg, insertbackground=fga, padx=4
)
s.configure(
    'k.TEntry',
    fieldbackground=bg,
    foreground=fg,
    insertcolor=fg,
    insertwidth=2,
    bordercolor=bg,
    borderwidth=0,
    relief='flat',
    selectborderwidth=0,
    selectforeground=bg,
    selectbackground=fg,
    bd=0
)
s.map(
    "k.TEntry",
    fieldbackground=[('focus', bga), ('!focus', bg)],
    foreground=[('focus', fga), ('!focus', fg)]
)
en_path.config(style='k.TEntry')


vn.title("Genera Tags")
vn.geometry("600x200")
vn.mainloop()