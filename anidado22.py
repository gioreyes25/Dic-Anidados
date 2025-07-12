colegios = {
    "Colegio Norte": {
        "1A": {
            "Ana Torres": {"notas": [5.5, 6.0, 5.8]},
            "Luis Rojas": {"notas": [4.2, 4.5, 5.0]},
            "Paula Diaz": {"notas": [6.0, 5.9, 6.1]},
            "Carlos Mena": {"notas": [4.8, 4.0, 4.5]},
            "Sofia Rivas": {"notas": [5.0, 5.2, 5.4]}
        },
        "1B": {
            "Diego Soto": {"notas": [3.9, 4.1, 4.0]},
            "Lucia Fuentes": {"notas": [6.0, 6.2, 6.1]},
            "Martina Lagos": {"notas": [5.1, 5.0, 5.3]},
            "Tomas Paredes": {"notas": [4.4, 4.3, 4.6]},
            "Fernanda Nuñez": {"notas": [5.5, 5.6, 5.7]}
        },
        "2A": {
            "Andres Vidal": {"notas": [4.5, 4.9, 5.0]},
            "Valentina Soto": {"notas": [6.0, 5.8, 6.1]},
            "Joaquin Lara": {"notas": [5.2, 5.3, 5.4]},
            "Catalina Reyes": {"notas": [4.0, 4.2, 4.1]},
            "Sebastian Rios": {"notas": [3.5, 3.9, 4.0]}
        }
    },
    "Liceo Sur": {
        "1C": {
            "Maria Paz": {"notas": [5.8, 5.9, 6.0]},
            "Francisco Mora": {"notas": [4.1, 4.3, 4.5]},
            "Natalia Rojas": {"notas": [6.0, 5.9, 6.1]},
            "Benjamín Soto": {"notas": [3.8, 4.0, 4.2]},
            "Isidora Gallardo": {"notas": [5.0, 5.1, 5.3]}
        },
        "2B": {
            "Gabriel Muñoz": {"notas": [5.7, 5.9, 6.0]},
            "Josefa Palma": {"notas": [6.2, 6.1, 6.0]},
            "Ignacio Bravo": {"notas": [4.8, 5.0, 4.9]},
            "Florencia Vidal": {"notas": [5.5, 5.6, 5.7]},
            "Matias Rivas": {"notas": [3.9, 4.0, 4.1]}
        },
        "2C": {
            "Agustin Fuentes": {"notas": [5.4, 5.5, 5.6]},
            "Constanza Pino": {"notas": [4.2, 4.3, 4.5]},
            "Rafael Castillo": {"notas": [6.0, 6.1, 6.2]},
            "Antonella Mena": {"notas": [5.1, 5.2, 5.3]},
            "Bruno Tapia": {"notas": [4.0, 4.2, 4.3]}
        }
    },
    "Instituto Central": {
        "3A": {
            "Martin Castillo": {"notas": [4.5, 4.6, 4.7]},
            "Trinidad Rojas": {"notas": [6.0, 6.1, 6.2]},
            "Javiera Diaz": {"notas": [5.2, 5.3, 5.4]},
            "Diego Fernandez": {"notas": [3.8, 4.0, 4.1]},
            "Camila Ortiz": {"notas": [5.5, 5.6, 5.7]}
        },
        "3B": {
            "Leonardo Silva": {"notas": [4.9, 5.0, 5.1]},
            "Renata Farias": {"notas": [5.3, 5.4, 5.5]},
            "Aaron Leiva": {"notas": [4.2, 4.3, 4.4]},
            "Laura Gutierrez": {"notas": [5.0, 5.1, 5.3]},
            "Cristobal Romero": {"notas": [6.0, 5.9, 6.1]}
        },
        "3C": {
            "Benjamin Pizarro": {"notas": [3.7, 4.0, 4.2]},
            "Maite Navarro": {"notas": [5.6, 5.8, 6.0]},
            "Ignacia Herrera": {"notas": [4.8, 5.0, 5.1]},
            "Vicente Rojas": {"notas": [5.4, 5.6, 5.5]},
            "Emilia Vega": {"notas": [4.0, 4.2, 4.3]}
        }
    }
}

while True:
    print("1. Ver Todos Los Cursos")
    print("2. Ver Estudiantes De X Curso")
    print("3. Buscar Estudiante Por Nombre")
    print("4. Ver Estudianets Con Promedio >=5.5")
    print("5. Agregar Estudiante nuevo a un curso")
    print("6. Eliminar Estudiante")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in colegios.items():
                for f,v in i.items():
                    for a,k in v.items():
                        p=0
                        p=sum(k["notas"])/len(k["notas"])
                        p=round(p,1)
                        print(f"{n}|{f}|{a}|Promedio: {p}")
        case 2:
            curso=input("Ingrese curso: ").upper()
            for n,i in colegios.items():
                for f,v in i.items():
                    for a,k in v.items():
                        if curso==f:
                            p=0
                            p=sum(k["notas"])/len(k["notas"])
                            p=round(p,1)
                            print(f"{n}|{f}|{a}|Promedio: {p}")
        case 3:
            name=input("Ingrese nombre de estudiante: ").title()
            for n,i in colegios.items():
                for f,v in i.items():
                    for a,k in v.items():
                        if name==a:
                            p=0
                            p=sum(k["notas"])/len(k["notas"])
                            p=round(p,1)
                            print(f"{n}|{f}|{a}|Promedio: {p}")
        case 4:
            for n,i in colegios.items():
                for f,v in i.items():
                    for a,k in v.items():
                        p=0
                        p=sum(k["notas"])/len(k["notas"])
                        p=round(p,1)
                        if p>=5.5:
                            print(f"{n}|{f}|{a}|Promedio: {p}")
        case 5:
            cole=input("Ingrese coelgio: ").title()
            curso=input("Ingrese curso: ").upper()
            name=input("Ingrese nombre de estudiante: ").title()
            n1=float(input("Ingrese nota 1: "))
            n2=float(input("Ingrese nota 2: "))
            n3=float(input("Ingrese nota 3: "))
            colegios[cole][curso][name]={"notas":[n1,n2,n3]}
        case 6:
            cole=input("Ingrese colegio ddonde esta: ").title()
            curso=input("Ingrese su curso: ").upper()
            name=input("Ingrese nombre de el estudainte: ")
            if name in colegios[cole][curso]:
                del colegios[cole][curso][name]
                print(f"Se ha eliminado el estudiante {name}")
            else:
                print("Estudainte no existe")