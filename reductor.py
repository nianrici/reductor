import os
import subprocess

def vidio(input_file, output_file):
    # Reducimos el tamaño de los archivos de video usando FFMPEG y el códec de video x265
    # Para poder ejecutarlo hay que tener instalado el programa FFMPEG:
    # https://ffmpeg.org/download.html
    try:
        c = 'ffmpeg -i "' + input_file + '" -vcodec libx265 -an -preset ultrafast "' + output_file + '"'
        subprocess.run(c)
    except:
        print('Sucedió un error')

def reducto(self):
    # ¡Mira mamá, como Harry Potter!
    # Para poder ejecutarlo, hay que tener instalada la suite "Imagemagick":
    # https://imagemagick.org/script/download.php
    try:
        f = 'mogrify -format jpg -resize 2048x2048 "' + self + '"'
        subprocess.run(f)
        print("El archivo " + self + " ha sido reducido!")
    except:
        print('Sucedió un error')



path = os.getcwd()

for subdir, dirs, files in os.walk(path):
    for file in files:
        fpath = subdir + os.sep + file
        if fpath.endswith(".bmp"):
             reducto(fpath)
             os.remove(fpath)
        elif fpath.endswith(".ts") or fpath.endswith(".mov") or fpath.endswith(".mp4"):
            vidio(fpath, (fpath + ".redux.mp4"))
            os.remove(fpath)
