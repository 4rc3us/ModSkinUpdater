from bs4 import BeautifulSoup
import requests
import os
import wget
import zipfile
import subprocess, sys


def unZip():
    # Funcion para descomprimir el archivo descargado
    pathContenedor = os.popen('echo "%USERPROFILE%\ModSkin"').read()
    fileName = os.listdir(pathContenedor[:-1])
    pathDestino = os.popen('echo "%USERPROFILE%\ModSkin"').read()
    pathWfile = pathContenedor[0:-1] + "\\" + fileName[0]

    with zipfile.ZipFile(pathWfile, "r") as zip_ref:
        zip_ref.extractall(pathDestino[0:-1])

    print("\n\nArchivo descomprimido")
    # Finde la funcion


def getUrl():
    # Funcion para obtener la url del zip
    r = requests.get("https://lolskin.pro/")
    soup = BeautifulSoup(r.content, "lxml")

    for link in soup.find_all("a"):
        if ".zip" in link.get("href"):
            return link.get("href")
    # Finde la funcion


def createShortcut():
    p = subprocess.Popen(["powershell.exe", ".\\CreateShortCut.ps1"], stdout=sys.stdout)
    p.communicate()


if os.system('mkdir "%USERPROFILE%\ModSkin"') == 0:
    p = subprocess.Popen(
        ["powershell.exe", ".\\GetHomeFolder.ps1"], stdout=subprocess.PIPE
    )
    output = p.communicate()[0].decode("utf-8")[0:-2]
    url = getUrl()
    print("\nDescargando archivo", url + "\n")
    wget.download(url, output)
    unZip()
    createShortcut()

else:
    os.system('rmdir "%USERPROFILE%\ModSkin" /S /Q')
    p = subprocess.Popen(
        ["powershell.exe", ".\\GetHomeFolder.ps1"], stdout=subprocess.PIPE
    )
    output = p.communicate()[0].decode("utf-8")[0:-2]

    print("\nEliminando...")

    if os.system('mkdir "%USERPROFILE%\ModSkin"') == 0:
        url = getUrl()
        print("\nDescargando archivo", url, "\n")
        wget.download(url, output)
        unZip()
        createShortcut()
