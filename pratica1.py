datos = {
    "A001": ["Thriller", 1982, "Pop", 15],
    "A002": ["Back in Black", 1982, "Rock", 10],
    "A003": ["The Dark Side of the Moon", 1973, "Rock", 8],
    "A004": ["The Bodyguard", 1992, "RB", 12],
    "A005": ["Rumours", 1977, "Rock", 9],
    "A006": ["Run", 2011, "Pop", 11],
    "A007": ["Come Away With Me", 2002, "Jazz", 0],
    "A008": ["Abbey Road", 1970, "Rock", 13],
    "A009": ["Hotel California", 1970, "Rock", 10],
    "A010": ["Zilk", 2014, "Pop", 14]
}
inventario = {
    "A001": [15, "Pop"],
    "A002": [10, "Rock"],
    "A003": [8, "Rock"],
    "A004": [12, "RB"],
    "A005": [9, "Rock"],
    "A006": [11, "Pop"],
    "A007": [0, "Jazz"],
    "A008": [13, "Rock"],
    "A009": [10, "Rock"],
    "A010": [14, "Pop"]
}
while True:
    print("1. Stock Por Genero")
    print("2. Buscar Album Por Año De Lanzamiento")
    print("3. Actualizar Stock")
    print("4. Salir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            stoc=input("Ingrese genero que desea buscar: ").capitalize()
            total=0
            for id,valor in inventario.items():
                if stoc==valor[1]:
                    total+=valor[0]
            print(f"El stock de {stoc} es: {total}")
        case 2:
            while True:
                try:
                    num1=int(input("Ingrese rango de años min"))
                    num2=int(input("Ingrese rango de años max"))
                    break
                except ValueError:
                    print("Solo se permiten numeros enteros")
            ordenados = sorted(datos.items(), key=lambda item: item[1][0])
            resultados = []
            for id,valor in ordenados:
                cancion,año,genero,cantidad = valor
                if num1 <= int(año) <= num2  and cantidad !=0:
                    resultados.append(f"{id}--{cancion}--{año}--s{genero}")
                else:
                    print
            if resultados:
                for i in resultados:
                    print(i)
            else:
                print("No se ecnontraron album en ese rango de años")
        case 3:
            buscar=input("Ingrese ID para actualizar stock: ").upper()
            if buscar in inventario:
                for id,valor in inventario.items():
                    if buscar==id:
                        print(f"{id}--{valor[0]}--{valor[1]}")
                        canti=int(input("Ingrese cantidad que desea"))
                        inventario[id][0]+=canti
                        print(f"Se han agregado {canti}u a el ID {id}")
            else:
                print("ID Ingresado no existe")
        case 4:
            print("Programa Finalizado")