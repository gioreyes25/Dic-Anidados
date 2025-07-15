cursos = [
    ["1A", [
        ["Ana Torres", 20, 18],
        ["Luis Rojas", 20, 15],
        ["Camila Soto", 20, 20]
    ]],
    ["1B", [
        ["Carlos Mena", 20, 17],
        ["Sofia Rivas", 20, 20],
        ["Pedro Mora", 20, 14]
    ]]
]
while True:
    print("1. Ver Estudiantes")
    print("2. Buscar Estudiante")
    print("3. Agregar Alumno Nuevo A x Curso")
    print("4. Registrar Asistencia")
    print("5. Eliminar Alumno")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for i in cursos:
                print(f"{i[0]}")
                p=0
                for n in i[1]:
                    p=(n[2]/n[1])*100
                    p=round(p,1)
                    print(f"{n[0]}|{n[1]}|{n[2]}|Promedio Asistencia: {p}%")
        case 2:
            name=input("Ingrese nombre de estudainte: ").lower()
            for i in cursos:
                for n in i[1]:
                    if name==n[0].lower():
                        p=(n[2]/n[1])*100
                        p=round(p,1)
                        print(f"{n[0]}|{n[1]}|{n[2]}|Promedio Asistencia: {p}%")
        case 3:
            curso=input("Ingrese curso al que lo añadira: ").upper()
            name=input("Ingrese nombre de alumno nuevo: ").title()
            for n in cursos:
                if curso==n[0]:
                    n[1].append([name,1,1])
        case 4:
            name=input("Ingrese nombre de alumno: ").lower()
            for i in cursos:
                for n in i[1]:
                    if name==n[0].lower():
                        n[2]+=1
                        n[1]+=1
                        print("Asistencia registrada con exito")
        case 5:
            name=input("Ingrese nombre de alumno: ")
            for n in cursos:
                for na,i in  enumerate(n[1]):
                    if name==i[0].lower():
                        del n[1][na]
                        print(f"Estudainte eliminado")
                    
                        