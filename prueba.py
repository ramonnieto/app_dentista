print("---------------------------")
print("Bienvenido a Clinica PePe")
print("---------------------------")
tipo_perfil=""  # iniciamos variable
while tipo_perfil != "client" and tipo_perfil != "doctor": # bucle para definir un perfil 
    tipo_perfil=input("Que perfil ejecutar un valor client o doctor: ")
"""     if tipo_perfil == "client":
        print("Hola soy un cliente")
    elif tipo_perfil =="doctor":
        print("Hola soy el doctor")
    else:
        print("seleccione un valor client o doctor") """

#print("Estoy fuera")

# Perfil client
if tipo_perfil == "client":
    # se implementa el espacio cliente
    print("Hola soy un cliente")
    client = dict()
    client["name_client"]=input("Dame un nombre: ")
    client["apellido_client"]=input("Dame un apellido: ")
    client["telf_client"]=input("Dame un telf: ")
    print(client)
# La variable diccionario subirla a la bbdd
#
# perfil doctor
#
else:
    # Se implementa espacio doctor
    print("Hola soy el doctor")

