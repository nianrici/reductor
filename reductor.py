#!/usr/bin/env python3
import shlex
import subprocess
from pathlib import Path


def vidio(input_file, output_file):
    try:
        c = ['ffmpeg', '-i', input_file, '-vcodec', 'libx265', '-an'
             '-preset', 'ultrafast', output_file]
        subprocess.run([shlex.quote(arg) for arg in c])
    except subprocess.CalledProcessError as e:
        print(f'Error al reducir el video {input_file}: {e}')
    except OSError as e:
        print(f'Error al eliminar el archivo {input_file}: {e}')


def reducto(filepath):
    try:
        f = ['mogrify', '-format', 'jpg', '-resize', '2048x2048', filepath]
        subprocess.run([shlex.quote(arg) for arg in f])
        print(f'El archivo {filepath} ha sido reducido!')
    except subprocess.CalledProcessError as e:
        print(f'Error al reducir la imagen {filepath}: {e}')
    except OSError as e:
        print(f'Error al eliminar el archivo {filepath}: {e}')


path = Path.cwd()

for fpath in path.glob('**/*.{bmp,ts,mov,mp4}'):
    if fpath.suffix == '.bmp':
        reducto(str(fpath))
    elif fpath.suffix in ('.ts', '.mov', '.mp4'):
        vidio(str(fpath), str(fpath.with_suffix('.redux.mp4')))
    fpath.unlink()
