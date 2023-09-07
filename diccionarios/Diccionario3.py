def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("ingrese palabra en castellano:")
        ing= input("ingrese palabra en ingles:")
        diccionario[ing]=caste
        continua=input("quiere cargar otra palabra [s/n]")
    return diccionario
    
def imprimir(diccionario):
    print("listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])

def consultar_palabra(diccinario):
    pal=input("ingrese la palabra en ingles a consultar:")
    if pal in diccinario:
        print("en castellano significa:",diccinario[pal])

diccionario=cargar()
imprimir(diccionario)
consultar_palabra(diccionario)
