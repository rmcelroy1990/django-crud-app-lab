from django.shortcuts import render

from django.http import HttpResponse
def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def bird_index(request):
    return render(request, 'birds/index.html', {'birds':birds})

class Bird:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


birds = [
    Bird('Lolo', 'tabby', 'Kinda rude.', 3),
    Bird('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Bird('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Bird('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]
