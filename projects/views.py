from django.http import HttpResponse
from django.shortcuts import redirect, render

from projects.forms import ProjectForm
from projects.models import Project

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {
        "project" : projectObj,
    }
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    

    context = {
        'form' : form
    }
    return render(request, 'projects/project_form.html', context)