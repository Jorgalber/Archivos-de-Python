#Jorge alberto

from PIL import Image
import os

rutaActual= os.path.dirname(os.path.abspath(__file__))

def formatRuta(ruta):
    clean=""
    for caracter in ruta:
        if caracter=='\\':
            clean=clean+'/'
        else:
            clean=clean+caracter
    return clean

currentFolder= formatRuta(rutaActual)+"/"

organized_files= currentFolder+'/ArchivosOrganizados'

organized_filesImagenes= currentFolder+'/ArchivosOrganizados/Imagenes'
organized_filesAudio=currentFolder+'/Archivosorganizados/Audios'
organized_filesPDF=currentFolder+'/Archivosorganizados/PDF'
organized_filesCompresed=currentFolder+'/Archivosorganizados/Comprimidos'
organized_filesHojasDCalculo=currentFolder+'/Archivosorganizados/HojasDeCalculo'
organized_filesDocumentosTex= currentFolder+'/ArchivosOrganizados/DocumentosDeTexto'

if os.path.isdir(organized_files):
    if not os.path.isdir(organized_filesImagenes):
        os.mkdir(organized_filesImagenes)
    if not os.path.isdir(organized_filesAudio):
        os.mkdir(organized_filesAudio)
    if not os.path.isdir(organized_filesPDF):
        os.mkdir(organized_filesPDF)
    if not os.path.isdir(organized_filesCompresed):
        os.mkdir(organized_filesCompresed)
    if not os.path.isdir(organized_filesHojasDCalculo):
        os.mkdir(organized_filesHojasDCalculo)
    if not os.path.isdir(organized_filesDocumentosTex):
        os.mkdir(organized_filesDocumentosTex)
else:
    os.mkdir(organized_files)
    os.mkdir(organized_filesImagenes)
    os.mkdir(organized_filesAudio)
    os.mkdir(organized_filesPDF)
    os.mkdir(organized_filesCompresed)
    os.mkdir(organized_filesHojasDCalculo)
    os.mkdir(organized_filesDocumentosTex)


if __name__== "__main__":
    for filename in os.listdir(currentFolder):
        name,extension= os.path.splitext(currentFolder+ filename)

        if extension in [".jpg",".jpeg",".png","gif"]:
            picture= Image.open(currentFolder+filename)
            picture.save(organized_filesImagenes+'/'+"comprezed_"+ filename, optimized=True, quality=60)
            os.remove(currentFolder+filename)
        
        if extension in [".mp3",".flac"]:
            os.rename(currentFolder+filename, organized_filesAudio + '/' + filename)
        
        if extension in [".pdf"]:
            os.rename(currentFolder+filename, organized_filesPDF + '/' + filename)
        
        if extension in [".zip",".rar"]:
            os.rename(currentFolder+filename, organized_filesCompresed + '/' + filename)
        
        if extension in [".xlsx",".csv"]:
            os.rename(currentFolder+filename, organized_filesHojasDCalculo + '/' + filename)
        
        if extension in [".doc", ".docx", ".docm", ".dotx"]:
            os.rename(currentFolder+filename, organized_filesDocumentosTex +'/' + filename) 
