def cargar_fechas():
    dd=int(input("ingrese numero de dia:"))
    mm=int(input("ingrese numeros de mes:"))
    aa=int(input("ingrese numero de año:"))
    return(dd,mm,aa)

def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

fecha=cargar_fechas()
imprimir_fecha(fecha)