from django.shortcuts import render
from .models import Job

from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application
from .forms import ApplicationForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def job_list(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()

            # Email notification to admin
            send_mail(
                subject='New Job Application',
                message=f'{request.user.username} applied to {job.title}',
                from_email='your_email@gmail.com',
                recipient_list=['your_email@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'jobs/job_success.html', {'job': job})
    else:
        form = ApplicationForm()

    return render(request, 'jobs/job_apply.html', {'form': form, 'job': job})
