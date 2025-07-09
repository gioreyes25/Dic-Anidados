datos= {
    "Electronica": {
        "Celular": {"precio": 300000, "stock": 10},
        "Audífonos": {"precio": 15000, "stock": 25}
    },
    "Ropa": {
        "Polera": {"precio": 8000, "stock": 40},
        "Pantalón": {"precio": 12000, "stock": 15}
    }
}
while True:
    print("1. Agregar producto a una categoría (si la categoría no existe, la crea)")
    print("2. Ver productos por categoría.")
    print("3. Actualizar stock de un producto específico.")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            cate=input("Ingrese categoria a la que desea agregar producto, si no existe se creara: ").title()
            if cate in datos:
                producto=input("Ingrese producto: ").title()
                precio=int(input("Ingrese precio: "))
                stock=int(input("Ingrese stock: "))
                if producto in datos:   
                    datos[cate][producto]={"precio":precio,"stock":stock}
                else:
                    datos[cate][producto]={}
        case 2:
            cate=input("Ingrese categoria a buscar: ").title()
            if cate in datos:
                print(cate)
                for n,i in datos.items():
                    for p,v in i.items():
                        if cate==n:
                            print(f"Producto: {p} Precio: {v["precio"]} Stock: {v["stock"]}")
        case 3:
            produ=input("Ingrese producto a modificar: ").title()
            encontrado=False
            for n,i in datos.items():
                for p,v in i.items():
                    if produ in i:
                        encontrado=True
                        if produ==p:
                            print(f"Producto: {p} Precio: {v["precio"]} Stock: {v["stock"]}")
                            canti=int(input("Ingrese cantidad que desea agregar: "))
                            v["stock"]+=canti
                        
                    
            if not encontrado:
                print("No")
            