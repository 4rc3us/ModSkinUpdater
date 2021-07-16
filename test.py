import os
import wget

if(os.system('mkdir %USERPROFILE%\ModSkin') == 0):
    url = 'https://www.python.org/static/img/python-logo@2x.png'

    stream = os.popen('echo %USERPROFILE%\ModSkin')
    output = stream.read()

    print("El directorio {} no existe. Creando...".format(output[0:-1]))

    wget.download(url, output[0:-1])
    
else:
    stream = os.popen('echo %USERPROFILE%\ModSkin')
    output = stream.read()
    print("El directorio {} ya existe. Eliminando...".format(output[0:-1]))
    os.system('rmdir %USERPROFILE%\ModSkin')

    url = 'https://www.python.org/static/img/python-logo@2x.png'
    
    wget.download(url, output[0:-1])