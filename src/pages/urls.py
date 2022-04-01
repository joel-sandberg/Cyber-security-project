from django.urls import path

from .views import homePageView, loginPageView, guestPageView, errorPageView

urlpatterns = [
    path('guest/', guestPageView, name='guest'),
    path('home/', homePageView, name='home'),
    path('', loginPageView, name='login'),
    path('error/', errorPageView, name='error'),
]
