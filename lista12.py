datos = [
    ["Aeropuerto Santiago", [
        ["LA123", "Buenos Aires", "LATAM", "En Horario"],
        ["SK456", "Lima", "Sky", "Retrasado"]
    ]],
    ["Aeropuerto Concepción", [
        ["JA789", "Antofagasta", "JetSmart", "En Horario"]
    ]],
    ["Aeropuerto Iquique", [
        ["LA999", "Santiago", "LATAM", "Cancelado"],
        ["JA101", "Arica", "JetSmart", "En Horario"]
    ]]
]
estado=["En Horario","Cancelado","Retrasado"]
while True:
    print("1. Ver Vuelos")
    print("2. Buscar vuelo por numero")
    print("3. Agregar vuelo a aeropuerto")
    print("4. Cambiar Estado de vuelo")
    print("5. Eiminar Vuelo")
    print("6. Mostrar Vuelos Totales")
    op=int(input("Ingerse una opcion: "))
    match op:
        case 1:
            for n in datos:
                print(n[0])
                for i in n[1]:
                    print(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}")
        case 2:
            num=input("Ingres numero de vuelo: ").lower()
            for n in datos:
                for i in n[1]:
                    if num==i[0].lower():
                        print(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}")
        case 3:
            aero=input("Ingrese aeropuerto: ").lower()
            for n in datos:
                if aero==n[0].lower():
                    codigo=input("Ingrese numero de vuelo: ").upper()
                    destino=input("Ingrese destino donde volara: ").title()
                    empresa=input("Ingrese empresa de avion: ").capitalize()
                    for r in estado:
                        print(r)
                    estado=input("Ingrese estado de vuelo: ").title()
                    if estado in estado:
                        n[1].append([codigo,destino,empresa,estado])
                    else:
                        print("Estado ingresado mal")
        case 4:
            codi=input("Ingrese codigo de un vuelo: ").lower()
            for n in datos:
                for i in n[1]:
                    if codi==i[0].lower():
                        print(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}")
                        for r in estado:
                            if i[3] in r:
                                estado.remove(i[3])
                        for r in estado:
                            print(r)
                        estadonew=input("Ingrese nuevo estado: ").title()
                        if estadonew in estado:
                            i[3]=estadonew
                            print("Se ha actualiado el estado")
                        else:
                            print("Mal, Ingrese estados que se le muestran en pantalla")
        case 5:
            codi=input("Ingrese codigo de vuelo: ").lower()
            for n in datos:
                for v,i in enumerate(n[1]):
                    if codi==i[0].lower():
                        del n[1][v]
                        print(f"Se ha eliminado el vuelo {i[0]}|{i[1]}|{i[2]}|{i[3]}")    
        case 6:
            for n in datos:
                for i in n[1]:
                    r=len(n[1])
                    print(f"-{i[3]}")
                print(f"{n[0]} Vuelos: {r}")