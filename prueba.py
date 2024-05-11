import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint





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

""" db = firestore.client()
# Add documents with auto IDs
data = {
    'name': 'John Smith',
    'age': 40,
    'employed': True
}
db.collection('client').add(data) """


cred = credentials.Certificate("token_app_clinic.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



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
    
    dni=input("Dame un DNI: ")
    client=db.collection("dentista pruebas").document(dni).get().to_dict()
    if client is None:    
        client=dict()
        client["name_client"]=input("Dame un nombre: ")
        client["apellido_client"]=input("Dame un apellido: ")
        client["telf_client"]=int(input("Dame un telf: "))
        db.collection("dentista pruebas").document(dni).set(client)
  
    print(client)    

    print (f"Bienvenido {client['name_client']} {client['apellido_client']}")
    #print ("Bienvenido " + client["name_client"] + " " + client["apellido_client"])
    while True:
        print("""
        Seleccione informacion que desea modificar:
        1. Nombre
        2. Apellido
        3. Telefono
        4. Email
        5. Localidad
        6. exit
        """)
        opcion = input("elige una opcion: ")
                
        if opcion == "6":
            exit()
        print(f"he elegido {opcion}")
        if opcion == "1":
            newname = input("Introduce nuevo nombre: ")
            db.collection("dentista pruebas").document(dni).update({"name_client": newname})

# la variable client se puede guardar en un archivo o en la bbdd
# perfil doctor

else:
    # Se implementa espacio doctor
    print("Hola soy el doctor")
# Qué puede hacer el doctor ? # ver los datos del cliente
# No se puede acceder al diccionario client pq esta guardado
    operation = "0"
    while operation != "X":
        print("\nSelect an operation, o press [X] to exit")
        print("\t[1] Crear Cliente")
        print("\t[2] Actualizar datos")
        print("\t[3] Buscar Cliente")
        if operation == "x":
            quit()
        operation = input("Selection: ")

# Registramos en la bbdd los datos de cliente
# db.child("clientes").push(client)
