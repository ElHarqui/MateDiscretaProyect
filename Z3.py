import pandas as pd
import random

Preg1 = {
    "1": "futbol",
    "2": "basquet",
    "3": "voley",
    "4": "natacion",
    "5": "karate",
    "6": "otros"
}

Preg2 = {
    "1": "salsa",
    "2": "rock",
    "3": "bachata",
    "4": "regaetton",
    "5": "merengue",
    "6": "technocumbia",
    "7": "folklorica",
    "8": "otros"
}

Preg3 = Preg2

Preg4 = {
    "1": "guitarra",
    "2": "bateria",
    "3": "piano",
    "4": "saxo",
    "5": "no toca",
    "6": "otros"
}

Preg5 = {
    "1": "x",
    "2": "y",
    "3": "z",
    "4": "d",
    "5": "p"
}

Preg6 = {
    "1": "cine",
    "2": "visitar museos",
    "3": "viajar",
    "4": "oratoria",
    "5": "videojuegos",
    "6": "conciertos",
    "7": "otros"
}
Preg = [Preg1,Preg2,Preg3,Preg4,Preg5,Preg6] 
Persona = list()   
#x = Preg.keys()
#print(Preg[1].keys())
b = str()
hh = ["1.- Cual es su deporte favorito?","2.- Que musica le gusta ?","3.- Que danza le gusta de preferencia?","4.- Toca algun instrumento?","5.- Cual es su clib favorito?","6.- Cual es su hobbie favorito?"]
h = []



def AgregarPreguntas():
    PreguntasArchivo = pd.read_csv("Preguntas.csv",sep = ";",header= 0)
    ColumnaPregunta = PreguntasArchivo
    print(ColumnaPregunta)
    print("Cuantas preguntas va a agregar?")
    npre0 = int(input("->"))
    for i in range(npre0) :
        print("Ingrese nueva pregunta")
        npre = input("->")
        #Pnue0 = pd.assign( Pregunta = npre)
        #Pnue.to_csv("preguntas.csv",";",mode = "a", header= False, index= False)
        print("Cuantas respuestas va a tener?")
        nres = int(input("->"))
        nuerestemp = str()
        for j in range(nres):
            print(f"Ingrese respuesta {i+1} : ")
            nueres = input("->")
            if j != nres -1 :
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

    for k in range (n) :
        print(f'Ingrese nombre del alumno N°{k+1} :')
        b = ""
        nombre = input("-> ")
        for i in range (6)  :
            print(hh[i])
            r = list(Preg[i].keys())
            for j in range(len(r)) :
                print(f'{r[j]} :   {Preg[i][r[j]]}')
            a = input('-> ')
            b = b + a
        #*  
        Persona.append(f'Persona{k}')
        Persona[k] = Alumno(nombre , b)
        #*
        GuardarDatosCSV(nombre,b)

def FormarEquipos():
    print("Ingrese las preguntas de código a analizar (separadas por comas):")
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