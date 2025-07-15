datos = [
    ["Grupo A", [
        ["Chile", 3, 5, 2, 6],
        ["Argentina", 3, 7, 3, 7],
        ["Paraguay", 3, 3, 6, 3]
    ]],
    ["Grupo B", [
        ["Brasil", 3, 9, 1, 9],
        ["Ecuador", 3, 4, 4, 4],
        ["Uruguay", 3, 2, 5, 2]
    ]]
]
#|nombre_equipo|partidos|goles|goles_en_contra|puntos
paises=["Chile","Argentina","Paraguay","Brazil","Uruguay","Ecuador"]
while True:
    print("1. Ver Equipos")
    print("2. Buscar Equipo Por Nombre")
    print("3. Agregar Nuevo Equipo a x grupo")
    print("4. Jugar Partido")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            for i in datos:
                for n in i[1]:
                    todos.append((i,n))
            orden=sorted(todos,key=lambda x:x[1][4],reverse=True)
            for n,i in orden:
                print(f"{n[0]}|{i[0]}|Puntos: {i[4]}")
        case 2:
            name=input("Ingrese nombre de equipo: ").lower()
            for i in datos:
                for n in i[1]:
                    if name==n[0].lower():
                        print(f"{i[0]}|{n[0]}|Puntos: {n[4]}")          
        case 3:
            grupo=input("Ingrese grupo: ").lower()
            for i in datos:
                for n in i[1]:
                    if grupo==i[0].lower():
                        pais=input("Ingrese pais: ").title()
                        partidos=int(input("Ingrese partidos jugados: "))
                        gol=int(input("Ingrese goles: "))
                        golen=int(input("Ingrese goles encontra: "))
                        pts=int(input("Ingrese puntos: "))
                        if pais not in paises:
                            i[1].append([pais,partidos,gol,golen,pts])
                            paises.append(pais)
                            break
                        else:
                            print(f"{pais} Ya se encuentra registado")
                            break
        case 4:
            c=0
            pais1=input("Ingrese primer Pais: ").title()
            if pais1 in paises:
                pais2=input("Ingrese segundo Pais: ").title()
                if pais2 in paises:
                    esta={
                        pais1:{},
                        pais2:{}
                    }
                    for n in datos:
                        for i in n[1]:
                            if pais1 == i[0]:
                                gol=int(input(F"Ingrese goles que {pais1} le anota a {pais2}"))
                                i[2]+=gol
                                i[1]+=1
                                esta[pais1]={"total":gol}
                                c=1
                            elif pais2==i[0] and c==1:
                                    goles=int(input(F"Ingrese goles que {pais2} le anota a {pais1}"))
                                    i[2]+=goles
                                    i[1]+=1
                                    esta[pais2]={"total":goles}
            if gol != goles:
                mayor=max(esta.items(),key= lambda x:x[1]["total"])
                ganador=mayor[0]
                for i in datos:
                    for n in i[1]:
                        if ganador==n[0]:
                            n[4]+=3
                print(f"{ganador} Ha sumado 3 pts")
            else:
                print("Ambos suman 1 pts")
                                    
                                    
                            
                    