ventas = [
    {
        "fecha": "10-07-2025",
        "productos": {
            "Teclado": {"cantidad": 4, "precio_unitario": 25000},
            "Mouse": {"cantidad": 6, "precio_unitario": 12000}
        }
    },
    {
        "fecha": "11-07-2025",
        "productos": {
            "Monitor": {"cantidad": 2, "precio_unitario": 150000},
            "Mouse": {"cantidad": 3, "precio_unitario": 12000}
        }
    },
    {
        "fecha": "12-07-2025",
        "productos": {
            "Notebook": {"cantidad": 1, "precio_unitario": 500000},
            "Teclado": {"cantidad": 2, "precio_unitario": 25000}
        }
    }
]
while True:
    print("1. Ver todas las ventas por día")
    print("2. Ver Ventas De X Producto")
    print("3. Ver Ventas Por Fecha")
    print("4. Agregar Nuevo Producto a una fecha")
    op=int(input("Ingerse una opcion: "))
    match op:
        case 1:
            for n in ventas:
                for p,v in n["productos"].items():
                    print(f"{n["fecha"]}|{p}|{v["cantidad"]}|{v["precio_unitario"]}")
        case 2:
            produ=input("Ingrese produot que desea buscar: ").title()
            for n in ventas:
                for p,v in n["productos"].items():
                    if produ==p:
                        print(f"{n["fecha"]}|{p}|{v["cantidad"]}|{v["precio_unitario"]}")
        case 3:
            for n in ventas:
                print(f"En la fecha {n['fecha']}")
                t=0
                for p,v in n["productos"].items():
                    t+=v["cantidad"]*v["precio_unitario"]
                print(f"Total: {t}")
        case 4:
            fecha=input("Ingrese fecha: ")
            produ=input("Ingrese producto: ").title()
            canti=int(input("Ingrese cantidad: "))
            precio=int(input("Ingrese precio: "))
            for n in ventas:
                if fecha==n["fecha"]:
                    n["productos"][produ]={"cantidad":canti,"precio_unitario":precio}

                        