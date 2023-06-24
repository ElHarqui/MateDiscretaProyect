import pandas as pd
#alfa = open ( "./MateDiscretaProyect/data.csv", "a")
#alfa.close()
class Alumno :
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        
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

menu = "\t\tMENU\t1.- PREGUNTAS"
#x = Preg.keys()
#print(Preg[1].keys())
b = str()
h = ["1.- Cual es su deporte favorito?","2.- Que musica le gusta ?","3.- Que danza le gusta de preferencia?","4.- Toca algun instrumento?","5.- Cual es su clib favorito?","6.- Cual es su hobbie favorito?"]
print("Cuantas personas son ?")
n = int(input("-> "))
####!
#!      

####!
df = pd. read_csv("data.csv", sep=";" )
print(df)
print(df["codigo_alum"].size)
print(df.index)
print(df.size)
print(df.dtypes)
for k in range (n) :
    print(f'Ingrese nombre del alumno N°{k+1} :')
    nombre = input("-> ")
    for i in range (6)  :
        print(h[i])
        r = list(Preg[i].keys())
        for j in range(len(r)) :
            print(f'{r[j]} :   {Preg[i][r[j]]}')
        a = input('-> ')
        b = b + a  
    Persona.append(f'Persona{k}')
    Persona[k] = Alumno(nombre , b)
    archivo = pd.DataFrame({"nombre_alum" : [Persona[k].nombre] ,"codigo_alum" : [Persona[k].codigo]})
    print(archivo)
    archivo.to_csv("data.csv",";",mode= "a", header= False, index= False)
    df = pd. read_csv("data.csv", sep=";")

    #*GUARDAR b EN UNA ESTRUCTURA
    

