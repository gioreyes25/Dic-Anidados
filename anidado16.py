datos= {
    "Carlos": {
        "edad": 21,
        "carrera": "Ingenieria",
        "notas": [5.5, 6.0, 4.8]
    },
    "Lucia": {
        "edad": 22,
        "carrera": "Derecho",
        "notas": [6.2, 5.9, 6.1]
    },
    "Matias": {
        "edad": 20,
        "carrera": "Medicina",
        "notas": [4.3, 4.8, 5.0]
    },
    "Fernanda": {
        "edad": 23,
        "carrera": "Psicologia",
        "notas": [6.0, 6.4, 5.7]
    },
    "Diego": {
        "edad": 19,
        "carrera": "Arquitectura",
        "notas": [5.1, 4.9, 5.3]
    }
}

while True:
    print("1. Ver Estudiantes Registrados")
    print("2. Buscar Estudiante Por Nombre")
    print("3. Ver Estudiantes Con Promedio >=5.5")
    print("4. Agregar Nuevo Estudiante")
    print("5. Eliminar Estudiante")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in datos.items():
                p=0
                p=sum(i["notas"])/len(i["notas"])
                p=round(p,1)
                print(f"Nombre: {n}|Edad: {i["edad"]}|Carrera: {i["carrera"]}|Promedio: {p}")
        case 2:
            name=input("Ingrese nombre de estudiante: ").lower()
            for n,i in datos.items():
                if name==n.lower():
                    p=0
                    p=sum(i["notas"])/len(i["notas"])
                    p=round(p,1)
                    print(f"Nombre: {n}|Edad: {i["edad"]}|Carrera: {i["carrera"]}|Promedio: {p}")
        case 3:
            for n,i in datos.items():
                p=0
                p=sum(i["notas"])/len(i["notas"])
                p=round(p,1)
                if p>=5.5:
                    print(f"Nombre: {n}|Edad: {i["edad"]}|Carrera: {i["carrera"]}|Promedio: {p}")
        case 4:
            name=input("Ingrese nombre de estudiante: ").capitalize()
            edad=int(input("Ingrese edad: "))
            carrera=input("Ingrese carrera: ").capitalize()
            n1=float(input("Ingrese nota 1: "))
            n2=float(input("Ingrese nota 2: "))
            n3=float(input("Ingrese nota 3: "))
            datos[name]={"edad":edad,"carrera":carrera,"notas":[n1,n2,n3]}
        case 5:
            n=input("Ingrese name de estudiante que desea eliminar: ").capitalize()
            if n in datos:
                del datos[n]
                print(f"Se ha eliminado el estudiante {n}")
            else:
                print("No existe ese estudiante")