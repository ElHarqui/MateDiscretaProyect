import pandas as pd
#alfa = open ( "./MateDiscretaProyect/data.csv", "a")
#alfa.close()
#*Posiblemente Este de mas esta clase / eliminar si es el caso
class Alumno :
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
"""
Preg = []  #GUARDAR PREGUNTAS
"""
Persona = list()  
""" 
b = str()
hh = [] #GUARDAR RESPUESTAS
h = []"""
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
            print(f"Ingrese respuesta {j+1} : ")
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
    PreguntasArchivo = pd.read_csv("Preguntas.csv",sep = ";",header= 0) #Leyendo CSV para obtener las preguntas y variables
    Preguntas = PreguntasArchivo['preguntas'] #Preguntas
    RespuestasCompuestas = PreguntasArchivo['respuestas']# Respuestas
    Preguntas = list(Preguntas) #*Lista de Preguntas
    RespuestasCompuestas = list(RespuestasCompuestas) #* Lista de respuestas(Compuestas)
    Num_Preguntas = len(Preguntas) #* *N° Cantidad de preguntas   == Cantidad de respuestas compuestas
    for k in range (n) :
        print(f'Ingrese nombre del alumno N°{k+1} :')
        b = ""
        nombre = input("-> ")
        for i in range (Num_Preguntas)  :
            print(f"{i+1}.- {Preguntas[i]}\n")#*Imprimiendo Preguntas del archivo
            #La lista de respuestas compuestas las separamos en un nuevo vector
            RespuestasSeparadas = RespuestasCompuestas[i].split("/")
            Num_RespuestasSeparadas = len(RespuestasSeparadas)
            
            for j in range(Num_RespuestasSeparadas) :
                print(f'    {j+1} :  {RespuestasSeparadas[j]}')#*Imprimiendo Respuestas del archivo
            a = input(' -> ')
            b = b + a
        #*  
        Persona.append(f'Persona{k}')
        Persona[k] = Alumno(nombre , b)
        #*
        GuardarDatosCSV(nombre,b)
        print("\n")
def menu():
    menu1 = "\t\tMENU\n1.- Agregar Alumnos\n2.- Agregar Preguntas\n3.- Formar Equipos"
    print(menu1)
    usu1 = input("> ")
    match (usu1):
        case ("1"):
            AgregarAlumnos()
        case ("2"):
            AgregarPreguntas()
        case ("3"):
            Combinar_Equipos()
        case (_):
            print("vuelva a intentarlo")
            menu()

#!##################################################################################
def Combinar_Equipos():
    # Obtener el número de preferencias a buscar
    print("Ingrese el número de preferencias a buscar:")
    num_preferencias = int(input("-> "))

    # Crear una lista para almacenar las preferencias a buscar
    preferencias_buscar = []

    for _ in range(num_preferencias):
        print("Ingrese el tipo de gusto:")
        num_pregunta = int(input("-> "))

        print(f"Ingrese el número de respuesta para la pregunta {num_pregunta}:")
        num_respuesta = int(input("-> "))

        # Almacenar la pregunta y respuesta en una tupla y agregarla a la lista de preferencias a buscar
        preferencias_buscar.append((num_pregunta, str(num_respuesta)))

    # Encontrar personas que coincidan en todas las preferencias
    personas_coincidentes = []

    for persona in Persona:
        coincidente = True

        for preferencia in preferencias_buscar:
            pregunta, respuesta = preferencia

            if persona.codigo[pregunta - 1] != respuesta:
                coincidente = False
                break

        if coincidente:
            personas_coincidentes.append(persona.nombre)

    # Mostrar el equipo formado
    if personas_coincidentes:
        print("Equipo formado con las siguientes personas:")
        print(", ".join(personas_coincidentes))
    else:
        print("No se encontraron personas que coincidan en todas las preferencias.")


#!##################################################################################




if __name__ == "__main__":
    menu()







#!
####!
#!      

####!
#df = pd. read_csv("data.csv", sep=";" )
#colum = df["codigo_alum"]
#print(colum[1])

#print(df)
#print(df["codigo_alum"].size)
#print(df.index)
#print(df.size)
#print(df.dtypes)