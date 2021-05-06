from django.shortcuts import render
from django.views import View

# Create your views here.
from .models import Room


def hello(request):
    rooms = Room.objects.all()

    print(rooms.count())

    return render(request, template_name='welcome.html', context={
        'name': 'Alex',
        'rooms': rooms,
    })
