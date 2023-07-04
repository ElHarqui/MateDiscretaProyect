class Alumno:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
Persona = list()



#!AQUI ESTOY PASANDO LAS PREGUNTAS A EL ARCHIVO
#!FALTARIA  HACER QUE SE LEAN DE MANERA DINAMICA LAS PREGUNTAS Y RESPUESTAS

h = [] #* ESTE ES EL VECTOR DONDE SE GUARDARAN LAS PREGUNTAS

print("Cuantas personas son?")
n = int(input("-> "))

for k in range(n):
    print(f'Ingrese nombre del alumno N°{k + 1}:')
    nombre = input("-> ")

    b = ""  # *Variable para almacenar las respuestas de cada categoría

    for i in range(6):
        print(h[i])
        #r = list(Preg[i].keys())
        for j in range(len(r)):
            #print(f'{r[j]}:   {Preg[i][r[j]]}')
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