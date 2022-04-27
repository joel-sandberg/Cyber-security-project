from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.db import transaction
from .models import Account


# Create your views here.
@transaction.atomic
def transfer(sender, receiver, amount):
        acc1 = Account.objects.get(iban=sender)
        acc2 = Account.objects.get(iban=receiver)

        if (amount >= 0 and amount <= acc1.balance):
                acc1.balance -= amount
                acc2.balance += amount
                acc1.save()
                acc2.save()

# def loginPageView(request):
  # if request.method == 'POST':
          # name = request.POST('name')
          # passw = request.POST('pass')
          # user = authenticate(request, username=name, password=passw)
          # if user is not None:
                  # login(request, user)
                  # return redirect('/home/')
          # else:
                 # return()
  
def loginPageView(request):

        if request.method == 'GET':
                name = request.GET.get('name')
                passw = request.GET.get('pass')
                if name == 'admin' and passw == 'admin':
                        return redirect('/home/')
                if name == 'guest' and passw == 'guest':
                        return redirect('/guest/')
        return render(request, 'pages/login.html')

def guestPageView(request):
        accounts = Account.objects.all()
        context = {'accounts': accounts}
        return render(request, 'pages/guest.html', context)

def errorPageView(request):
        return render(request, 'pages/error.html')


def homePageView(request):
        if request.method == 'POST':
                sender = request.POST.get('from')
                receiver = request.POST.get('to')
                amount = int(request.POST.get('amount'))
                transfer(sender, receiver, amount)

        accounts = Account.objects.all()
        context = {'accounts': accounts}
        return render(request, 'pages/index.html', context)
