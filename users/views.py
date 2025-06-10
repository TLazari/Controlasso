from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'users/pages/register.html', {})