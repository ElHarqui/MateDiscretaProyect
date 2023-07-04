nombre = input("Ingrese su nombre: ")
print(nombre)

altura=(input("Ingrese la altura: "))
Acuad=(altura*altura)
print(nombre,", El área del cuadrado es: ",Acuad)

Ultimo = int(input("Digite el ultimo numero: "))
suma=0
n = 0
while n<=Ultimo :
  suma += n
  n+=1
print(suma)

if suma>100:
  print("Su suma es grande")
else:
  print("Su suma no es tan grande")

r=5
for i in range (r):
   print("Hola")