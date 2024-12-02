from django.shortcuts import render
from .models import *
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def list(request):
    cr = course.objects.all()
    return render(request, 'list.html' , {'courses':cr})

class update(UpdateView):
    model = course
    fields = ['name', 'tname']
    template_name = 'update.html'
    success_url = reverse_lazy('listc')