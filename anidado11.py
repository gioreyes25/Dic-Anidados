datos = {
    "ciencias": {
        "matematica": {
            "alice":    {"edad": 20, "notas": [6.0, 5.5, 7.0], "asistencia": 92},
            "bernardo": {"edad": 21, "notas": [4.0, 5.0, 2.1], "asistencia": 85},
            "camila":   {"edad": 19, "notas": [7.0, 6.5, 6.8], "asistencia": 97}
        },
        "fisica": {
            "daniel":   {"edad": 22, "notas": [5.5, 6.3, 6.0], "asistencia": 88},
            "elena":    {"edad": 20, "notas": [6.8, 7.0, 7.2], "asistencia": 95},
            "fernando": {"edad": 21, "notas": [4.5, 5.0, 4.8], "asistencia": 80}
        }
    },
    "letras": {
        "literatura": {
            "gabriela": {"edad": 23, "notas": [6.9, 7.0, 6.5], "asistencia": 90},
            "hernan":   {"edad": 22, "notas": [5.0, 5.5, 5.2], "asistencia": 82},
            "irene":    {"edad": 20, "notas": [6.2, 6.0, 6.4], "asistencia": 93}
        },
        "filosofia": {
            "juan":     {"edad": 24, "notas": [4.8, 5.1, 4.9], "asistencia": 78},
            "karla":    {"edad": 21, "notas": [6.5, 6.7, 6.8], "asistencia": 94},
            "luis":     {"edad": 23, "notas": [5.3, 5.6, 5.4], "asistencia": 88}
        }
    }
}
while True:
    print("1. Ver Mejores 3 Estudiantes Por Curso")
    print("2. Ver Promedio Generales De Cursos")
    print("3. Ver Estudiantes Reprobados")
    print("4. Buscar Estudiante por nombre")
    print("5. Ver Mejor Facultad")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            import heapq
            total=[]
            buscar=input("Ingrese curso: ")
            encontrado=False
            for n,i in datos.items():
                for p,v in i.items():
                    for a,k in v.items():
                        if buscar==n:
                            encontrado=True
                            pro=sum(k["notas"])/len(k["notas"])
                            pro=round(pro,1)
                            total.append((a,pro,p,k))
            if not encontrado:
                print("No hay coincidencias")
            top=heapq.nlargest(3,total,key= lambda x:x[1])
            for i,(a,pro,p,k) in enumerate(top,start=1):
                print(f"{i}- {a} {pro} {p}")
        case 2:
            todos=[]
            for n,i in datos.items():
                pro=0
                for p,v in i.items():
                    for a,k in v.items():
                        if n:
                            if p:
                                pro+=sum(k["notas"])
                    pro/=9
                    pro=round(pro,1)
                    todos.append((n,p,pro))
                    pro=0
            orden=sorted(todos,key= lambda x:x[2],reverse=True)
            for n,p,pro in orden:
                print(f"{n} {p} {pro}")
        case 3:
            todos=[]
            for n,i in datos.items():
                pro=0
                for p,v in i.items():
                    for a,k in v.items():
                        if a:
                            pro+=sum(k["notas"])
                        pro/=3
                        pro=round(pro,1)
                        todos.append((a,n,p,pro,k))
                        pro=0
            orden=sorted(todos,key= lambda x:x[2])
            for a,n,p,pro,k in orden:
                if pro<4.0:
                    print(f"{a} {p}|Promedio: {pro}|Edad: {k["edad"]}|")
        case 4:
            buscar=input("Ingrese nombre de estudiante: ")
            encontrado=False
            for n,i in datos.items():
                pro=0
                for p,v in i.items():
                    for a,k in v.items():
                        if buscar==a:
                            encontrado=True
                            pro+=sum(k["notas"])
                            pro/=3
                            pro=round(pro,1)
                            print(f"{a} {p}|Promedio: {pro}|Edad: {k["edad"]}|")
            if not encontrado:
                print("No existe almuno ingresado")
        case 5:
            todos=[]
            for n,i in datos.items():
                pro=0
                if n:
                    for p,v in i.items():
                        for a,k in v.items():
                            p=sum(k["notas"])
                            pro+=p
                pro/=18
                pro=round(pro,1)
                todos.append((n,pro))
            mayor=max(todos,key= lambda x:x[1])
            print(f"La mejor facu es: {mayor[0]} {mayor[1]}")
                                
                            

                            
                        
