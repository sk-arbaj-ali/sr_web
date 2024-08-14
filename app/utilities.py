from django.contrib.auth import login, authenticate, logout

def check_if_authenticated(request):
    if request.user.is_authenticated:
        return True
    
    return False