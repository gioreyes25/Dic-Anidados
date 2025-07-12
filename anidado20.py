hospitales = {
    "Santiago": {
        "Hospital Central": {
            "doctores": {
                "Dr. Pérez": {
                    "especialidad": "Cardiología",
                    "pacientes": ["Juan", "Ana", "Luis"],
                    "consultas": 12
                },
                "Dra. Soto": {
                    "especialidad": "Neurología",
                    "pacientes": ["Pedro", "Claudia"],
                    "consultas": 8
                }
            }
        },
        "Hospital Sur": {
            "doctores": {
                "Dr. Rojas": {
                    "especialidad": "Pediatría",
                    "pacientes": ["María", "Tomás"],
                    "consultas": 5
                }
            }
        }
    },
    "Valparaiso": {
        "Hospital Regional": {
            "doctores": {
                "Dra. Ruiz": {
                    "especialidad": "Dermatología",
                    "pacientes": ["Felipe"],
                    "consultas": 2
                }
            }
        }
    }
}
while True:
    print("\n1. Ver Cantidad de doctores")
    print("2. Ver Hospitales Por Ciudad")
    print("3. Preguntar por una especialidad y mostrar los nombres de los doctores que la tienen y en qué ciudad y hospital trabajan")
    print("4. Mostrar el total de consultas realizadas en toda la red.")
    print("5. Agregar un nuevo paciente a un doctor específico (debes pedir ciudad, hospital y nombre del doctor).")
    print("6. Ver Doctor Con Mas Pacientes")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            c=0
            for n,i in hospitales.items():
                for p,v in i.items():
                    for a,k in v.items():
                        for r,b in k.items():
                            if r:
                                print(f"{r}")
                                c+=1
            print(f"Cantidad de doctores: {c}")
        case 2:
            city=input("Ingrese ciudad a buscar: ").capitalize()
            if city in hospitales:
                for n,i in hospitales.items():
                    for p,v in i.items():
                        if city==n:
                            print(p)
        case 3:
            espe=input("Ingrese especialidad: ").title()
            for n,i in hospitales.items():
                for p,v in i.items():
                    for a,k in v.items():
                        for r,b in k.items():
                            if espe==b["especialidad"]:
                                print(f"{r}|Trabaja En {n} en el {p}")
        case 4:
            c=0
            for n,i in hospitales.items():
                for p,v in i.items():
                    for a,k in v.items():
                        for r,b in k.items():
                            c+=b["consultas"]
            print(f"Consultas Hechas En Total {c}")
        case 5:
            ciudad=input("Ingrese ciudad: ")
            hospital=input("Ingrese Hospital: ")
            name=input("Ingrese Nombre De Doctor: ")
            paciente=input("Ingrese nombre de paciente: ")
            hospitales[ciudad][hospital]["doctores"][name]["pacientes"].append(paciente)
        case 6:
            t=[]
            for n,i in hospitales.items():
                for p,v in i.items():
                    for a,k in v.items():
                        for r,b in k.items():
                            t.append((r,b))
            orden=sorted(t,key= lambda x:len(x[1]["pacientes"]),reverse=True)
            for n,i in orden:
                print(f"{n} {len(i["pacientes"])}")                      