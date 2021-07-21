# Mod Skin Updater

**dependencias:  **
bs4  
requests  
lxml  
wget

comandos:  
-py --version  
-Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))  
-choco install python  
-py -m pip --version  
-py -m ensurepip --default-pip  
-py -m pip install --upgrade pip setuptools wheel  
-pip install bs4  
-pip install requests  
-pip install lxml  
-pip install wget
