import pycdlib
import os
import sys


def getArchivos(ruta):
    archivos = list()
    directorios = list()
    for item in os.scandir(ruta):
        if item.is_file():
            archivos.append(item)
        elif item.is_dir():
            directorios.append(item)
    return {"archivos": archivos, "directorios": directorios}

def copiarSoloFicheros( listaArchivos,raiz):
    # print(origen)

    # print(gficheros)
    for archivo in listaArchivos:
        if not archivo.name.startswith("."):
            print("creado archivo","%s/%s"%(raiz,archivo.name))
            iso.add_file(archivo.path,udf_path="%s/%s"%(raiz,archivo.name))



def copiarFicheros(origen,raiz):
    gficheros = getArchivos(origen)
    copiarSoloFicheros(gficheros["archivos"],raiz)

    for dir in gficheros["directorios"]:
        if not dir.name.startswith(".") :
                print("creado directorio:","%s/%s"%(raiz,dir.name))
                iso.add_directory(udf_path="%s/%s"%(raiz,dir.name))
                copiarFicheros(dir.path,"%s/%s"%(raiz,dir.name))
def create_iso(rutaOrigen):
    raiz="/"
    gficherosApps = getArchivos(rutaOrigen)
    copiarSoloFicheros(gficherosApps["archivos"],raiz)

    for dir in gficherosApps["directorios"]:
        if not dir.name.startswith("__"):
            print("creado directorio:", "%s%s" % (raiz, dir.name))
            iso.add_directory(udf_path="%s%s" % (raiz, dir.name))
            copiarFicheros(dir.path,"%s%s"%(raiz,dir.name))






iso = pycdlib.PyCdlib()

iso.new(udf="2.60")
# Uso
rutaDesde = "."
destino = None
if len(sys.argv) > 1:
   rutaDesde = sys.argv[1]
if len(sys.argv) > 2:
   destino = sys.argv[2]

if destino and rutaDesde != destino:
    create_iso(rutaDesde)
    iso.write(destino)
    iso.close()
print("Se ha reado la iso.. %s"%destino)

