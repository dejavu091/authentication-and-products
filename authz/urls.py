from django.urls import path
from authz.views import Signup,logoutView,loginView

urlpatterns=[
    path('signup/',Signup.as_view(), name='signup'),
    path('login/', loginView.as_view(), name='login'),
    path('logout/',logoutView,name='logout')
]