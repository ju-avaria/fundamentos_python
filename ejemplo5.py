# Ejemplo mínimo
linea = "     2026-10-12|ERROR|payment_gateway|Timeout en la respuesta    "

print(linea)

linea_limpia = linea.strip()
print(linea_limpia)
campos = linea_limpia.split("|")

print(campos)

print(campos[1])  
print(len(campos))