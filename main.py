from bs4 import BeautifulSoup
import requests
import os
import wget
import zipfile
import subprocess, sys

p = subprocess.Popen(
    ["powershell.exe", ".\\Scripts\\GetHomeFolder.ps1"], stdout=subprocess.PIPE
)

HOME = p.communicate()[0].decode("utf-8")[0:-2]


def unZip():
    fileName = os.listdir(HOME)
    pathWfile = HOME + "\\" + fileName[0]

    with zipfile.ZipFile(pathWfile, "r") as zip_ref:
        zip_ref.extractall(HOME)

    print("\n\nunzipped file")


def getUrl():
    # Funcion para obtener la url del zip
    r = requests.get("http://leagueskin.net/p/download-mod-skin-2020-chn")
    soup = BeautifulSoup(r.content, "lxml")

    return soup.find("a", {"id": "link_download3"}).get("href")


def createShortcut():
    p = subprocess.Popen(["powershell.exe", ".\\Scripts\\CreateShortCut.ps1"], stdout=sys.stdout)
    p.communicate()


if os.system('mkdir "%USERPROFILE%\ModSkin"') == 0:
    url = getUrl()
    print("\nDescargando archivo", url + "\n")
    wget.download(url, HOME)
    unZip()
    createShortcut()

else:
    os.system('rmdir "%USERPROFILE%\ModSkin" /S /Q')

    print("\nEliminando...")

    if os.system('mkdir "%USERPROFILE%\ModSkin"') == 0:
        url = getUrl()
        print("\nDescargando archivo", url, "\n")
        wget.download(url, HOME)
        unZip()
        createShortcut()
