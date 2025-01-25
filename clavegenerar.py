import secrets

def generar_clave_encriptacion(longitud=32):
    # Generar una clave criptográficamente segura de la longitud especificada en bytes
    clave = secrets.token_bytes(longitud)  # Devuelve una cadena de bytes aleatorios
    
    # Convertir a formato hexadecimal para almacenamiento o uso más fácil
    return clave.hex()

# Generar la clave de encriptación (32 bytes = 256 bits)
clave_encriptacion = generar_clave_encriptacion()

# Mostrar la clave generada
print(f"Clave de encriptación generada: {clave_encriptacion}")

