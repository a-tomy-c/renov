import yaml


def escribe():
    configs = {
        'nombre':'Juan',
        'Apellidos':['Perez', 'Calle'],
        'edad':20
    }

    with open('salida.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(
            configs, file,
            default_flow_style=False,
            allow_unicode=True
        )

def lectura(name:str) -> dict:
    with open(name, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


res = lectura('salida.yaml')
print(type(res))
from pprint import pprint
pprint(res)
