datos= {
    "accion": {
        "call of duty": {"anio": 2019, "jugadores": 500000, "calificacion": 8.7},
        "doom eternal": {"anio": 2020, "jugadores": 200000, "calificacion": 9.1},
        "fortnite": {"anio": 2017, "jugadores": 1000000, "calificacion": 8.0}
    },
    "aventura": {
        "zelda breath of the wild": {"anio": 2017, "jugadores": 300000, "calificacion": 9.8},
        "uncharted 4": {"anio": 2016, "jugadores": 250000, "calificacion": 9.0},
        "assassin's creed odyssey": {"anio": 2018, "jugadores": 280000, "calificacion": 8.5}
    },
    "deportes": {
        "fifa 23": {"anio": 2022, "jugadores": 900000, "calificacion": 7.9},
        "nba 2k22": {"anio": 2021, "jugadores": 400000, "calificacion": 8.1},
        "rocket league": {"anio": 2015, "jugadores": 600000, "calificacion": 8.6}
    }
}
while True:
    print("1. Ver Juegos Por Jugadores Activos")
    print("2. Ver Juegos Con Calificacion >9.0")
    print("3. Ver promedio de calificacion por cateoria")
    print("4. Ver Juegos Lanzados Por Rango De Años")
    print("5. Ver Juegos Mas Antiguo")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["jugadores"],reverse=True)
            for n,p,v in ordenados:
                print(f"Categoria: {n}|Juego: {p}|Año: {v["anio"]}| Jugadores: {v["jugadores"]}")
        case 2:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["calificacion"],reverse=True)
            for n,p,v in ordenados:
                if v["calificacion"]>=9.0:
                    print(f"Categoria: {n}|Juego: {p}|Año: {v["anio"]}| Jugadores: {v["jugadores"]}|Calificacion: {v["calificacion"]}")
        case 3:
            for n,i in datos.items():
                pro=0
                for p,v in i.items():
                    pro+=v["calificacion"]
                pro/=3
                pro=round(pro,1)
                print(f"{n} Calificacion: {pro}")
        case 4:
            todos=[]
            n1=int(input("Ingrese año min: "))
            n2=int(input("Ingrese año max: "))
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["anio"],reverse=True)
            for n,p,v in ordenados:
                if n1 <= int(v["anio"]) <=n2:
                    print(f"Categoria: {n}|Juego: {p}|Año: {v["anio"]}| Jugadores: {v["jugadores"]}|Calificacion: {v["calificacion"]}")
        case 5:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            mayor=min(todos,key= lambda x:x[2]["anio"])
            print(mayor)
            print(f"{mayor[1]},{mayor[0]} es el juego mas antiguo {mayor[2]["anio"]}")
