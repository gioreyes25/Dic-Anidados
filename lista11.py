datos = [
    ["Donde Carlitos", [
        ["Ana", "Lomo a lo pobre", 8500],
        ["Luis", "Empanadas", 4000]
    ]],
    ["La Picá de la Abuela", [
        ["Camila", "Porotos con riendas", 5000],
        ["Carlos", "Pastel de choclo", 6000]
    ]],
    ["Sushi Express", [
        ["Pedro", "Sushi 12 piezas", 7500],
        ["Sofía", "Ramen", 6500]
    ]]
]
while True:
    print("1. Ver Restaurantes")
    print("2. Ver Pedidos Por Cliente")
    print("3. Agregar Nuevo Pedido A Restaurante")
    print("4. Eliminar Pedido Por Cliente")
    print("5. Ver Ingresos Por Restaurnate")
    print("6. Ver Total De Pedidos Realizados")
    op=int(input("Ingrese una op: "))
    match op:
        case 1:
            for n in datos:
                print(n[0])
                for i in n[1]:
                    print(f"{i[0]}|{i[1]}|${i[2]}")
        case 2:
            cli=input("Ingrese nombre de cliente: ").lower()
            for n in datos:
                for i in n[1]:
                    if cli==i[0].lower():
                        print(f"{i[0]}|{i[1]}|${i[2]}")
        case 3:
            res=input("Ingrese restaurante: ").lower()
            for n in datos:
                if res==n[0].lower():
                    name=input("Ingrese nombre de cliente: ").title()
                    plato=input("Ingrese plato: ").title()
                    precio=int(input("Ingrese precio de el plato: "))
                    n[1].append([name,plato,precio])
        case 4:
            r=False
            ingrese=input("Ingrese restaurante: ").lower()
            for n in datos:
                if ingrese==n[0].lower():
                    cliente=input("Ingerse nombre: ").lower()
                    for v,i in enumerate(n[1]):
                        if cliente==i[0].lower():
                            r=True
                            del n[1][v]
                            print(f"Se ha eliminado el pedido {i[0]}|{i[1]}|{i[2]}")
            if not r:
                print("No hay coicnidencias de cliente")
        case 5:
            for n in datos:
                t=0
                for i in n[1]:
                    t+=i[2]
                print(f"{n[0]} Ingreso: {t}")
        case 6:
            t=0
            for n in datos:
                for i in n[1]:
                    c=len(n[1])
                print(f"{n[0]} Clientes Atendidos: {c}")
                t+=c
            print(f"Clientes Totales {t}")
                    
                            
                    
                    