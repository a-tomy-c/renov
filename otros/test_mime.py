from pprint import pprint
import platform
from mi_mediainfo import InfoVideo



if __name__=="__main__":
    system = platform.system()
    if system == 'Windows':
        v1 = ''
    elif system == 'Linux':
        v1 = '/run/media/tomy/sis/beta/renom/celmont.mp4'


    iv = InfoVideo(file=v1)
    print(iv.get_info_text())