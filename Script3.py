print("10Verificador de ACL")

try:
    numero_acl = int(input("Ingrese el número de ACL a consultar: "))
    
    if 1 <= numero_acl <= 99:
        resultado = "ACL Estándar"
    elif 100 <= numero_acl <= 199:
        resultado = "ACL Extendida"
    elif 1300 <= numero_acl <= 1999:
        resultado = "ACL Estándar (Rango expandido)"
    elif 2000 <= numero_acl <= 2699:
        resultado = "ACL Extendida (Rango expandido)"
    else:
        resultado = "El número ingresado no está en los rangos de ACL estándar o extendida."

    print(f"\nResultado: El número {numero_acl} corresponde a una: {resultado}")

except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
