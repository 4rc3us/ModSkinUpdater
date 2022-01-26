from bs4 import BeautifulSoup
import requests
import wget
import os
import subprocess, sys


def getUrl():
    r = requests.get("https://modskin.org/")
    soup = BeautifulSoup(r.content, "lxml")

    for link in soup.find_all("a"):
        if ".zip" in link.get("href"):
            return link.get("href")


p = subprocess.Popen(["powershell.exe", ".\\GetHomeFolder.ps1"], stdout=subprocess.PIPE)
output = p.communicate()[0].decode("utf-8")[0:-2]

url = getUrl()

# print("\nDescargando archivo", url + "\n")
print(url)
print(output)
wget.download(url)
