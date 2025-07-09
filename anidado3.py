datos = {
    "Ventas": {
        "maria": {"edad": 30, "sueldo": 800000, "antiguedad": 5},
        "juan": {"edad": 27, "sueldo": 750000, "antiguedad": 2},
        "sofia": {"edad": 25, "sueldo": 700000, "antiguedad": 3}
    },
    "Informatica": {
        "carlos": {"edad": 35, "sueldo": 1200000, "antiguedad": 7},
        "ana": {"edad": 29, "sueldo": 1000000, "antiguedad": 4},
        "pedro": {"edad": 31, "sueldo": 1100000, "antiguedad": 6}
    },
    "Recursos Humanos": {
        "lucia": {"edad": 40, "sueldo": 950000, "antiguedad": 10},
        "diego": {"edad": 38, "sueldo": 900000, "antiguedad": 8},
        "laura": {"edad": 33, "sueldo": 850000, "antiguedad": 5}
    }
}
while True:
    print(datos)
    print("1. Agregar Empleado")
    print("2. Listar Empleados Por Departamento")
    print("3. Buscar Empleado Por Nombre")
    print("4. Mostrar Empleados Con mas de 5 años de antiguedad")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            name=input("Ingrese nombre de el empleado: ").title()
            for n,i in datos.items():
                print(n)
            area=input("Ingrese area: ").title()
            edad=input("Ingrese edad de el empleado: ")
            sueldo=int(input("Ingrese sueldo: "))
            if area in datos:
                datos[area][name]={"edad":edad,"sueldo":sueldo}
            else:
                datos[area]={}
                datos[area][name]={"edad":edad,"sueldo":sueldo}
        case 2:
            cate=input("Ingrese departmaneto a filtrar: ").title()
            if cate in datos:
                for n,i in datos.items():
                    for p,v in i.items():
                        if cate==n:
                            print(f"Nombre: {p} {v["edad"]} {v["sueldo"]}")
        case 3:
            name=input("Ingrese nombre de empleado a buscar: ")
            encontardo=False
            for n,i in datos.items():
                for p,v in i.items():
                    if name==p:
                        encontardo=True
                        print(f"Area: {n}")
                        print(f"Nombre: {p} {v["edad"]} {v["sueldo"]}")
            if not encontardo:
                print("No existe ese empleado")
        case 4:
            for n,i in datos.items():
                for p,v in i.items():
                    if v["antiguedad"]>=5:
                            print(f"Area: {n} Nombre: {p} {v["edad"]} {v["sueldo"]}")