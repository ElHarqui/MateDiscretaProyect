import pandas as pd
PreguntasArchivo = pd.read_csv("Preguntas.csv",sep = ";",header= 0) #Leyendo CSV para obtener las preguntas y variables
Preguntas = PreguntasArchivo['preguntas'] #Preguntas
Preguntas = list(Preguntas)
print(Preguntas)
Respuestas = PreguntasArchivo['respuestas']
Respuestas = list(Respuestas)
Num_Preguntas = Preguntas.size #Numero de preguntas existentes
print(Num_Preguntas)