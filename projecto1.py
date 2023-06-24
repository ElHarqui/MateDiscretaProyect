import pandas as pd
#alfa = open ( "./MateDiscretaProyect/data.csv", "a")
#alfa.close()
#*Posiblemente Este de mas esta clase / eliminar si es el caso
class Alumno :
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
#*



        
Preg1 = {
    "1"  :  "futbol",
    "2" :  "basquet",
    "3"  :  "voley",
    "4" :  "natacion",
    "5" :  "karate",
    "6"  :  "otros"
}
Preg2 = {
    "1" : "salsa",
    "2" : "rock",
    "3" : "bachata",
    "4" : "regaetton",
    "5" : "merengue",
    "6" : "technocumbia",
    "7" : "folklorica",
    "8" : "otros"
}
Preg3 = Preg2
Preg4 = {
    "1" : "guitarra",
    "2" : "bateria",
    "3" : "piano",
    "4" : "saxo",
    "5" : "no toca",
    "6" : "otros"
}
Preg5 = {
    "1" : "x",
    "2" : "y",
    "3" : "z",
    "4" : "d",
    "5" : "p"
}
Preg6 = {
    "1" : "cine",
    "2" : "visitar museos",
    "3" : "viajar",
    "4" : "oratoria",
    "5" : "videojuegos",
    "6" : "conciertos",
    "7" : "otros"
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
            print(h[i])
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
def menu():
    menu1 = "\t\tMENU\n1.- Agregar Alumnos\n2.- Agregar Preguntas\n2.- Formar Equipos"
    print(menu1)
    usu1 = input("> ")
    match (usu1):
        case ("1"):
            AgregarAlumnos()
        case ("2"):
            AgregarPreguntas()
        case (_):
            print("vuelva a intentarlo")
            menu()






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