from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird

from django.http import HttpResponse
def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def bird_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds':birds})

def bird_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': bird})

class BirdCreate(CreateView):
    model = Bird
    field = ['name', 'breed', 'description', 'age']

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'


# class Bird:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# birds = [
#     Bird('Lolo', 'tabby', 'Kinda rude.', 3),
#     Bird('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Bird('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Bird('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]
