from django.http import HttpResponse
from .firebase_config import db

def prueba_firebase(request):
    doc_ref = db.collection('usuarios').document('usuario1')
    doc_ref.set({
        'nombre': 'Vicente',
        'puntaje': 0
    })
    return HttpResponse("Datos guardados en Firebase")
