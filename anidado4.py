datos = {
    "matematica": {
        "camila": {"edad": 15, "nota": 6.1, "asistencia": 20},
        "rodrigo": {"edad": 16, "nota": 5.8, "asistencia": 85},
        "jose": {"edad": 15, "nota": 6.5, "asistencia": 95}
    },
    "historia": {
        "maria": {"edad": 17, "nota": 6.3, "asistencia": 92},
        "nicolas": {"edad": 16, "nota": 5.5, "asistencia": 80},
        "paula": {"edad": 15, "nota": 6.9, "asistencia": 58}
    },
    "biologia": {
        "francisco": {"edad": 16, "nota": 5.7, "asistencia": 48},
        "laura": {"edad": 15, "nota": 6.4, "asistencia": 93},
        "sebastian": {"edad": 17, "nota": 6.0, "asistencia": 55}
    }
}
while True:
    print("1. Ver estudaintes Por Asgignatura")
    print("2. Ver Alumnos Por Notas")
    print("3. Ver Alumnos Aprobados Por Asistencia")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            buscar=input("Ingrese agignaturta: ")
            if buscar in datos:
                for n,i in datos.items():
                    for p,v in i.items():
                        if buscar==n:
                            print(f"Estudiante: {p}|Edad: {v["edad"]}|Promedio: {v["nota"]}|Asistencia: {v["asistencia"]}")
        case 2:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["nota"],reverse=True)
            for n,p,v in ordenados:
                print(f"Asignatura: {n}|Estudiante: {p}|Promedio: {v["nota"]}|Asistencia: {v["asistencia"]}")
        case 3:
            for n,i in datos.items():
                for p,v in i.items():
                    if v["asistencia"]>=75:
                        print(f"Estudiante: {p}|Edad: {v["edad"]}|Promedio: {v["nota"]}|Asistencia: {v["asistencia"]}")