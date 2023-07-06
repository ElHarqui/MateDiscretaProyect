import pandas as pd
import random

#*Posiblemente Este de mas esta clase / eliminar si es el caso
class Alumno :
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
Persona = list()  

def AgregarPreguntas():
    PreguntasArchivo = pd.read_csv("Preguntas.csv",sep = ";",header= 0)
    ColumnaPregunta = PreguntasArchivo
    print(ColumnaPregunta)
    print("Cuantas preguntas va a agregar?")
    npre0 = int(input("->"))
    for i in range(npre0) :
        print("Ingrese nueva pregunta")
        npre = input("->")
        print("Cuantas respuestas va a tener?")
        nres = int(input("->"))
        nuerestemp = str()
        for j in range(nres):
            print(f"Ingrese respuesta {j+1} : ")
            nueres = input("->")
            if (j != (nres -1)) :
                nuerestemp = nuerestemp + nueres+ "/"
            else :
                nuerestemp = nuerestemp + nueres
        Pnue = pd.DataFrame({"pregunta" : [npre],"respuestas" : [nuerestemp]})
        Pnue.to_csv("preguntas.csv",";",mode = "a",header= False, index= False)

def GuardarDatosCSV(nombre,codigo):
    archivo = pd.DataFrame({"nombre_alum" : [nombre] ,"codigo_alum" : [codigo]})
    archivo.to_csv("data.csv",";",mode= "a", header= False, index= False)
            
def AgregarAlumnos():
    print("Cuantos alumnos mas vas a agregar?")
    n = int(input("-> "))
    PreguntasArchivo = pd.read_csv("Preguntas.csv",sep = ";",header= 0) #Leyendo CSV para obtener las preguntas y variables
    Preguntas = PreguntasArchivo['preguntas'] #Preguntas
    RespuestasCompuestas = PreguntasArchivo['respuestas']# Respuestas
    Preguntas = list(Preguntas) #*Lista de Preguntas
    RespuestasCompuestas = list(RespuestasCompuestas) #* Lista de respuestas(Compuestas)
    Num_Preguntas = len(Preguntas) #* *N° Cantidad de preguntas   == Cantidad de respuestas compuestas
    for k in range (n) :
        print(f'Ingrese nombre del alumno N°{k+1} :')
        CodigoAculumar = ""
        nombre = input("-> ")
        for i in range (Num_Preguntas)  :
            print(f"{i+1}.- {Preguntas[i]}\n")#*Imprimiendo Preguntas del archivo
            #La lista de respuestas compuestas las separamos en un nuevo vector
            RespuestasSeparadas = RespuestasCompuestas[i].split("/") 
            
            Num_RespuestasSeparadas = len(RespuestasSeparadas)
            
            for j in range(Num_RespuestasSeparadas) :
                print(f'    {j+1} :  {RespuestasSeparadas[j]}')#*Imprimiendo Respuestas del archivo
            respuestaA = input(' -> ')
            CodigoAculumar = CodigoAculumar + respuestaA 
        #*  nombre , CodigoAculumar
        archivo = pd.DataFrame({"nombre_alum" : [nombre] ,"codigo_alum" : [CodigoAculumar]})
        archivo.to_csv("data.csv",";",mode= "a", header= False, index= False)
        print("\n")
        
def FormarEquipos():
    PreguntasArchivo = pd.read_csv("Preguntas.csv",sep = ";",header= 0)
    ColumnaPregunta = PreguntasArchivo['preguntas']
    ColumnaPregunta = list(ColumnaPregunta)
    NumPreguntas1 = len(ColumnaPregunta)
    print("\n\n->PREGUNTAS")
    for h in range (NumPreguntas1) :
        print(f' {h+1}  : {ColumnaPregunta[h]}')
    
    print("\nIngrese las preguntas de código a analizar (separadas por comas):")
    posiciones = input("-> ").split(",")
    posiciones = [int(p) for p in posiciones]

    print("Ingrese las respuestas específicas para formar los equipos (separados por comas):")
    numeros = input("-> ").split(",")
    numeros = [int(n) for n in numeros]

    equipos = []
    equipo_actual = []

    datos = pd.read_csv("data.csv", sep=";", header=0)

    for _, row in datos.iterrows():
        codigo = [int(c) for c in str(row["codigo_alum"])]

        coincide = True
        for pos, num in zip(posiciones, numeros):
            if codigo[pos - 1] != num:
                coincide = False
                break

        if coincide:
            equipo_actual.append(row["nombre_alum"])

    equipos = Agrupar(equipo_actual, 7)     
        
            #if len(equipo_actual) >= 5:
                #equipos.append(equipo_actual[:7])  # Limitamos el equipo a un máximo de 7 personas
                #equipo_actual = []  # Reiniciamos el equipo actual

    # if equipo_actual:  # Si hay personas que no formaron parte de un equipo completo
    # equipos.append(equipo_actual)

    num_equipos = len(equipos)
    print(f"Se formaron {num_equipos} equipos:")

    for i, equipo in enumerate(equipos):
        print(f"Equipo {i+1}: {equipo}")

def Agrupar(datos, tamGrupos):
    n = len(datos)
    numGrupos = n // tamGrupos
    elementosRestantes = n % tamGrupos
    
    random.shuffle(datos)
    
    gruposFinales = []
    
    for i in range(numGrupos):
        grupo = datos[i*tamGrupos : (i+1)*tamGrupos]
        gruposFinales.append(grupo)
    
    #Para los elementos sobrantes
    if elementosRestantes > 0:
        ultimoGrupo = datos[numGrupos*tamGrupos:]
        gruposFinales.append(ultimoGrupo)
    
    return gruposFinales        

def menu():
    print("\t\tMENU\n1.- Agregar Alumnos\n2.- Agregar Preguntas\n3.- Formar Equipos")
    usu1 = input("> ")

    if usu1 == "1":
        AgregarAlumnos()
    elif usu1 == "2":
        AgregarPreguntas()
    elif usu1 == "3":
        FormarEquipos()
    else:
        print("Opción no válida. Intente nuevamente.")
        menu()
        
if __name__ == "__main__":
    menu()