fechatupla=(25,12,2016)
print("Imprimir la primer tupla")
print(fechatupla)
#copiamos la tupla en una lista
fechalista=list(fechatupla)
print("Imprimos la lista que se le copio la tupla anterior")
print(fechalista)
#modificamos la lista
fechalista[0]=31
print("imprimimos la lista ya modificada")
print(fechalista)
#copiamos la lista modificada a una tupla
fechatuplas2=tuple(fechalista)
print("Imprimimos la segunda tupla que se copio la lista")
print(fechatuplas2)