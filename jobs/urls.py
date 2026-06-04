from django.urls import path
from jobs.views import Jobs,postJOb,EditJob,delete_job,list_jobs,Apply



urlpatterns= [path('',Jobs.as_view(), name='jobs'),
              path('post-job/',postJOb.as_view(),name='post-jobs'),
              path('edit-job/<str:job_id>',EditJob.as_view(),name='edit-job'),
              path('delete-job/<str:job_id>',delete_job, name = 'delete-job'),
              path('all',list_jobs, name='all_jobs'),
              path('apply-job/<str:job_id>',Apply.as_view(),name='apply-job')

]