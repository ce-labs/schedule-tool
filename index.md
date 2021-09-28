## Schedule-tool

[Schedule-tool](https://github.com/ce-labs/schedule-tool/releases) es una herramienta que realiza el ordenamiento de horarios de trabajo de los operadores en laboratorios del [Área Académica de Ingeniería en Computadores](https://www.tec.ac.cr/programas-academicos/licenciatura-ingenieria-computadores), se realizó con el fin de automatizar y agilizar el proceso de definición de horarios según la disponibilidad de los operadores.

Dicha herramienta recibe los horarios disponibles de cada uno de los operadores, según una plantilla establecida. Seguidamente el programa comienza a procesar los horarios de entrada, el encargado debe decidir si desea 1 o 2 estudiantes por turno, y retorna dos archivos uno con el horario propuesto, y otro con los estudiantes no incluidos, si fuese el caso.

### Registro de Cambios - Documentación

<table>
   <tr>
     <th align = "center">
       <img width = "441" height = "1">
       <p> <small> Version </small> </p>
     </th>
     <th align = "center">
       <img width = "441" height = "1">
       <p> <small> Causa del Cambio  </small> </p>
     </th>
     <th align = "center">
       <img width = "441" height = "1">
       <p> <small> Responsable </small> </p>
     </th>
     <th align = "center">
       <img width = "441" height = "1">
       <p> <small> Fecha </small> </p>
     </th>
   </tr>
   <tr>
     <td align = "center">
       001
     </td>
     <td align = "center">
       Versión Inicial
     </td>
     <td align = "center">
       Angelo Ortiz Vega (angelortizv@estudiantec.cr)
     </td>
     <td align = "center">
       09/28/2021
     </td>
   </tr>
</table>

### Sección Operador

A continuación, se mostrarán los pasos que deben seguir los operadores para llenar sus solicitudes. 

Como primera instancia, se tienen la plantilla mostrada en la siguiente imagen donde se muestran los espacios que el estudiante debe llenar, primeramente se debe de completar los espacios en amarillo al lado de “Nombre de Operador” y “Carné” 

<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135148430-9f4b81b8-3fa4-43e5-9851-85a4485d8d12.png" alt="Manual de Usuario - Estudiante 001"/>
</p>

Si no se completan los espacios en amarillo y se selecciona alguno de los espacios en blanco del horario, aparecerá el siguiente mensaje: 

<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135148429-8b3aba6e-5efe-4b3c-b198-e80765b9e1f4.png" alt="Manual de Usuario - Estudiante 002"/>
</p>

Una vez llenados los espacios amarillos mencionados anteriormente, se podrá seleccionar con “doble click” cualquiera de los espacios en blanco del horario, cambiando a color verde. El resultado final debe ser parecido al siguiente ejemplo: 

<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135148427-40ff8a61-995e-4c38-ae47-bf55e6473e85.png" alt="Manual de Usuario - Estudiante 003"/>
</p>

El archivo Excel de la plantilla, tiene dos sheet: “Horario” y “RegistroHorario”; en la primera aparece el horario que se mostró anteriormente, y en la segunda sheet debe aparecer una lista (según los espacios seleccionados) con lo siguiente: los datos ingresados en los espacios amarillos, la fecha y hora según lo seleccionado en el primer sheet; como se muestra a continuación: 

<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135148425-9cd66549-181a-4a01-93e4-a38cec977c2d.png" alt="Manual de Usuario - Estudiante 004"/>
</p>

Finalmente guarde el archivo con su nombre y carnet en el siguiente formato: NOMBRE - CARNÉ (estudiante1 - 2001111111).

Para acceder a la plantilla, haga click [aquí](https://github.com/ce-labs/schedule-tool/docs/).


### Sección administrador de herramienta

Para esta sección, ya se debe tener los archivos con las selecciones de los operadores, para ser ingresados a una carpeta que comenzará el procedimiento del programa. Se explicará con ejemplos para mejorar la comprensión del programa. 

#### Instalación en la máquina

Prerequisitos: Debe tener instalado [Git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git) en su consola.

1. En GitHub, vaya a la página principal del [repositorio del Proyecto](https://github.com/ce-labs/schedule-tool).
2. Debajo del nombre del repositorio, haga clic en Clonar o descargar.
3. En la sección Clonar con HTTPs, haga clic para copiar la URL de clonación del repositorio.
4. Abre Git Bash y cambie el directorio de trabajo actual a la ubicación donde desea que se realice el directorio clonado.
5. Escriba 'git clone', y luego pegue la URL que copió en el Paso 2.

```$ https://github.com/ce-labs/schedule-tool.git ```

Para iniciar, al abrir la carpeta principal se deben de tener lo siguiente: 


#### Requisitos para utilizar el programa

El programa está codificado en Python 3, específicamente en la versión Python 3.7 (64 bits) y es necesario tener instalado preferiblemente Excel o algún programa que permita la lectura de archivos con extensión .xlsx para visualizar la información de manera correcta.  

También se requiere tener instalado las siguientes librerías de Python: 

* Pandas 
* Openpyxl 
* Xlrd 

Dichas librerías se pueden instalar con el siguiente comando desde consola: 

```pip install pandas openpyxl xlrd```
 
Se debe tener instalado pip (las últimas versiones de Python lo incluyen). 


#### Uso de la herramienta

Para esta sección, ya se debe tener los archivos con las selecciones de los operadores, para ser ingresados a una carpeta que comenzará el procedimiento del programa. Se explicará con ejemplos para mejorar la comprensión del programa. 

Para iniciar, al abrir la carpeta principal se debe de tener lo siguiente: 


<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135151604-010c1cb7-73ed-4b8d-8d61-c50f7b8d4baf.png" alt="Manual de Usuario - Administrador 001"/>
</p>

En la carpeta “src/data” se procede a ingresar todos los horarios seleccionados de los operadores, y debe visualizarse de la siguiente manera: 

<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135151819-9e10a2fa-6255-47aa-8252-91cf8daf2a5d.png" alt="Manual de Usuario - Administrador 002"/>
</p>

La fecha de la ultima modificación del archivo afectará en el orden de prioridad que se asignará en el horario final, por lo que se debe de asegurar que se respeta la hora que se recibió el archivo (ya que, si un operador tenía la hora de su computador atrasada, eso afectará al establecer la prioridad del horario). Una vez los archivos en dicha carpeta, ya está listo para realizar la ejecución del programa. 

Abra el programa en un editor, para este ejemplo lo realicé en [Pycharm](https://www.jetbrains.com/pycharm/)

Deberá aparecer la estructura del proyecto de este modo:

<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135152288-836fd521-8a19-4405-8fb8-fea78fd1293f.png" alt="Manual de Usuario - Administrador 003"/>
</p>

Bajo la configuración del Proyecto, edite los espacios de tal manera que le quede así:

<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135152521-a837aaad-9617-485b-a894-7f7c53ed8c86.png" alt="Manual de Usuario - Administrador 004"/>
</p>

Ejecute el programa, y digite 1 o 2, según crea conveniente (cantidad de estudiantes). En consola le aparecerá un resultado como se muestra en la siguiente imagen:

<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135152644-7fd5b81d-0981-4cb1-bd6b-8a0ff449837f.png" alt="Manual de Usuario - Administrador 005"/>
</p>

En lo archivos con nombre "HorarioCompleto.xlsx" y "notInList.xls" se encuentran los resultados generados.

Si usted digitó 1, la herramienta asignará un estudiante por casilla con prioridad de recepción de archivo. Puede observar el horario tentivo en "HorarioCompleto.xlsx" y estudiantes no asignados en "notInList.xls".

----> "HorarioCompleto.xlsx"
<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135153406-d388de1b-6564-40b0-98b9-80f1b2f362d5.png" alt="Manual de Usuario - Administrador 006"/>
</p>

----> "notInList.xlsx"
<p align="center">
  <img src="https://user-images.githubusercontent.com/18412939/135153408-8ceae434-e860-43f7-b822-d6a9ab87ba2f.png" alt="Manual de Usuario - Administrador 008"/>
</p>

Este es el resultado final, donde se puede observar los supuestos nombres de los estudiantes ordenados según la hora de los archivos de la plantilla del horario.  El archivo Python “main”, ejecuta los dos archivos Python mencionados anteriormente, reduciendo el proceso del programa a un solo archivo. 


### Soporte y Contacto

Si desea contactarnos, visite el sitio en Github para obtener más información [ce-labs] (https://github.com/ce-labs/schedule-tool/)
