from django.urls import path
from user.views import aboutpage, Contact, homepage, profile, edit_profile, profiles_list

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', aboutpage, name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profiles/', profiles_list, name='profiles'),
]