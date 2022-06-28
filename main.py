from bs4 import BeautifulSoup
import subprocess, sys, os, requests, wget, zipfile

p = subprocess.Popen(
    ["powershell.exe", "Write-Output $HOME\ModSkin\;"], stdout=subprocess.PIPE
)

HOME = p.communicate()[0].decode("utf-8")[0:-2]


def unZip():
    fileName = os.listdir(HOME)
    pathWfile = HOME + "\\" + fileName[0]

    with zipfile.ZipFile(pathWfile, "r") as zip_ref:
        zip_ref.extractall(HOME)

    print("\n\nunzipped file")


def getUrl():
    r = requests.get("http://leagueskin.net/p/download-mod-skin-2020-chn")
    soup = BeautifulSoup(r.content, "lxml")

    return soup.find("a", {"id": "link_download3"}).get("href")


def createShortcut():
    p = subprocess.Popen(["powershell.exe", ".\\Scripts\\CreateShortCut.ps1"], stdout=sys.stdout)
    p.communicate()


if os.system('mkdir "%USERPROFILE%\ModSkin"') == 0:
    url = getUrl()
    print("\nDownloading file", url + "\n")
    wget.download(url, HOME)
    unZip()
    createShortcut()

else:
    os.system('rmdir "%USERPROFILE%\ModSkin" /S /Q')

    print("\nRemoving...")

    if os.system('mkdir "%USERPROFILE%\ModSkin"') == 0:
        url = getUrl()
        print("\nDownloading file", url, "\n")
        wget.download(url, HOME)
        unZip()
        createShortcut()
