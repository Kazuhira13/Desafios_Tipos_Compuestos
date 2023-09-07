nombre=[]
edades=[]
for x in range (5):
    nom=input("ingrese el nombre de la persona:")
    nombre.append(nom)
    ed= int(input("Ingrese la edad de dicha persona:"))
    edades.append(ed)
print("Nombre de las persona mayores de edad:")
for x in range(5):
    if edades[x]>=18:
        print(nombre[x])
