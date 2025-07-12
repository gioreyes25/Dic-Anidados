datos= {
    "Ventas": {
        "Ana Perez": {"edad": 30, "puesto": "Gerente", "salario": 55000},
        "Luis Gomez": {"edad": 25, "puesto": "Ejecutivo", "salario": 32000},
        "Maria Diaz": {"edad": 28, "puesto": "Asistente", "salario": 28000}
    },
    "Recursos Humanos": {
        "Carla Ruiz": {"edad": 28, "puesto": "Analista", "salario": 40000},
        "Pedro Soto": {"edad": 35, "puesto": "Jefe", "salario": 60000},
        "Laura Sanchez": {"edad": 32, "puesto": "Coordinadora", "salario": 45000}
    },
    "Tecnologia": {
        "Jorge Ramirez": {"edad": 27, "puesto": "Desarrollador", "salario": 50000},
        "Sandra Lopez": {"edad": 29, "puesto": "Ingeniera de Sistemas", "salario": 52000},
        "Carlos Martinez": {"edad": 31, "puesto": "Administrador de Redes", "salario": 48000}
    }
}
while True:
    print("1. Mostrar Todas Las Areas")
    print("2. Ver Empleados De Un Area X")
    print("3. Buscar Empleado Por Nombre")
    print("4. Ver Salario Promedio Por Area")
    print("5. Agregar Nuevo Empleado")
    print("6. Eliminar Empleado")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in datos.items():
                for p,v in i.items():
                    print(f"Area: {n}|{p}|{v["edad"]}|{v["puesto"]}|{v["salario"]}")
        case 2:
            area=input("Ingrese area: ").lower()
            for n,i in datos.items():
                for p,v in i.items():
                    if area==n.lower():
                        print(f"Area: {n}|{p}|{v["edad"]}|{v["puesto"]}|{v["salario"]}")
        case 3:
            name=input("Ingrese nombre de empleado: ").lower()
            for n,i in datos.items():
                for p,v in i.items():
                    if name==p.lower():
                        print(f"Area: {n}|{p}|{v["edad"]}|{v["puesto"]}|{v["salario"]}")
        case 4:
            for n,i in datos.items():
                total=0
                for p,v in i.items():
                        total+=v["salario"]
                total/=3
                total=round(total)
                print(f"El promedio de {n} es {total}")
        case 5:
            for n,i in datos.items():
                print(n)
            area=input("Ingrese area: ").capitalize()
            for n,i in datos.items():
                if area==n.capitalize():
                    name=input("Ingrese nombre de el empleado: ").capitalize()
                    edad=int(input("Ingrese edad: "))
                    puesto=input("Ingrese puesto: ").capitalize()
                    salario=int(input("Ingrese salario: "))
                    datos[area][name]={"edad":edad,"puesto":puesto,"salario":salario}
        case 6:
            for n,i in datos.items():
                print(n)
            area=input("Ingrese area: ").title()
            for n,i in datos.items():
                for p,v in i.items():
                    if area==n.title():
                        print(p)
            delete=input("Ingrese nombre de el empleado que desea eliminar: ").title()
            e=False
            if delete in datos[area]:
                e=True
                if datos[area][delete]:
                    del datos[area][delete]
                    print(f"Se ha eliminado el empleado {delete}")
                else:
                    print("Empleado no existe")
            if not e:
                print("No existe area")