registro_lluvia = []

registro_lluvia.append(float(input("Ingresa la precipitacion de la muestra N.1 del dia: ")))
registro_lluvia.append(float(input("Ingresa la precipitacion de la muestra N.2 del dia: ")))
registro_lluvia.append(float(input("Ingresa la precipitacion de la muestra N.3 del dia: ")))
registro_lluvia.append(float(input("Ingresa la precipitacion de la muestra N.4 del dia: ")))
registro_lluvia.append(float(input("Ingresa la precipitacion de la muestra N.5 del dia: ")))

promedio_precipitacion = (registro_lluvia[0] + registro_lluvia[1] + registro_lluvia[2] + registro_lluvia[3] + registro_lluvia[4]) /5

brecha_pluvial = max(registro_lluvia) - min(registro_lluvia)

print("\n-----------REGISTRO DEL DIA-------------")
print(registro_lluvia)
print("----------------------------------------")

print(f"\nEl promedio del registro de la precipitaciones del dia fue de {promedio_precipitacion} mm")
print(f"La brecha pluvial que hubo del dia fue de {round(brecha_pluvial)} mm")