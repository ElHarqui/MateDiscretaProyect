class Alumno:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

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

Preg = [Preg1, Preg2, Preg3, Preg4, Preg5, Preg6]
Persona = list()

h = ["1.- Cual es su deporte favorito?", "2.- Que musica le gusta ?", "3.- Que danza le gusta de preferencia?",
     "4.- Toca algun instrumento?", "5.- Cual es su club favorito?", "6.- Cual es su hobbie favorito?"]

print("Cuantas personas son?")
n = int(input("-> "))

for k in range(n):
    print(f'Ingrese nombre del alumno N°{k + 1}:')
    nombre = input("-> ")

    b = ""  # Variable para almacenar las respuestas de cada categoría

    for i in range(6):
        print(h[i])
        r = list(Preg[i].keys())
        for j in range(len(r)):
            print(f'{r[j]}:   {Preg[i][r[j]]}')
        a = input('-> ')
        b += a

    Persona.append(Alumno(nombre, b))  # Pasar la cadena de respuestas a la instancia de Alumno






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