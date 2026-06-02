codigo = input("Ingresa el codigo identificador: ")

codigo = codigo.upper()

codigo = codigo.strip()

codigo = codigo.replace("_", "")

print(f"El reporte del codigo en limpio es el siguiente:{codigo}, y los numeros de caracteres que tienes es de: {len(codigo)} caracteres")