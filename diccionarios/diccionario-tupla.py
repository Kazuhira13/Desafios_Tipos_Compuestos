def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("ingrese el codigo del producto:"))
        descripcion=input("ingrese la descripcion:")
        precio=float(input("ingrese el precio:"))
        stock=int(input("ingrese el stock actual:"))
        productos[codigo]=(descripcion,precio,stock)
        continua=input("desea cargar otro producto [s/n]")
    return productos

def imprimir(productos):
    print("listado completo de productos")
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])


def consulta(productos):
    codigo=int(input("ingrese el cogido del producto:"))
    if codigo in productos:
        print(productos[codigo][0],productos[codigo][1],productos[codigo][2])


def listado_stock_cero(productos):
    print("listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])


productos=cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)
