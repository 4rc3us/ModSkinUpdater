from bs4 import BeautifulSoup
import requests
import os
import wget

r = requests.get("http://leagueskin.net/p/download-mod-skin-2020-chn")
soup = BeautifulSoup(r.content, "lxml")
url = ""

for link in soup.find_all("a"):
    if ".zip" in link.get("href"):
        url = link.get("href")
        print(url)

if os.system("mkdir %USERPROFILE%\ModSkin") == 0:
    stream = os.popen("echo %USERPROFILE%\ModSkin")
    output = stream.read()

    print("El directorio {} no existe. Creando...".format(output[0:-1]))

    wget.download(url, output[0:-1])

else:
    os.system("rmdir %USERPROFILE%\ModSkin /S /Q")
    stream = os.popen("echo %USERPROFILE%\ModSkin")
    output = stream.read()
    print("Eliminando...")
    if os.system("mkdir %USERPROFILE%\ModSkin") == 0:
        print("Descargando archivo")
        wget.download(url, output[0:-1])
