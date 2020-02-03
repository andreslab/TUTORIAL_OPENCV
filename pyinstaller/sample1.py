print("hola mundo")

#instalar pyinstaller para crear archivos ejecutables
#pip install pyinstaller

#crear archivos ejecutables:

#para ejecutar el programa ir a la carpeta "dist" luego de ejecutar pyinstaller

#pyinstaller name_project.py

#solo crea un archivo con:
#pyinstaller --onefile name_project.py

#los programas q usan interfaces dejan abierto un terminal, para q no aparesca
#pyinstaller --onefile -w name_project.py

#usar "nullsoft scriptable" para crear un ejecutable a partir de comprimir todo el programa por pyinstaller 