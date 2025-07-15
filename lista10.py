biblioteca = [
    ["Ana Torres", "Ingeniería", [
        ["1984", "2025-07-10"],
        ["El Principito", "2025-07-01"]
    ]],
    ["Luis Rojas", "Psicología", [
        ["Mente y Cerebro", "2025-07-05"]
    ]],
    ["Camila Soto", "Medicina", [
        ["Anatomía Humana", "2025-07-03"],
        ["Fisiología", "2025-07-04"]
    ]]
]
while True:
    print("1. Ver Todos Los Alumnos")
    print("2. Buscar un alumno por nombre y ver sus préstamos.")
    print("3. Agregar un nuevo libro prestado a un alumno")
    print("4. Eliminar un libro prestado")
    print("5. Mostrar cuántos libros tiene cada alumno")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for i in biblioteca:
                print(f"{i[0]},{i[1]}")
                for n in i[2]:
                    print(f"{n[0]}|{n[1]}")
        case 2:
            name=input("Ingrese nombre de el alumno: ").lower()
            for i in biblioteca:
                for n in i[2]:
                    if name==i[0].lower():
                        print(f"{n[0]}|{n[1]}")
        case 3:
            name=input("Ingrese nombre de alumno a agregar libro: ").lower()
            for i in biblioteca:
                if name==i[0].lower():
                    i[2].append(["Spiderman",2020])
        case 4:
            name=input("Ingrese nombre de libro a eliminar: ").lower()
            for i in biblioteca:
                for p,n in enumerate(i[2]):
                    if name==n[0].lower():
                        del i[2][p]
        case 5:
            for n in biblioteca:
                r=len(n[2])
                print(f"La estudiante {n[0]} Tiene {r} Libros")