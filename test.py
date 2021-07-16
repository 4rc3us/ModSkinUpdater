import os

pathContenedor = os.popen("echo %USERPROFILE%\ModSkin").read()
fileName = os.listdir(pathContenedor[:-1])
pathDestino = os.popen("echo %USERPROFILE%\ModSkin").read()
pathWfile = pathContenedor[0:-1] + "\\" + fileName[0]

ejecutable = []

for fichero in fileName:
    if os.path.isfile(os.path.join(pathContenedor[:-1], fichero)) and fichero.endswith(
        ".exe"
    ):
        ejecutable.append(fichero)

print(ejecutable[0])
