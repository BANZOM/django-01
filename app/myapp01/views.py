from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Function-based view
def hello_world(request):
    return render(request, 'hello_world.html', {'message': "Hello, World! I'm from function-based view!"})

def hello_world2(request):
    return HttpResponse("Hello, World! I'm from function-based view! (hello_world2)")


# Class-based view
class HelloWorldView(View):
    def get(self, request):
        return render(request, 'hello_world.html', {'message': "Hello, World! I'm from class-based view!"})