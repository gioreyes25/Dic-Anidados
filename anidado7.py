datos= {
    "colegio andes": {
        "ignacio": {"edad": 16, "disciplina": "futbol", "puntaje": 88},
        "valentina": {"edad": 17, "disciplina": "voleibol", "puntaje": 91},
        "tomas": {"edad": 15, "disciplina": "atletismo", "puntaje": 83}
    },
    "colegio libertad": {
        "camila": {"edad": 16, "disciplina": "basquetbol", "puntaje": 76},
        "matias": {"edad": 17, "disciplina": "futbol", "puntaje": 95},
        "laura": {"edad": 16, "disciplina": "voleibol", "puntaje": 84}
    },
    "colegio sur": {
        "nicolas": {"edad": 15, "disciplina": "atletismo", "puntaje": 93},
        "sofia": {"edad": 17, "disciplina": "futbol", "puntaje": 87},
        "cristobal": {"edad": 16, "disciplina": "basquetbol", "puntaje": 78}
    }
}
while True:
    print("1. Mostrar Jugadores ordenados mayor a menor (puntaje)")
    print("2. Filtrar Jugadores Por Disciplina")
    print("3. Calcular El Promedio de puntaje por colegio")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["puntaje"],reverse=True)
            for n,p,v in ordenados:
                print(f"{n}|Nombre: {p}|Edad: {v["edad"]}|Disciplina: {v["disciplina"]}|Puntaje: {v["puntaje"]}")
        case 2:
            for n,i in datos.items():
                for p,v in i.items():
                    print
                print(v["disciplina"])
            buscar=input("Ingrese disciplina: ")
            for n,i in datos.items():
                for p,v in i.items():
                    if buscar==v["disciplina"]:
                        print(f"{n}|Nombre: {p}|Edad: {v["edad"]}|Disciplina: {v["disciplina"]}|Puntaje: {v["puntaje"]}")
        case 3:
            for n,i in datos.items():
                pro=0
                for p,v in i.items():
                    pro+=v["puntaje"]
                pro/=3
                pro=round(pro)
                print(f"{n} Promedio de puntaje: {pro}")
        case 4:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            mayor=max(todos,key= lambda x:x[2]["puntaje"])
            print(f"Colegio: {mayor[0]}|Nombre: {mayor[1]}|Disciplina: {mayor[2]["disciplina"]}|Puntaje: {mayor[2]["puntaje"]}")

