cursos = [
    ["MAT101", "Matematicas", [
        ["Ana Torres", 17, [5.5, 6.0, 5.8]],
        ["Luis Rojas", 18, [4.2, 4.5, 5.0]],
        ["Paula Diaz", 17, [6.0, 5.9, 6.1]]
    ]],
    ["HIS202", "Historia", [
        ["Carlos Mena", 16, [4.8, 4.0, 4.5]],
        ["Sofia Rivas", 18, [5.0, 5.2, 5.4]]
    ]],
    ["FIS303", "Fisica", [
        ["Diego Soto", 17, [3.9, 4.1, 4.0]],
        ["Lucia Fuentes", 17, [6.0, 6.2, 6.1]],
        ["Martina Lagos", 16, [5.1, 5.0, 5.3]]
    ]]
]
while True:
    print("1. Ver Estudaintes")
    print("2. Ver Estduiantes de x curso")
    print("3. Buscar Estudiante por nombre")
    print("4. Agregar Nuevo Estudainte")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for i in cursos:
                print(f"Curso: {i[1]}")
                for e in i[2]:
                    p=sum(e[2])/len(e[2])
                    p=round(p,1)
                    print(f"Nombre: {e[0]}|Promedio: {p}")
        case 2:
            curso=input("Ingrese curso a buscar: ").title()
            for i in cursos:
                if curso==i[1]:
                    for e in i[2]:
                        p=sum(e[2])/len(e[2])
                        p=round(p,1)
                        print(f"Nombre: {e[0]}|Promedio: {p}")
        case 3:
            name=input("Ingrese nombre de estudiante: ").title()
            for i in cursos:
                for e in i[2]:
                    if name==e[0]:
                        p=sum(e[2])/len(e[2])
                        p=round(p,1)
                        print(f"Nombre: {e[0]}|Promedio: {p}")
        case 4:
            curso=input("Ingrese curso: ")
            name=input("Ingrese nombre de el estudiante: ")
            n1=float(input("Ingrese nota 1: "))
            n2=float(input("Ingrese nota 2: "))
            n3=float(input("Ingrese nota 3: "))
            for n in cursos:
                if n[1]==curso:
                    n[2].append([name,17,[n1,n2,n3]])