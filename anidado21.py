datos= {
    "Juan Perez": {
        "info": {"edad": 30, "email": "juanperez@mail.com"},
        "prestamos": {
            "B001": {"titulo": "1984", "fecha_prestamo": "01-07-2025", "fecha_devolucion": None},
            "B002": {"titulo": "El Principito", "fecha_prestamo": "15-06-2025", "fecha_devolucion": "01-07-2025"}
        }
    },
    "Maria Lopez": {
        "info": {"edad": 25, "email": "marialopez@mail.com"},
        "prestamos": {
            "B003": {"titulo": "Cien anos de soledad", "fecha_prestamo": "05-07-2025", "fecha_devolucion": None}
        }
    }
}
while True:
    print("1. Mostrar Usuarios ")
    print("2. Ver Libros Prestados Por usuario")
    print("3. Agregar Prestamo a un usuario")
    print("4. Registrar Fecha de devolucion")
    print("5. Mostrar Libros Prestados")
    print("6. Buscar que usuario tiene x libro por codigo")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in datos.items():
                for c,l in i["prestamos"].items():
                    print(f"{n}|Edad: {i["info"]["edad"]}|Email: {i["info"]["email"]}|{c}|{l["titulo"]}|{l["fecha_prestamo"]}|{l["fecha_devolucion"]}")
        case 2:
            usu=input("Ingrese usuario: ").title()
            if usu in datos:
                for n,i in datos.items():
                    for c,l in i["prestamos"].items():
                        if usu==n:
                            print(f"{n}|{c}|{l["titulo"]}|{l["fecha_prestamo"]}|{l["fecha_devolucion"]}")
        case 3:
            usuario=input("Ingrese usuario: ")
            if usuario in datos:
                codigo=input("Ingrese codigo: ").upper()
                titulo=input("Ingrese titulo: ")
                fecha1=input("Ingrese fecha de prestamo: ")
                datos[usuario]["prestamos"][codigo]={"titulo":titulo,"fecha_prestamo":fecha1,"fecha_devolucion":None}
        case 4:
            codigo=input("Ingrese codigo: ").upper()
            for n,i in datos.items():
                for c,l in i["prestamos"].items():
                    if codigo==c:
                        if l["fecha_devolucion"]==None:
                            print(f"{c}|{l["titulo"]}|{l["fecha_prestamo"]}|{l["fecha_devolucion"]}")
                            fecha=input("Ingrese fecha devolucion: ")
                            datos[n]["prestamos"][codigo]["fecha_devolucion"]=fecha
                            print("Se ha devuelto libro con exito")
        case 5:
            for n,i in datos.items():
                for c,l in i["prestamos"].items():
                    if l["fecha_devolucion"]==None:
                        print(f"{n}|{c}|{l["titulo"]}|{l["fecha_prestamo"]}|{l["fecha_devolucion"]}")
        case 6:
            codigo=input("Ingrese codigo para buscar Libro: ").upper()
            for n,i in datos.items():
                for c,l in i["prestamos"].items():
                    if codigo==c:
                        print(f"{n}|{c}|{l["titulo"]}|{l["fecha_prestamo"]}|{l["fecha_devolucion"]}")