import firebase_admin
from firebase_admin import credentials, firestore

# Ruta al archivo de credenciales
cred = credentials.Certificate('/home/j131/IWG400/climaeduca/educacion/serviceAccountKey.json')

# Inicializar la app de Firebase
firebase_admin.initialize_app(cred)

# Cliente de Firestore
db = firestore.client()
