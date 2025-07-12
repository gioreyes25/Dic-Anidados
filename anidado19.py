datos = {
    "Carlos": {
        "P001": {"producto": "Teclado", "cantidad": 1, "precio_unitario": 25000, "estado": "pendiente"},
        "P002": {"producto": "Mouse", "cantidad": 2, "precio_unitario": 12000, "estado": "entregado"},
        "P003": {"producto": "Audifonos", "cantidad": 1, "precio_unitario": 18000, "estado": "enviado"},
        "P004": {"producto": "USB 32GB", "cantidad": 3, "precio_unitario": 6000, "estado": "pendiente"}
    },
    "Lucia": {
        "P005": {"producto": "Monitor", "cantidad": 1, "precio_unitario": 150000, "estado": "enviado"},
        "P006": {"producto": "Cable HDMI", "cantidad": 2, "precio_unitario": 8000, "estado": "pendiente"},
        "P007": {"producto": "Mousepad", "cantidad": 1, "precio_unitario": 5000, "estado": "entregado"},
        "P008": {"producto": "Parlantes", "cantidad": 1, "precio_unitario": 25000, "estado": "pendiente"}
    },
    "Pedro": {
        "P009": {"producto": "Notebook", "cantidad": 1, "precio_unitario": 450000, "estado": "pendiente"},
        "P010": {"producto": "SSD 1TB", "cantidad": 1, "precio_unitario": 85000, "estado": "enviado"}
    }
}
while True:
    print("1. Ver Pedidos De Clientes")
    print("2. Ver Pedidos De X Cliente")
    print("3. Ver Gasto Total Por Cliente")
    print("4. Ver Pedidos Con Estado Pendiente")
    print("5. Cambiar Estado De Pedido Por ID")
    print("6. Agregar Nuevo Pedido A Cliente")
    print("7. Eliminar Pedido Por ID")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in datos.items():
                print(f"Pedidos De {n}")
                for p,v in i.items():
                    print(f"{p}|{v["producto"]}|Cantidad: {v["cantidad"]}|Precio u {v["precio_unitario"]}|Estado: {v["estado"]}")
        case 2:
            cli=input("Ingrese nombre de cliente: ").capitalize()
            for n,i in datos.items():
                if cli==n:
                    print(f"Pedidos De {n}")
                    for p,v in i.items():
                        print(f"{p}|{v["producto"]}|Cantidad: {v["cantidad"]}|Precio u {v["precio_unitario"]}|Estado: {v["estado"]}")
        case 3:
            for n,i in datos.items():
                t=0
                for p,v in i.items():
                    t+=v["cantidad"]*v["precio_unitario"]
                print(f"La cantidad gastada de {n} es ${t}")
        case 4:
            for n,i in datos.items():
                print(f"Pedidos De {n}")
                for p,v in i.items():
                    if v["estado"]=="pendiente":
                        print(f"{p}|{v["producto"]}|Cantidad: {v["cantidad"]}|Precio u {v["precio_unitario"]}|Estado: {v["estado"]}")
        case 5:
            si=False
            palabra=["pendiente","entregado","enviado"]
            for n,i in datos.items():
                print(f"Pedidos De {n}")
                for p,v in i.items():
                    print(f"{p}|{v["producto"]}|Cantidad: {v["cantidad"]}|Precio u {v["precio_unitario"]}|Estado: {v["estado"]}")
            id=input("Ingrese ID de pedido que desea cambiar estado: ").upper()
            for n,i in datos.items():
                for p,v in i.items():
                    if id==p:
                        if v["estado"] in palabra:
                            palabra.remove(v["estado"])
                            for r in palabra:
                                print(r)
                            estadonew=input("Ingrese estado nuevo: ")
                            for r in palabra:
                                if estadonew ==r:
                                    si=True
                                    datos[n][id]["estado"]=estadonew
                                    print("Se ha actualizado Correctamente")
                            if not si:
                                print("Ingreso incorrectamente el estado")
        case 6:
            palabra=["pendiente","entregado","enviado"]
            for n,i in datos.items():
                print(n)
            cli=input("Ingrese cliente al que agregara pedido: ").capitalize()
            for n,i in datos.items():
                if cli==n:
                    id=input("Ingrese codigo de 4 digitos exactos")
                    if id not in datos[n]:
                        if len(id)==4:
                            producto=input("Ingrese producto: ")
                            canti=int(input("Ingrese cantidad: "))
                            precio=int(input("Ingrese precio unitario: "))
                            for r in palabra:
                                print(r)
                            estado=input("Ingrese estado:")
                            for r in palabra:
                                if estado in r:
                                    datos[cli][id]={"producto":producto,"cantidad":canti,"precio_unitario":precio,"estado":estado}
                    else:
                        print("Codigo ya se encuentra usado por otro pedido")
        case 7:
            for n,i in datos.items():
                print(n)
            name=input("Ingrese nombre de cliente: ").capitalize()
            for n,i in datos.items():
                for p,v in i.items():
                    if name==n:
                        print(f"{p}|{v["producto"]}|Cantidad: {v["cantidad"]}|Precio u {v["precio_unitario"]}|Estado: {v["estado"]}")
            id=input("Ingrese ID para eliminar pedido: ").upper()
            del datos[name][id]
            print(f"Se ha eliminado el pedido {id}")