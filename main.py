from bs4 import BeautifulSoup
import requests
import os
import wget
import zipfile
import subprocess, sys


def unZip():
    p = subprocess.Popen(
        ["powershell.exe", ".\\GetHomeFolder.ps1"], stdout=subprocess.PIPE
    )

    pathContenedor = p.communicate()[0].decode("utf-8")[0:-2]
    fileName = os.listdir(pathContenedor)
    pathWfile = pathContenedor + "\\" + fileName[0]

    with zipfile.ZipFile(pathWfile, "r") as zip_ref:
        zip_ref.extractall(pathContenedor)

    print("\n\nArchivo descomprimido")


def getUrl():
    # Funcion para obtener la url del zip
    r = requests.get("http://leagueskin.net/p/download-mod-skin-2020-chn")
    soup = BeautifulSoup(r.content, "lxml")

    return soup.find("a", {"id": "link_download3"}).get("href")


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
