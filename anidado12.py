datos = {
    "drama": {
        "la vida es bella":    {"anio": 1997, "duracion": 116, "rating": 8.6, "views": 1200000},
        "the crown":           {"anio": 2016, "duracion": 60,  "rating": 8.7, "views": 900000},
        "breaking bad":        {"anio": 2008, "duracion": 47,  "rating": 9.5, "views": 2300000}
    },
    "comedia": {
        "friends":             {"anio": 1994, "duracion": 22,  "rating": 8.9, "views": 2500000},
        "the office":          {"anio": 2005, "duracion": 22,  "rating": 8.8, "views": 2100000},
        "parks and rec":       {"anio": 2009, "duracion": 22,  "rating": 8.6, "views": 1300000}
    },
    "ciencia ficcion": {
        "black mirror":        {"anio": 2011, "duracion": 60,  "rating": 8.8, "views": 1100000},
        "stranger things":     {"anio": 2016, "duracion": 50,  "rating": 8.7, "views": 2000000},
        "westworld":           {"anio": 2016, "duracion": 60,  "rating": 8.6, "views": 800000}
    }
}
while True:
    print("1. Ver Peliculas Por Genero")
    print("2. Ver Top 3 peliculas mejor vistas")
    print("3. Ver Peliculas con rating >9.0")
    print("4. Ver Promedio de duracion de cada genero")
    print("5. Buscar Pelicula")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in datos.items():
                print(n)
            buscar=input("Ingrese genero de pelicula: ")
            encontrado=False
            for n,i in datos.items():
                for p,v in i.items():
                    if buscar==n:
                        encontrado=True
                        print(f"Pelicula: {p}|Año: {v["anio"]}|Duracion: {v["duracion"]}|Rating: {v["rating"]}|Views: {v["views"]}")
            if not encontrado:
                print("No hay coincidencias")
        case 2:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            orden=sorted(todos,key= lambda x:x[2]["views"],reverse=True)[:3]
            for n,p,v in orden:
                print(f"Genero: {n}|Pelicula: {p}|Views: {v["views"]}")
        case 3:
            for n,i in datos.items():
                for p,v in i.items():
                    if v["rating"]>=9.0:
                        print(f"Pelicula: {p}|Año: {v["anio"]}|Duracion: {v["duracion"]}|Rating: {v["rating"]}|Views: {v["views"]}")
        case 4:
            for n,i in datos.items():
                pro=0
                for p,v in i.items():
                    pro+=v["duracion"]
                pro/=3
                pro=round(pro,1)
                print(f"{n} {pro}")
        case 5:
            peli=input("Ingrese peliocula a buscar: ")
            encontrado=False
            for n,i in datos.items():
                for p,v in i.items():
                    if peli==p:
                        encontrado=True
                        print(f"Pelicula: {p}|Año: {v["anio"]}|Duracion: {v["duracion"]}|Rating: {v["rating"]}|Views: {v["views"]}")
            if not encontrado:
                print("No hay coincidencias")