datos= {
    "hospital central": {
        "cardiologia": {
            "sofia": {"edad": 60, "diagnostico": "hipertension", "dias": 4, "seguro": True},
            "pedro": {"edad": 70, "diagnostico": "infarto", "dias": 10, "seguro": False},
            "P": {"edad": 70, "diagnostico": "infarto", "dias": 10, "seguro": False}
        },
        "neurologia": {
            "camila": {"edad": 50, "diagnostico": "epilepsia", "dias": 3, "seguro": True},
            "matiasadas": {"edad": 45, "diagnostico": "acv", "dias": 12, "seguro": True},
            "matieeeeas": {"edad": 45, "diagnostico": "acv", "dias": 12, "seguro": True},
            "matifdfdas": {"edad": 45, "diagnostico": "acv", "dias": 12, "seguro": True},
            "matssaeias": {"edad": 45, "diagnostico": "acv", "dias": 12, "seguro": True}
        }
    },
    "hospital norte": {
        "traumatologia": {
            "ricardo": {"edad": 38, "diagnostico": "fractura", "dias": 5, "seguro": False},
            "josefina": {"edad": 42, "diagnostico": "esguince", "dias": 2, "seguro": True}
        },
        "ginecologia": {
            "valentina": {"edad": 30, "diagnostico": "control prenatal", "dias": 1, "seguro": True},
            "carla": {"edad": 33, "diagnostico": "cesarea", "dias": 4, "seguro": False},
            "matrrgrs": {"edad": 45, "diagnostico": "acv", "dias": 12, "seguro": True},
            "mataddas": {"edad": 45, "diagnostico": "acv", "dias": 12, "seguro": True}
        }
    }
}
total={}
if not total:
    for n,i in datos.items():
        c=0
        for p,v in i.items():
            for a,k in v.items():
                c+=1
                total[n]={"total":c}     
while True:
    print(total)
    print("1. Ordenar Pacientes Por Dias Internados")
    print("2. Mostrar Pacientes Con Seguro que estuvieron mas de 5 dias internado")
    print("3. Calcular Promedio de dias internaods por hospital")
    print("4. Buscar Pacientes Por Diagnostico")
    print("5. Mostrar El Hospital Con Mas pacientes")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            todos=[]
            for n,i in datos.items():
                for p,v in i.items():
                    for a,k in v.items():
                        todos.append((n,p,a,k))
            orde=sorted(todos,key= lambda x:x[3]["dias"],reverse=True)
            for n,p,a,k in orde:
                print(f"{n}|{p}|{a}|{k["dias"]}")
        case 2:
            for n,i in datos.items():
                for p,v in i.items():
                    for a,k in v.items():
                        if k["seguro"]==True and k["dias"]>=5:
                            print(f"{n}|{p}|{a}|{k["dias"]}")
        case 3:
            for n,i in datos.items():
                pro=0
                for p,v in i.items():
                    for a,k in v.items():
                        pro+=k["dias"]
                    pro/=4
                    pro=round(pro)
                print(f"{n} Dias Promedio Total: {pro}")
        case 4:
            buscar=input("Ingrese diagnostico: ")
            encontrado=False
            for n,i in datos.items():
                for p,v in i.items():
                    for a,k in v.items():
                        if buscar==k["diagnostico"]:
                            encontrado=True
                            print(f"{n}|{p}|{a}|{k["dias"]}|{k['diagnostico']}")
            if not encontrado:
                print("Nombre de diagnostico ingresado no existe")
        case 5:
            mayor=max(total.items(),key= lambda x:x[1]["total"])
            print(f"{mayor[0]} {mayor[1]["total"]}")
            
                        