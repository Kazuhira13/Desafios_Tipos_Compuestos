def cargar():
    agenda={}
    continua="s"
    while continua=="s":
        fecha=input("ingrese la fecha con formato dd/mm/aa:")
        continua2="s"
        lista=[]
        while continua2=="s":
            hora=input("ingrese la hora de la actividad con formato hh:mm:")
            actividad=input("ingrese la descripcion de la actividad:")
            lista.append((hora,actividad))
            continua2=input("ingrese otra actividad para la misma fecha [s/n]:")
        agenda[fecha]=lista
        continua=input("ingrese otra fecha[s/n]:")
    return agenda

def imprimir(agenda):
    print("listado completa de la agenda")
    for fecha in agenda:
        print("para la fecha",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)

def consulta_fecha(agenda):
    fecha=input("ingrese la fecha que desea consultar:")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("no hay actividades agendadas para dicha fecha")


agenda=cargar()
imprimir(agenda)
consulta_fecha(agenda)