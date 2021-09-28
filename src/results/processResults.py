# Schedule Tool
# File name: processResults.py
# Date last modified: 08/03/2021
# Description: This script it's for place the student's name into a general schedule

import os
import pandas as pd  # For installation with pip -> "pip install pandas", "pip install openpyxl"," pip install xlrd"


def getListFiles(nameFileResult):
    actualPath = os.path.dirname(__file__)  # Get current file path
    # listFiles = sorted(os.listdir(actualPath), key=os.path.getctime)  # Get file sorted by the oldest
    listFiles = sorted(os.listdir(actualPath))
    # Remove files in use from the list
    listFiles.remove("processResults.py")
    # listFiles.remove("horariosDisponibles.txt")
    listFiles.remove("notInList.xlsx")
    try:
        listFiles.remove(nameFileResult)  # Delete this python file from list
    except:
        1 + 1
    for i in listFiles:  # It should show only excel files
        pass
        # print("1. Lectura del archivo horariosUnidos_SinProcesar.xlxs" )
        # print("i: " + i)
    print("1. Lectura del archivo horariosUnidos_SinProcesar.xlxs")
    return listFiles


def scheduleData():  # Return matrix with all the days and hours
    dfCondition = []
    actualPath = os.path.dirname(__file__)
    f = open(actualPath + r'\assets\horariosDisponibles.txt', "r", encoding='utf-8')
    txtLine = f.readline()
    while (txtLine != "ETX"):  # change "ETX" to "", if you want to delete ETX line of file
        values = txtLine.split(",")  # position 0 -> Day   position 1 -> hours
        dfCondition.append(values[0:2])
        txtLine = f.readline()
    return dfCondition


def getDaysFiltered(dataFrame, dfConditions):
    daysSelected = []
    print("3. Selección de estudiante por horario.")
    for i in range(len(dfConditions)):
        filterAux = (dataFrame['Unnamed: 0'] == dfConditions[i][0]) & (dataFrame['Unnamed: 1'] == dfConditions[i][1])
        #print(dataFrame.loc[filterAux])
        daysSelected.append(dataFrame.loc[filterAux])
    return daysSelected


def concatStudents(studentsData):
    concatStudents = ""
    for student in studentsData:
        concatStudents += student + " \r \n "
    return concatStudents


def createExcelFile():
    dataSchedule = scheduleData()
    horas = []
    dias = []
    pos = 0
    count = 0
    IsLunes = True
    while count < len(dataSchedule):
        if (dataSchedule[count][0] == 'LUNES (L)' and IsLunes):
            horas.append(dataSchedule[count][1])
            count += 1
            if (dataSchedule[count][0] != 'LUNES (L)'):
                IsLunes = False
                count = 0
        else:
            dias.append(dataSchedule[count][0])
            count += 5
    """print("dias: ")
    print(dias)
    print("horas: ")
    print(horas)"""
    dataInsert = {'Horas': horas}
    for i in dias:
        dataInsert[i] = ''

    df = pd.DataFrame(dataInsert)
    return df


def positionHourExcel(x):
    return {
        '7:00am - 10:00am': 0,
        '10:00am - 12:30pm': 1,
        '12:30pm - 3:30pm': 2,
        '3:30pm - 6:30pm': 3,
        '6:30pm - 9:30pm': 4
    }[x]


def removeFirstFiltered(lst):
    newList = []
    thirdElems = {}
    daySections = {}
    for elem in lst:
        thirdElem = elem[3]
        daySection = elem[0] + elem[1]
        if (thirdElem in thirdElems) or (daySection in daySections):
            continue
        newList.append(elem)
        thirdElems[thirdElem] = 1
        daySections[daySection] = 1
    return newList


def removeLast(lst):
    newList = []
    thirdElems = {}
    for elem in lst:
        thirdElem = elem[3]
        if (thirdElem in thirdElems):
            continue
        newList.append(elem)
        thirdElems[thirdElem] = 1
    return newList


def checkAllStudents(lst, filteredList):
    notInList = []
    for elem in lst:
        thirdElem = elem[3]
        if not any(thirdElem in sublst for sublst in filteredList):
            # print(elem)
            notInList.append(elem)
    return notInList


def flatten(listOrItem, result=None):
    daySections = {}
    if result is None:
        result = []
    if type(listOrItem) != type([]):
        result.append(listOrItem)
    else:
        for item in listOrItem:
            daySection = item[0] + item[1]
            flatten(daySection, result)
    return result


def checkLength(lst, pos):
    auxlst = flatten(lst)
    # print(auxlst[pos])
    if (lst.count(auxlst[pos]) < 2):
        # print(lst[pos] + " ok" )
        return True
    else:
        # print(lst[pos] + " mayor a 2")
        return False


def addOutStudents(filteredList, outList):
    newList = filteredList
    counter = 0
    for elem in outList:
        if (checkLength(newList, counter)):
            newList.append(elem)
            # print(elem)
            # print(newList)
        counter += 1
    # print(newList)
    return newList


def getDataExcel(nameFileResult):
    listStudentFiles = getListFiles(nameFileResult)

    actualPath = os.path.dirname(__file__)
    actualFile = actualPath + r'\horariosUnidos_SinProcesar.xlsx'   # Get current file path
    # print(actualPath + r'\' + listStudentFiles[-1])
    dataExcel = pd.read_excel(actualFile)  # Get newest excel file
    dataFrame = pd.DataFrame(dataExcel, columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'])

    dfConditions = scheduleData()  # Get all conditions values

    totalStudentsList = dataFrame.values.tolist()

    print("2. Escriba '1' si quiere 1 estudiante por casilla y '2' si quiere 2 o más estudiantes por casilla:")
    condValue = int(input("Digite el valor aquí: "))

    if condValue == 1:
        print(">> Inicio de proceso para un estudiante por casilla")
        filteredStudentsList = removeFirstFiltered(totalStudentsList)
        outList = checkAllStudents(totalStudentsList, filteredStudentsList)

    elif condValue == 2:
        print(">> Inicio de proceso para dos estudiantes por casilla")
        firstfilter = removeFirstFiltered(totalStudentsList)
        firstout = checkAllStudents(totalStudentsList, firstfilter)

        finalList = addOutStudents(firstfilter, firstout)
        outList = checkAllStudents(firstout, finalList)

        filteredStudentsList = removeLast(finalList)
        #print(filteredStudentsList)

    dF = pd.DataFrame.from_records(filteredStudentsList, columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'])

    notInListDF = pd.DataFrame.from_records(outList, columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'])
    writer = pd.ExcelWriter(actualPath + r'\notInList.xlsx')
    notInListDF.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()

    daysSelected = getDaysFiltered(dF, dfConditions)  # get days and hours filtered by conditions

    dffinal = createExcelFile()
    for day in daysSelected:
        dayHour = day.values.tolist()
        listStudent = []
        day = dayHour[0][0]
        hour = dayHour[0][1]

        for student in dayHour:
            listStudent.append(student[2])
        concatResult = concatStudents(listStudent)
        #print("concatResult: " + concatResult)

        hourAux = positionHourExcel(hour)

        dffinal.at[hourAux, day] = concatResult

    dffinal.to_excel(nameFileResult, index=False)
    print("4. Proceso de calendarización de horarios terminado.")

    return True


def main():
    print("\n-------- Inicio de ejecución sobre processResults.py ----------------------------------------------\n")
    finalSchedule = os.path.dirname(__file__) + r'\HorarioCompleto.xlsx'
    getDataExcel(finalSchedule)
    print("\n-------- Proceso terminado exitosamente -----------------------------------------------------------")
    print("\nPuede ver el horario general en el archivo HorarioCompleto.xlsx y los resagados en notInList.xlsx")
    exit(True)


main()
