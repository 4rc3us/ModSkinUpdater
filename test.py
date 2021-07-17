import subprocess, sys

p = subprocess.Popen(["powershell.exe", ".\\CreateShortCut.ps1"], stdout=sys.stdout)

p.communicate()
