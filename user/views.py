from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from user.models import contactMessage
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from user.forms import UserProfileForm


@login_required
def homepage(request):
    print(request.method)
    return render(request, 'home.html')


@login_required
def profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'user_profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def profiles_list(request):
    """List view showing all user profiles (name, location, picture)."""
    profiles = UserProfile.objects.select_related('user').all()
    return render(request, 'profiles_list.html', {'profiles': profiles})


def aboutpage(request):
    return render(request, 'about.html')
# def contactpage(request):
#     if request.method=="POST":
#            name =request.POST.get("name")
#            email= request.POST.get("email")
#            comment= request.POST.get("comment")
#            if not name or not email or not comment:
#                 messages.error(request,'all field required')
#                 return render(request,'contact.html')
#            if len(name)<2:
#                 messages.error(request,'enter a valid name')
#                 return render(request,'contact.html')
#            messages.success(request,'we have received your message ,we will get back to you ')
#            return redirect('home')
#     return render(request,'contact.html')
     
class Contact(View):
     def get(self,request):
          return render(request,'contact.html')
     def post(self,request):
          name =request.POST.get('name')
          email =request.POST.get('email')
          comment =request.POST.get('comment')
          # password=request.POST.get('password')
          if not name or not email or not comment:
               messages.error (request,'all field are required')
               return render(request,'contact.html')
          if len(name)<2:
               messages.error(request,'name too short')
               return render(request,'contact.html')
          if len(name)>250:
               messages.error(request,'name too long')
               return render(request,'contact.html')
          contactMessage.objects.create(name=name, email=email,message=comment)
          
          
          messages.success(request,'welcome')
          return redirect(homepage)
               


# Create your views here.
