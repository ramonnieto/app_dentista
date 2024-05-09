#import pyrebase

# Configuración de Firebase
# config = {
#     "apiKey": "TU_API_KEY",
#     "authDomain": "TU_DOMINIO.firebaseapp.com",
#     "databaseURL": "https://TU_DOMINIO.firebaseio.com",
#     "storageBucket": "TU_DOMINIO.appspot.com"
# }
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
#firebase-adminsdk-cgdgv@my-first-project---prueba.iam.gserviceaccount.com	firebase-adminsdk	
#Correo electrónico
#firebase-adminsdk-cgdgv@my-first-project---prueba.iam.gserviceaccount.com
#ID único
#113756081115723530801
print("---------------------------")
print("Bienvenido a Clinica PePe")
print("---------------------------")
tipo_perfil=""  # iniciamos variable
while tipo_perfil != "client" and tipo_perfil != "doctor": # bucle para definir un perfil 
    tipo_perfil=input("Que perfil ejecutar un valor client o doctor: ")

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
    datos_client=client
# la variable client se puede guardar en un archivo o en la bbdd
# perfil doctor

else:
    # Se implementa espacio doctor
    print("Hola soy el doctor")
# Qué puede hacer el doctor ? # ver los datos del cliente
# No se puede acceder al diccionario client pq esta guardado


# Registramos en la bbdd los datos de cliente
# db.child("clientes").push(client)
