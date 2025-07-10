datos = {
    "españa": {
        "vuelo_001": {
            "info": {
                "aerolinea": "Iberia",
                "hora_salida": "12:30",
                "duracion": 720
            },
            "ana rojas": {"edad": 34, "maletas": 2, "clase": "economica"},
            "lucas díaz": {"edad": 40, "maletas": 1, "clase": "ejecutiva"},
            "maría torres": {"edad": 29, "maletas": 3, "clase": "economica"},
            "javier lópez": {"edad": 55, "maletas": 2, "clase": "primera"},
            "carla muñoz": {"edad": 23, "maletas": 1, "clase": "ejecutiva"}
        }
    },
    "eeuu": {
        "vuelo_002": {
            "info": {
                "aerolinea": "American Airlines",
                "hora_salida": "08:15",
                "duracion": 600
            },
            "sofia soto": {"edad": 31, "maletas": 1, "clase": "economica"},
            "pedro navarro": {"edad": 45, "maletas": 2, "clase": "primera"},
            "daniela fuentes": {"edad": 27, "maletas": 2, "clase": "ejecutiva"},
            "gonzalo reyes": {"edad": 38, "maletas": 1, "clase": "economica"},
            "ines contreras": {"edad": 60, "maletas": 3, "clase": "primera"}
        }
    },
    "brasil": {
        "vuelo_003": {
            "info": {
                "aerolinea": "LATAM",
                "hora_salida": "17:45",
                "duracion": 480
            },
            "matías godoy": {"edad": 36, "maletas": 2, "clase": "ejecutiva"},
            "alejandro vera": {"edad": 50, "maletas": 1, "clase": "primera"},
            "karla estrada": {"edad": 33, "maletas": 2, "clase": "economica"},
            "raul pizarro": {"edad": 42, "maletas": 1, "clase": "economica"},
            "ximena bustos": {"edad": 28, "maletas": 3, "clase": "primera"}
        }
    }
}

while True:
    print("1. Buscar Pasajeros")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for pais, vuelos in datos.items():
                for vuelo, contenido in vuelos.items():
                    info = contenido["info"]
                    for nombre, pasajero in contenido.items():
                        if nombre == "info":
                            continue
                        print(f"Pasajero: {nombre} | Vuelo: {vuelo} | Aerolínea: {info['aerolinea']} | Duración: {info['duracion']} min")
