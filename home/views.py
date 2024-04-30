from django.shortcuts import render
from .models import OurHeroes, Contact


def home(request):
    our_heroes = OurHeroes.objects.all()
    context = {
        'our_heroes': our_heroes
    }
    return render(request, 'home/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, email, phone, message)
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'home/contact.html')
