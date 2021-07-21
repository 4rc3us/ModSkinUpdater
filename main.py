from bs4 import BeautifulSoup
import requests
import os
import wget
import zipfile
import subprocess, sys


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

    for link in soup.find_all("a"):
        if ".zip" in link.get("href"):
            return link.get("href")
    # Finde la funcion


def createShortcut():
    p = subprocess.Popen(["powershell.exe", ".\\CreateShortCut.ps1"], stdout=sys.stdout)
    p.communicate()


if os.system("mkdir %USERPROFILE%\ModSkin") == 0:
    output = os.popen("echo %USERPROFILE%\ModSkin").read()
    print("\nDescargando archivo", getUrl() + "\n")
    wget.download(getUrl(), output[0:-1])
    unZip()
    createShortcut()

else:
    os.system("rmdir %USERPROFILE%\ModSkin /S /Q")
    output = os.popen("echo %USERPROFILE%\ModSkin").read()

    print("\nEliminando...")

    if os.system("mkdir %USERPROFILE%\ModSkin") == 0:

        print("\nDescargando archivo", getUrl(), "\n")
        wget.download(getUrl(), output[0:-1])
        unZip()
        createShortcut()
