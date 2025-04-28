from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Bird, Toy
from .forms import FeedingForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

@login_required
def bird_index(request):
    birds = Bird.objects.filter(user=request.user))
    return render(request, 'birds/index.html', {'birds':birds})

@login_required
def bird_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html', {
        'bird': bird, 
        'feeding_form': feeding_form
        'toys': toys_bird_doesnt_have
    })

@login_required
def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('bird-detail', bird_id=bird_id)

@login_required
def associate_toy(request, bird_id, toy_id):
    Bird.objects.get(id=bird_id).toys.add(toy_id)
    return redirect('bird-detail', bird_id=bird_id)

@login_required
def remove_toy(request, bird_id, toy_id):
    return redirect('bird-detail', bird_id=bird.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
    if form.is_valid():
           user = form.save()
            login(request, user)
            return redirect('bird-index')
        else:
            error_message = 'Invalid sign up - try again'
             form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class BirdCreate(LoginRequiredMixin, CreateView):
    model = Bird
    field = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BirdUpdate(LoginRequiredMixin, UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class BirdDelete(LoginRequiredMixin, DeleteView):
    model = Bird
    success_url = '/birds/'

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toyfields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
    models = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

class Home(LoginView):
    template_name = 'home.html'
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
