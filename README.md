# RENOV

renombrar video, agregandole bitrate al nombre


## Notas

- subida inicial
- agregado de skin (QWidget)
- cambie MiMediainfo a Tracks y cree otra Nueva
- ya se le puede colocar plantillas
- modulo funciones ya lee y escribe `yaml` y obtiene valores de string template
    

ejemplo de los datos que obtiene:
```bash
    'aspectratio': '0.562',
    'bitrate': 2180961,
    'bitrateu': '2181kbs',
    'codec': 'avc1',
    'duration': '00:00:37.613',
    'durationms': 37613,
    'format': 'video/H264',
    'height': 1280,
    'time': '37',
    'width': 720
```


## libreria

utitilizadas:

- pymediainfo==7.0.1 (en windows necesita el dll)



