videojuegos = [
    ["PC", [
        ["Minecraft", "Sandbox", 2011, 50],
        ["Valorant", "Shooter", 2020, 30],
        ["Stardew Valley", "Simulación", 2016, 25]
    ]],
    ["PlayStation", [
        ["God of War", "Acción", 2018, 20],
        ["Horizon Zero Dawn", "Aventura", 2017, 15],
        ["FIFA 23", "Deportes", 2022, 40]
    ]],
    ["Nintendo Switch", [
        ["Zelda: BOTW", "Aventura", 2017, 35],
        ["Animal Crossing", "Simulación", 2020, 28],
        ["Mario Kart 8", "Carreras", 2014, 33]
    ]]
]
while True:
    print(videojuegos)
    print("1. Ver Videojuegos")
    print("2. Buscar Videojuego Por Nomrbe")
    print("3. Buscar Por Rango De Años")
    print("4. Agregar Juego")
    op=int(input("Ingerse opcion: "))
    match op:
        case 1:
            for i in videojuegos:
                print("---------------------------")
                print(f"Consola: {i[0]}")
                for p in i[1]:
                    print(f"{p[0]}|{p[1]}|{p[2]}|{p[3]}")
        case 2:
            name=input("Ingrese nombre: ").lower()
            for i in videojuegos:
                for p in i[1]:
                    if name==p[0].lower():
                        print(f"{p[0]}|{p[1]}|{p[2]}|{p[3]}")
        case 3:
            todos=[]
            n1=int(input("Ingrese rango de min: "))
            n2=int(input("Ingrese rango de max: "))
            for i in videojuegos:
                for p in i[1]:
                    todos.append((i,p))
            orden=sorted(todos,key= lambda x:x[1][0])
            for n,i in orden:
                if n1 <= p[2] <= n2 and p[3]!=0:
                    print(f"{n[0]}|{i[0]}|{i[1]}|{i[2]}|{i[3]}")
        case 4:
            consola=input("Ingrese consola: ").lower()
            for i in videojuegos:
                if consola==i[0].lower():
                    juego=input("Ingrese nombre de videojuego: ").title()
                    genero=input("Ingrese genero: ").title()
                    año=int(input("Ingrese año: "))
                    stock=int(input("Ingrese stock: "))
                    i[1].append([juego,genero,año,stock])