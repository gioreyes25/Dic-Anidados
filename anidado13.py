datos = {
    "juan perez": {
        "pedido_001": {"fecha": "2025-06-01", "monto": 120000, "articulos": ["camiseta", "gorro"]},
        "pedido_002": {"fecha": "2025-06-15", "monto":  75000, "articulos": ["pantalon"]},
        "pedido_003": {"fecha": "2025-07-02", "monto": 200000, "articulos": ["chaqueta", "camiseta", "calcetines"]}
    },
    "ana gonzalez": {
        "pedido_004": {"fecha": "2025-05-20", "monto":  50000, "articulos": ["bufanda"]},
        "pedido_005": {"fecha": "2025-06-30", "monto": 180000, "articulos": ["abrigo", "guantes"]}
    },
    "luis ramirez": {
        "pedido_006": {"fecha": "2025-04-25", "monto":  90000, "articulos": ["zapatos"]},
        "pedido_007": {"fecha": "2025-02-01", "monto": 110000, "articulos": ["bolso", "gorro"]},
        "pedido_008": {"fecha": "2025-07-03", "monto":  60000, "articulos": ["camiseta"]}
    }
}
while True:
    print("1. Ver pedidos de un cliente especifico")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            name=input("Ingrese nombre de cliente: ")
            e=False
            for n,i in datos.items():
                for p,v in i.items():
                    if name==n:
                        e=True
                        todos.append((n,p,v))
            orden=sorted(todos,key= lambda x:x[2]["fecha"])
            for n,p,v in orden:
                print(f"{n}|{p}|{v["fecha"]}|{",".join(v["articulos"])}")
        case 2:
            total=[]
            for n,i in datos.items():
                t=0
                for p,v in i.items():
                    t+=v["monto"]
                total.append((n,t))
            orden=sorted(total,key= lambda x:x[1],reverse=True)
            for i,(n,t) in enumerate(orden,start=1):
                print(f"{i}-Cliente: {n}| Gasto Total: {t}")                                            
        case 3:
            for n,i in datos.items():
                t=0
                for p,v in i.items():
                    t+=v["monto"]
                t/=3
                t=round(t)
                print(f"{n}|Ticket Promedio: {t}")
        case 4:
            b=input("Ingrese articulo: ")
            for n,i in datos.items():
                for p,v in i.items():
                    if b in v["articulos"]:
                        print(f"{n}|{p}|{v['fecha']}|{" ".join(v['articulos'])}")