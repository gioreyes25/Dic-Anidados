datos= [
    ["Sala 1", [
        ["Duna 2", "Ciencia Ficcion", 165, 45],
        ["Intensamente 2", "Animacion", 100, 60]
    ]],
    ["Sala 2", [
        ["Joker", "Drama", 122, 35],
        ["The Batman", "Accion", 175, 40]
    ]],
    ["Sala 3", [
        ["Avengers: Endgame", "Accion", 181, 25],
        ["Parasite", "Suspenso", 132, 30]
    ]]
]
while True:
    print("1. Ver Peliculas")
    print("2. Buscar Pelicula Por Nombre")
    print("3. Ver Peliculas Por Genero")
    print("4. Vender Boletos")
    print("5. Agregar Pelicula A x Sala")
    print("6. Eliminar Pelicula Por Nombre")
    print("7. Ver Duracion De Pelis Por Sala")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n in datos:
                print(n[0])
                for i in n[1]:
                    print(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}")
        case 2:
            name=input("Ingrese pelicula que desea buscar: ").lower()
            for n in datos:
                for i in n[1]:
                    if name==i[0].lower():
                        print(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}")
        case 3:
            genero=input("Ingrese genero a buscar: ").lower()
            for n in datos:
                for i in n[1]:
                    if genero==i[1].lower():
                        print(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}")
        case 4:
            for n in datos:
                for i in n[1]:
                    print(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}")
            peli=input("Ingrese pelicula que desea comprar: ").lower()
            for n in datos:
                for i in n[1]:
                    if peli==i[0].lower():
                        print(f"\nPelicula Elegida")
                        print(f"{i[0]}|{i[1]}|{i[2]}|{i[3]}")
                        cantidad=int(input("Ingrese cantidad que desea comprar: "))
                        i[3]-=cantidad
                        print(f"Se han comprado {cantidad} con exito")
        case 5:
            sala=input("Ingrese sala: ").lower()
            for n in datos:
                if sala==n[0].lower():
                    pelicula=input("Ingrese pelicula: ").title()
                    genero=input("Ingrese genero: ")
                    dura=int(input("Ingrese duracionde la misma: "))
                    stock=int(input("Ingrese cantidad de boletos: "))
                    n[1].append([pelicula,genero,dura,stock])
        case 6:
            name=input("Ingrese pelicula que desea eliminar: ").lower()
            for n in datos:
                for p,i in enumerate(n[1]):
                    if name==i[0].lower():
                        del n[1][p]
                        print("Pelicula eliminada con exito")
        case 7:
            for n in datos:
                t=0
                c=0
                for i in n[1]:
                    c+=1
                    t+=i[2]
                    r=len(i[0])
                t/=c
                t=round(t)
                print(f"La duracion de {n[0]} es {t}")
                
                    