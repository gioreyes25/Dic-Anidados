biblioteca = {
    "Fantasia": {
        "El nombre del viento": {
            "autor": "Patrick Rothfuss",
            "año": 2007,
            "disponibles": 3
        },
        "Harry Potter y la piedra filosofal": {
            "autor": "J.K. Rowling",
            "año": 1997,
            "disponibles": 5
        },
        "La comunidad del anillo": {
            "autor": "J.R.R. Tolkien",
            "año": 1954,
            "disponibles": 2
        }
    },
    "Ciencia Ficcion": {
        "Dune": {
            "autor": "Frank Herbert",
            "año": 1965,
            "disponibles": 4
        },
        "Neuromante": {
            "autor": "William Gibson",
            "año": 1984,
            "disponibles": 3
        },
        "Fundacion": {
            "autor": "Isaac Asimov",
            "año": 1951,
            "disponibles": 6
        }
    },
    "Misterio": {
        "El codigo Da Vinci": {
            "autor": "Dan Brown",
            "año": 2003,
            "disponibles": 4
        },
        "Los hombres que no amaban a las mujeres": {
            "autor": "Stieg Larsson",
            "año": 2005,
            "disponibles": 2
        },
        "Asesinato en el Orient Express": {
            "autor": "Agatha Christie",
            "año": 1934,
            "disponibles": 3
        }
    }
}

while True:
    print("1. Mostrar Libros Disponibles")
    print("2. Ver Libros Por Genero")
    print("3. Buscar Libro")
    print("4. Ver Cantidad de libros Disponibles Total")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in biblioteca.items():
                for p,v in i.items():
                    if v["disponibles"]!=0:
                        print(f"Genero: {n}|{p}|{v["autor"]}|{v["año"]}|{v["disponibles"]}")
        case 2:
            genero=input("Ingrese genero a buscar: ").lower()
            for n,i in biblioteca.items():
                for p,v in i.items():
                    if genero==n.lower():
                        print(f"Genero: {n}|{p}|{v["autor"]}|{v["año"]}|{v["disponibles"]}")
        case 3:
            libro=input("Ingrese libro que desea buscar: ").lower()
            for n,i in biblioteca.items():
                for p,v in i.items():
                    if libro==p.lower():
                        print(f"Genero: {n}|{p}|{v["autor"]}|{v["año"]}|{v["disponibles"]}")
        case 4:
            t=0
            for n,i in biblioteca.items():
                for p,v in i.items():
                    t+=v["disponibles"]
            print(f"La cantidad de libros disponibles total es: {t}")                    
                        
                                       
                        