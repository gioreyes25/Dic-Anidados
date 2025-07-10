datos= {
    "sede norte": {
        "el principito": {"autor": "antoine de saint-exupery", "anio": 1943, "prestamos": 23},
        "1984": {"autor": "george orwell", "anio": 1949, "prestamos": 31},
        "cien años de soledad": {"autor": "gabriel garcia marquez", "anio": 1967, "prestamos": 18}
    },
    "sede centro": {
        "don quijote": {"autor": "miguel de cervantes", "anio": 1605, "prestamos": 45},
        "rayuela": {"autor": "julio cortazar", "anio": 1963, "prestamos": 29},
        "la sombra del viento": {"autor": "carlos ruiz zafon", "anio": 2001, "prestamos": 34}
    },
    "sede sur": {
        "el tunel": {"autor": "ernesto sabato", "anio": 1948, "prestamos": 12},
        "la tregua": {"autor": "mario benedetti", "anio": 1960, "prestamos": 27},
        "el aleph": {"autor": "jorge luis borges", "anio": 1949, "prestamos": 30}
    }
}
while True:
    print("1. Mostrar Libros Mas Prestados")
    print("2. Mostrar Libros Publicados Antes De 1970")
    print("3. Mostrar El Promedio de prestamos por sede")
    print("4. Buscar Libros Por Autor")
    print("5. Mostrar Sede que tiene el libro mas antiguo")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["prestamos"],reverse=True)
            for n,p,v in ordenados:
                print(f"{n}|Libro: {p}|Autor: {v["autor"]}|Año: {v["anio"]}|Prestamos: {v["prestamos"]}")
        case 2:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            ordenados=sorted(todos,key= lambda x:x[2]["prestamos"],reverse=True)
            for n,p,v in ordenados:
                if v["anio"]<=1970:
                    print(f"{n}|Libro: {p}|Autor: {v["autor"]}|Año: {v["anio"]}|Prestamos: {v["prestamos"]}")
        case 3:
            for n,i in datos.items():
                pro=0
                for p,v in i.items():
                    pro+=v["prestamos"]
                pro/=3
                pro=round(pro) 
                print(f"{n} Promedio: {pro}")
        case 4:
            for n,i in datos.items():
                for p,v in i.items():
                    print(f"{v["autor"]}")
            autor=input("Ingrese nombre de autor para buscar sus libros: ")
            for n,i in datos.items():
                for p,v in i.items():
                    if autor==v["autor"]:
                        print(f"Libro: {p}|Autor: {v["autor"]}|Año: {v["anio"]}|Prestamos: {v["prestamos"]}")
        case 5:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    todos.append((n,p,v))
            menor=min(todos,key= lambda x:x[2]["anio"])
            print(f"{menor[0]} {menor[1]} {menor[2]["autor"]}")
            
                    