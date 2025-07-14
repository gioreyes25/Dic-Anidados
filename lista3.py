inventario = [
    ["Electronica", [
        ["Notebook", 5, 700000],
        ["Mouse", 20, 10000],
        ["Monitor", 8, 150000]
    ]],
    ["Ropa", [
        ["Polera", 30, 12000],
        ["Pantalon", 15, 25000],
        ["Zapatillas", 10, 45000]
    ]],
    ["Alimentos", [
        ["Leche", 50, 1200],
        ["Pan", 100, 800],
        ["Arroz", 40, 1500]
    ]]
]
while True:
    print("1. Ver Productos")
    print("2. Buscar Producto Por Nombre")
    print("3. Ver STock de categorias")
    print("4. Agregar Producto a x categoria")
    print("5. Eliminar Producto de categoria")
    op=int(input("Ingrese opcion: "))
    match op:
        case 1:
            for i in inventario:
                print(f"Seccion de {i[0]}")
                for p in i[1]:
                    print(f"{p[0]}|Stock: {p[1]}|Precio: {p[2]}")
        case 2:
            name=input("Ingrese producto: ").title()
            for i in inventario:
                for p in i[1]:
                    if name==p[0]:
                        print(f"{p[0]}|Stock: {p[1]}|Precio: {p[2]}")
        case 3:
            for i in inventario:
                t=0
                for v in i[1]:
                    t+=v[1]
                print(f"Stock de {i[0]} {t}")
        case 4:
            cate=input("Ingrese categoria: ").title()
            producto=input("Ingrese producto: ")
            stock=int(input("Ingrese cantidad: "))
            precio=int(input("Ingrese precio: "))
            for i in inventario:
                if cate==i[0]:
                    i[1].append([producto,stock,precio])
        case 5:
            name=input("Ingrese producto que desea eliminar: ").title()
            for i in inventario:
                for p,pro in enumerate(i[1]):
                    if name==pro[0]:
                        del i[1][p]
                        print("Se ha eliminado con exito el producto")
        case 6:
            produ=input("Ingresr producto que desea modificar: ")
            for i in inventario:
                for p in i[1]:
                    if produ==p[0]:
                        print("1. Stock")
                        print("2. Precio")
                        op=int(input("Ingrese que desea modificar: "))
                        if op==1:
                            stocknew=int(input("Ingrese la cantidad que d4esea agregar: "))
                            p[1]+=stocknew
                            print("Se ha actualizado el stock con exito")
                        else:
                            precionew=int(input("Ingrese el precio nuevo: "))
                            p[2]=precionew
                            print("Se ha actualizado el prcio con exito")
                