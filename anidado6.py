datos= {
    "Norte": {
        "ignacio": {"ventas": 1500000, "clientes": 35, "region": "norte"},
        "catalina": {"ventas": 1800000, "clientes": 40, "region": "norte"},
        "daniel": {"ventas": 1300000, "clientes": 28, "region": "norte"},
        "sofia": {"ventas": 1650000, "clientes": 33, "region": "norte"}
    },
    "Centro": {
        "valentina": {"ventas": 2000000, "clientes": 50, "region": "centro"},
        "zebastian": {"ventas": 1700000, "clientes": 38, "region": "centro"},
        "matias": {"ventas": 1600000, "clientes": 36, "region": "centro"},
        "camila": {"ventas": 1900000, "clientes": 42, "region": "centro"}
    },
    "Sur": {
        "fernando": {"ventas": 1200000, "clientes": 30, "region": "sur"},
        "camila s": {"ventas": 1550000, "clientes": 32, "region": "sur"},
        "julian": {"ventas": 1400000, "clientes": 29, "region": "sur"},
        "martina": {"ventas": 1600000, "clientes": 34, "region": "sur"}
    }
}
total={}
if not total:
    gana=0
    for n,i in datos.items():
        for p,v in i.items():
            if n:
                gana+=v["ventas"]
        total[n]={"total":0}
        total[n]["total"]+=gana
        gana=0
while True:
    print(total)
    print("1. Mostrar Vendedores de mayor a menor (ventas)")
    print("2. Mostrar El Promedio de ventas por sucursal")
    print("3. Filtrar Vendedores por clientes Atendidos")
    print("4. Mostrar El Mejor Vendedor")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["ventas"],reverse=True)
            for n,p,v in ordenados:
                print(f"Sucursal: {n}|Vendedor: {p}|Ventas Totales: {v["ventas"]}|Clientes Atendidos: {v["clientes"]}")
        case 2:
            for n,i in total.items():
                print(f"{n} = {i["total"]}")
        case 3:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["clientes"],reverse=True)
            for n,p,v in ordenados:
                print(f"Sucursal: {n}|Vendedor: {p}|Ventas Totales: {v["ventas"]}|Clientes Atendidos: {v["clientes"]}")
        case 4:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            mayor=max(todos,key= lambda x:x[2]["ventas"])
            print(f"El vendedor con mas ventas es {mayor[1]} {mayor[2]["ventas"]}")