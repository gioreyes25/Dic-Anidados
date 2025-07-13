datos= {
    "Ingenieria": {
        "Informatica": {
            "Programacion I": "Prof. Lopez",
            "Base De Datos": "Prof. Gomez"
        },
        "Civil": {
            "Estatica": "Prof. Rivas",
            "Materiales": "Prof. Soto"
        }
    },
    "Salud": {
        "Medicina": {
            "Biologia General": "Dra. Contreras",
            "Anatomia": "Dr. Morales"
        },
        "Enfermeria": {
            "Fundamentos De Enfermeria": "Dra. Lagos",
            "Farmacologia": "Dr. Ruiz"
        }
    }
}
while True:
    print("1. Ver Todas Las Facultades")
    print("2. Ver carreras por facu")
    print("3. Ver Carrera Y Sus Datos")
    print("4. Agregar Nuevo Curso a una carrera existente")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in datos.items():
                for p,v in i.items():
                    for a,k in v.items():
                        print(f"{n}|{p}|{a}|{k}")
        case 2:
            facu=input("Ingrese facultad que desea ver: ").capitalize()
            for n,i in datos.items():
                if facu==n.capitalize():
                    for p,v in i.items():
                        for a,k in v.items():
                            print(f"{n}|{p}|{a}|{k}")
        case 3:
            carre=input("Ingrese carrera: ").capitalize()
            for n,i in datos.items():
                for p,v in i.items():
                    for a,k in v.items():
                        if carre==p.capitalize():
                            print(f"{n}|{p}|{a}|{k}")
        case 4:
            for n,i in datos.items():
                print(n)
            facu=input("Ingrese facultad: ").capitalize()
            for n,i in datos.items():
                if facu==n.capitalize():
                    for p,v in i.items():
                        print(p)
                    carre=input("Ingrese la carrera: ").capitalize()
                    for p,v in i.items():
                        if carre==p.capitalize():
                            curso=input("Ingrese Curso: ").capitalize()
                            profe=input("Ingrese profesor: ").capitalize()
                            datos[facu][carre][curso]=profe