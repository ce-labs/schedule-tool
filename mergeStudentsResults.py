# Schedule Tool
# File name: mergeStudentsResults.py
# Date last modified: 08/03/2021
# Description: This script it's for combining all students excel sheets, and sorts the  data by the oldest excel file.
# Notes: Don't change this python name, Don't delete  "Resultados" folder

import os
import pandas as pd  # For installation with pip -> "pip install pandas", "pip install openpyxl"," pip install xlrd"
import shutil


def deleteTempFiles(path):
    shutil.rmtree(path)
    print("4. Eliminación de archivos temporales generados.")
    #print('\n----File Deleted!----\n')


def copyFiles(source, destination):
    shutil.copytree(source, destination)
    print("1. Lectura de los archivos recibidos por los estudiantes.")
    #print('\n----Files copied!----\n')


def getListFiles(pathFiles):
    os.chdir(pathFiles)
    listFiles = filter(os.path.isfile, os.listdir(pathFiles))  # Get file sorted by the oldest
    listFiles = [os.path.join(pathFiles, f) for f in listFiles]  # add path to each file
    listFiles.sort(key=lambda x: os.path.getmtime(x))
    print("2. Adición de cada uno de los archivos  en la carpeta de ExcelRecibidos a una lista interna.")
    """for i in listFiles:  # Must only show excel files
        print(i)"""
    return listFiles


def mergeExcels(pathFinalFile, tempPath, sourceFiles):
    copyFiles(sourceFiles, tempPath)
    listStudentFiles = getListFiles(tempPath)
    storedData = []
    for i in listStudentFiles:
        dataExcel = pd.read_excel(i, 'RegistroHorario')
        valuesExcel = dataExcel[['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']]
        storedData.append(valuesExcel)
    mergeData = pd.concat(storedData)
    actualPath = os.path.dirname(__file__)  # Get actual file path
    os.chdir(actualPath)
    mergeData.to_excel(pathFinalFile, index=False)
    print("3. Proceso de combinación de contenido de archivos terminado.")
    #print('\n----Merge Part ended!----\n')
    deleteTempFiles(tempPath)


def main():
    print("\n-------- Inicio de ejecución sobre mergeStudentsResults.py ----------------------------------------\n")
    actualPath = os.path.dirname(__file__)  # Get actual file path
    tempPath = actualPath + r'\tempFiles'
    sourceFiles = actualPath + r'\ExcelRecibidos'
    pathFinalFile = actualPath + r'\Resultados\horariosUnidos_SinProcesar.xlsx'
    mergeExcels(pathFinalFile, tempPath, sourceFiles)


main()
