# data_loading_script.py
# Script simple para cargar datos numéricos vía input

data_count = int(input("Ingrese el número de datos: "))
datos = []

for i in range(data_count):
    try:
        valor = float(input(f"Ingrese el dato {i+1}: "))
        datos.append(valor)
    except ValueError:
        print(f"Error en dato {i+1}: debe ser un número. Omitido.")
        continue

if datos:
    print("Datos cargados:", datos)
    print("Promedio:", sum(datos) / len(datos))
else:
    print("No se cargaron datos válidos.")
