from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json

@require_POST
def login_view (request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    
    if username is None or password is None:
        return JsonResponse({'detail':'Please provide username and password'})
        
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({'detail':'Invalid credentials'}, status=400)
    
    login(request, user)
    return JsonResponse({'detail':'Succesfully logged in'}, status=200)

def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail':'You are not logged out'})
    logout(request)
    return JsonResponse({'detail':'Succesfully logged out'})

@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'is_authenticated':False})
    return JsonResponse({'is_authenticated':True})

def profile_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'is_authenticated':False})
    return JsonResponse({'username':request.user.username})