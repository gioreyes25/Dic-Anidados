datos = {
    "medicina general": {
        "roberto": {"edad": 34, "motivo": "dolor de cabeza", "prioridad": 3},
        "paula": {"edad": 22, "motivo": "resfrio", "prioridad": 4},
        "nicolas": {"edad": 40, "motivo": "fiebre", "prioridad": 2}
    },
    "pediatria": {
        "valentina": {"edad": 6, "motivo": "tos seca", "prioridad": 2},
        "martin": {"edad": 4, "motivo": "vomitos", "prioridad": 1},
        "camila": {"edad": 3, "motivo": "control sano", "prioridad": 5}
    },
    "traumatologia": {
        "ricardo": {"edad": 55, "motivo": "dolor de rodilla", "prioridad": 3},
        "diego": {"edad": 47, "motivo": "fractura", "prioridad": 1},
        "lucas": {"edad": 60, "motivo": "lumbago", "prioridad": 2}
    }
}
while True:
    print("1. Agregar Paciente")
    print("2. Lisar Pacientes Por Especialidad")
    print("3. Buscar Paciente por nombre")
    print("4. Listar Pacientes Con Prioirdad 1 y 2")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            name=input("Ingrese nombre de paciente: ")
            for n,i in datos.items():
                print(n)
            area=input("Ingrese area ( si no existe se creara una): ")
            edad=input("Ingrese edad: ")
            pri=int(input("Ingrese Prioridad de el paciente: "))
            if area in datos:
                datos[area][name]={"edad":edad,"prioridad":pri}
            else:
                datos[area]={}
                datos[area][name]={"edad":edad,"prioridad":pri}
        case 2:
            for n,i in datos.items():
                print(n)
            espe=input("Ingrese especialidad a buscar: ")
            if espe in datos:
                print(espe)
                for n,i in datos.items():
                    for p,v in i.items():
                        if espe==n:
                            print(f"Nombre: {p} Edad: {v["edad"]} Prioridad: {v["prioridad"]}")
        case 3:
            nombre=input("Ingrese nombre de paciente a buscar: ")
            encontrado=False
            for n,i in datos.items():
                for p,v in i.items():
                    if nombre==p:
                        encontrado=True
                        print(f"Nombre: {p} Edad: {v["edad"]} Prioridad: {v["prioridad"]}")
            if not encontrado:
                print("Paciente ingresado no existe")
        case 4:
            for n,i in datos.items():
                for p,v in i.items():
                    ordenados=sorted(i.items(),key= lambda x:x[1]["edad"])
                for na,va in ordenados:
                    if va["prioridad"]== 1 or va["prioridad"]== 2:
                        print(f"Area: {n} Nombre: {na} Edad: {va["edad"]} Prioridad: {va["prioridad"]}")