from bs4 import BeautifulSoup
import requests
import os
import wget
import zipfile


def unZip():
    # Funcion para descomprimir el archivo descargado
    pathContenedor = os.popen("echo %USERPROFILE%\ModSkin").read()
    fileName = os.listdir(pathContenedor[:-1])
    pathDestino = os.popen("echo %USERPROFILE%\ModSkin").read()
    pathWfile = pathContenedor[0:-1] + "\\" + fileName[0]

    with zipfile.ZipFile(pathWfile, "r") as zip_ref:
        zip_ref.extractall(pathDestino[0:-1])

    print("\n\nArchivo descomprimido")
    # Finde la funcion


def getUrl():
    # Funcion para obtener la url del zip
    r = requests.get("http://leagueskin.net/p/download-mod-skin-2020-chn")
    soup = BeautifulSoup(r.content, "lxml")
    url = ""

    for link in soup.find_all("a"):
        if ".zip" in link.get("href"):
            print(url)
            return link.get("href")
    # Finde la funcion


if os.system("mkdir %USERPROFILE%\ModSkin") == 0:
    output = os.popen("echo %USERPROFILE%\ModSkin").read()

    wget.download(getUrl(), output[0:-1])
    unZip()

else:
    os.system("rmdir %USERPROFILE%\ModSkin /S /Q")
    output = os.popen("echo %USERPROFILE%\ModSkin").read()

    print("Eliminando...")

    if os.system("mkdir %USERPROFILE%\ModSkin") == 0:

        print("Descargando archivo")
        wget.download(getUrl(), output[0:-1])
        unZip()
