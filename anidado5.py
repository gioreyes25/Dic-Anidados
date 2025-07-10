datos = {
    "rojos": {
        "matias": {"edad": 22, "goles": 5, "partidos": 10},
        "tomas": {"edad": 24, "goles": 3, "partidos": 9},
        "lucas": {"edad": 21, "goles": 6, "partidos": 11}
    },
    "azules": {
        "sebastian": {"edad": 25, "goles": 4, "partidos": 8},
        "diego": {"edad": 23, "goles": 7, "partidos": 12},
        "javier": {"edad": 22, "goles": 2, "partidos": 6}
    },
    "verdes": {
        "cristian": {"edad": 26, "goles": 8, "partidos": 13},
        "martin": {"edad": 24, "goles": 1, "partidos": 7},
        "agustin": {"edad": 23, "goles": 4, "partidos": 10}
    }
}
while True:
    print("1. Ver Jugador Por Equipo")
    print("2. Mostrar Los mas goleadores")
    print("3. Ver jugadores que hayan jugado mas de 10p")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            team=input("Ingrese un equipo: ")
            for n,i in datos.items():
                for p,v in i.items():
                    if team==n:
                        print(f"Jugador: {p}|Edad: {v["edad"]}|Goles: {v["goles"]}|Partidos: {v["partidos"]}")
        case 2:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["goles"],reverse=True)
            for n,p,v in ordenados:
                print(f"Equipo: {n}|Jugador: {p}|Goles Anotados: {v["goles"]}|Partidos: {v["partidos"]}")
        case 3:
            for n,i in datos.items():
                for p,v in i.items():
                    if v["partidos"]>=10:
                        print(f"Equipo: {n}|Jugador: {p}|Goles Anotados: {v["goles"]}|Partidos: {v["partidos"]}")