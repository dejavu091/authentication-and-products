from django.urls import path
from user.views import aboutpage, Contact
from user.views import homepage
urlpatterns = [
    path('', homepage, name='home'),
    path('about/', aboutpage, name='about'),
    path('contact',Contact.as_view(), name='contact')
]