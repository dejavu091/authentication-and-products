from django.shortcuts import render,redirect,resolve_url
from jobs.models import Job, Apply as ApplyModel
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from user.views import homepage
from django.forms.models import model_to_dict
from django.http import JsonResponse



class Jobs (LoginRequiredMixin,View):
    def get(self,request):
        all_jobs = Job.objects.all().order_by("-created_at")
        context = {
            'all_jobs':all_jobs
        }
        return render(request,'jobs.html',context)
    
class postJOb(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'post_job.html')
    def post (self,request):
        name=request.POST.get('name')
        description=request.POST.get('description')
        salary=request.POST.get('salary')
        qualification=request.POST.get('qualification')
        image=request.FILES.get('image')
        if not name or not description or not salary or not qualification or not image:
            messages.error(request,"all field required")
            return redirect(resolve_url('post-jobs'))
        try:
            salary = int(salary)
        except:
            messages.error(request,'salary must be intergers')
            return redirect(resolve_url('post-jobs'))
        if salary < 1:
                messages.error(request,"salary too low")
        Job.objects.create(name=name, description=description, salary=salary, qualification=qualification,image=image,
                                   user=request.user)
        messages.success(request,'job listed successfully')
        return redirect(resolve_url('post-jobs'))
            
class EditJob(LoginRequiredMixin,View):
     def get(self,request,job_id):
          job = Job.objects.filter(id=job_id).first()
          if not job:
               return redirect(resolve_url('jobs'))
          if job.user != request.user:
               return redirect(resolve_url('jobs'))
          context={'product':job}
          return render(request,'edit_jobs.html',context)
     def post (self,request,job_id):
          product = Job.objects.filter(id=job_id).first()
          if not product:
               return redirect(resolve_url('jobs'))
          if product.user != request.user:
               return redirect(resolve_url('jobs'))
          name=request.POST.get('name')
          description=request.POST.get('description')
          salary=request.POST.get('salary')
          if salary:
               try:
                    salary = int(salary)
               except ValueError:
                    messages.error(request,'salary must be an integer')
                    return redirect(resolve_url('edit-job', job_id=job_id))
               if salary < 1:
                    messages.error(request,'salary too low')
                    return redirect(resolve_url('edit-job', job_id=job_id))
          qualification=request.POST.get('qualification')
          image=request.FILES.get('image')
          product.name=name or product.name
          product.description=description or product.description
          product.salary=salary or product.salary
          product.qualification=qualification or product.qualification
          product.image=image or product.image
          product.save()
          messages.success(request,'job successfully updated')
          return redirect(resolve_url('jobs'))
     


@login_required    
def delete_job(request,job_id):
     job = Job.objects.filter(id=job_id).first()
     if not job:
          return redirect(resolve_url('jobs'))
     if job.user != request.user:
          return redirect(resolve_url('jobs'))
     job.delete()
     messages.success(request,'job deleted successfully')
     return redirect(resolve_url('jobs'))


def list_jobs(request):
     all_jobs = Job.objects.all()
     data=[{'name' : x.name,'id': x.id , 'qualification': x.qualification, 'image':x.image.url}for x in all_jobs]
     return JsonResponse(data,safe=False)


class Apply(LoginRequiredMixin, View):
    def get(self, request, job_id):
        job = Job.objects.filter(id=job_id).first()
        if not job:
            return redirect(resolve_url('jobs'))
        if job.user == request.user:
            messages.error(request, 'why are you applying for your own job!')
            return redirect(resolve_url('jobs'))
        return render(request, 'apply_job.html', {'job': job})

    def post(self, request, job_id):
        job = Job.objects.filter(id=job_id).first()
        if not job:
            return redirect(resolve_url('jobs'))
        if job.user == request.user:
            messages.error(request, 'why are you applying for your own job!')
            return redirect(resolve_url('jobs'))

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dob = request.POST.get('dob')
        school = request.POST.get('school')
        qualification = request.POST.get('qualification')
        years = request.POST.get('years')
        image = request.FILES.get('image')

        if not firstname or not lastname or not dob or not school or not qualification or not years or not image:
            messages.error(request, 'all field are required')
            return render(request, 'apply_job.html', {'job': job})
        if len(firstname) < 2 or len(lastname) < 2 or len(school) < 2 or len(qualification) < 2:
            messages.error(request, 'character too short')
            return render(request, 'apply_job.html', {'job': job})
        if len(firstname) > 250 or len(lastname) > 250 or len(school) > 250 or len(qualification) > 250:
            messages.error(request, 'character too long')
            return render(request, 'apply_job.html', {'job': job})

        ApplyModel.objects.create(
            firstname=firstname,
            lastname=lastname,
            dob=dob,
            school=school,
            qualification=qualification,
            years=years,
            image=image,
            job=job,
        )
        messages.success(request, 'job application sent successfully')
        return redirect(resolve_url('jobs'))
    


    
def error_404(request,exception):
     return render(request,'error_404.html')

def error_500(request):
     return render(request,'error_500.html')
    




    
    



# Create your views here.
