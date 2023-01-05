from django.shortcuts import render
from project.models import Project

def project_index(request):
    project = Project.objects.all()
    konteks = {
        'project' : project
    }
    return render(request, 'project_index.html', konteks)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    konteks = {
        'Project' : project
    }
    return render(request, 'detail_project.html', konteks)