from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import ReservationForm

# Function-based view
def hello_world(request):
    return render(request, 'hello_world.html', {'message': "Hello, World! I'm from function-based view!"})

def hello_world2(request):
    return HttpResponse("Hello, World! I'm from function-based view! (hello_world2)")


# Class-based view
class HelloWorldView(View):
    def get(self, request):
        return render(request, 'hello_world.html', {'message': "Hello, World! I'm from class-based view!"})
    
class ReservationView(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'reservation.html', {'form': form})
    
    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reservation.html', {'success': True, 'form': form})
        else:
            return render(request, 'reservation.html', {'success': False, 'form': form})
