# data cleaning script

# data_cleaning_script.py
# Script simple para limpiar datos numéricos

# Datos de ejemplo "sucios" (simulando carga previa)
datos_sucio = [10.5, 'abc', 20.0, 15.0, 20.0, 1000.0, None, 25.0, 15.0]

print("Datos sucios:", datos_sucio)

# Limpieza paso a paso
datos_limpios = []
for dato in datos_sucio:
    try:
        valor = float(dato) if dato is not None else float('nan')
        if 0 < valor < 100:  # Quitar outliers (ej: >100)
            datos_limpios.append(valor)
    except (ValueError, TypeError):
        continue

# Remover duplicados
datos_unicos = list(set(datos_limpios))

print("Datos limpios (sin outliers/nulos):", datos_limpios)
print("Datos únicos:", datos_unicos)
print("Promedio limpio:", sum(datos_unicos) / len(datos_unicos) if datos_unicos else 0)
