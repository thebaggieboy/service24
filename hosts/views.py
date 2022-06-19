from django.shortcuts import render, redirect
from django.views.generic import TemplateView,CreateView
from . import forms
# Create your views here.

def host_view(request):
    form = forms.HostForm()
    if request.method == 'POST':
        form = forms.HostForm(request.POST)

        if form.is_valid():
            host = form.save()
            redirect('hosts:get_started')
    return render(request, 'hosts/become_a_host.html', {'form':form})

class HostView(CreateView):
    template_name = 'hosts/become_a_host.html'

    