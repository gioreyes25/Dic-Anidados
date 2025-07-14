vuelos = [
    ["FL001", "Santiago", "Lima", [
        ["Ana Torres", 28, "12A"],
        ["Luis Rojas", 35, "14C"]
    ]],
    ["FL002", "Buenos Aires", "Madrid", [
        ["Carlos Mena", 40, "3B"],
        ["Sofia Rivas", 22, "5A"]
    ]],
    ["FL003", "Bogota", "Miami", [
        ["Diego Soto", 31, "7F"]
    ]]
]
while True:
    print("1. Ver Vuelos")
    print("2. Ver Pasajeros de x vuelo")
    print("3. Buscar pasajero por nombre")
    print("4. Agregar Pasajero a x vuelo")
    print("5. Eliminar Pasajero Por Nombre")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for i in vuelos:
                print(f"Vuelo: {i[0]}|{i[1]}-{i[2]}")
                for v in i[3]:
                    print(f"{v[0]}|Edad: {v[1]}|Asiento: {v[2]}")
        case 2:
            vuelo=input("Ingrese codigo de vuelo: ").upper()
            for i in vuelos:
                if vuelo==i[0]:
                    for v in i[3]:
                        print(f"{v[0]}|Edad: {v[1]}|Asiento: {v[2]}")
        case 3:
            name=input("ingrese nombre de pasajero: ").title()
            for i in vuelos:
                for v in i[3]:
                    if name==v[0]:
                        print(f"Vuelo: {i[0]}|{i[1]}-{i[2]}")
                        print(f"{v[0]}|Edad: {v[1]}|Asiento: {v[2]}")
        case 4:
            si=False
            codigo=input("Ingrese codigo del vuelo: ").upper()
            for i in vuelos:
                if codigo==i[0]:
                    nombre=input("Ingrese nombre de pasajero: ").title()
                    edad=int(input("Ingrese edad: "))
                    asiento=input("Ingrese asiento: ").upper()
                    for v in i[3]:
                        if asiento not in v[2]:
                            si=True
                            i[3].append([nombre,edad,asiento])
                            print("Pasajeor registrado exitosamennte")
                            break
                        else:
                            print("ASIENTO SE ENCUENTRA OCUPADO")
                            break
        case 5:
            name=input("Ingrese nombre de pasajero a eliminar: ").title()
            for i in vuelos:
                for v,pa in enumerate(i[3]):
                    print(v)
                    if pa[0]==name:
                        del i[3][v]