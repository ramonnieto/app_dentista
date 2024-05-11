import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint
from FirestoreDB import FirestoreClient
cred = credentials.Certificate("token_app_clinic.json")
firebase_admin.initialize_app(cred)

