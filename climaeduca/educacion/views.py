# climaeduca/views.py
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def api_login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
    except:
        return JsonResponse({'error': 'JSON inválido'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'success': True, 'message': 'Inicio de sesión correcto'})
    else:
        return JsonResponse({'success': False, 'message': 'Credenciales incorrectas'}, status=401)
