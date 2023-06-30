import random

def Agrupar(datos, tamGrupos):
    n = len(datos)
    numGrupos = n // tamGrupos
    elementosRestantes = n % tamGrupos
    
    random.shuffle(datos)
    
    grupos_finales = []
    
    for i in range(numGrupos):
        grupo = datos[i*tamGrupos : (i+1)*tamGrupos]
        grupos_finales.append(grupo)
    
    #Para los elementos sobrantes
    if elementosRestantes > 0:
        ultimo_grupo = datos[numGrupos*tamGrupos:]
        grupos_finales.append(ultimo_grupo)
    
    return grupos_finales

items = ['Alvaro', 'Bryan', 'Sergio', 'Sebastian', 'Cristian', 'Hector', 'Santiago', 'Rimbaud', 'Moquihot', 'Lucía', 'Diego', 'Valentina', 'Juan Diego', 'Isabela', 'Emilio']
tam_grupo = 7

grupos = Agrupar(items, tam_grupo)

for i, grupo in enumerate(grupos):
    print(f"Grupo {i+1}: {grupo}")
