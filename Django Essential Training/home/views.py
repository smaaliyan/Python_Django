from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()} 

# def home(request): 
    # return render(request, 'home/welcome.html', {'today': datetime.today()})

class Autherize(LoginRequiredMixin, TemplateView):
    template_name = 'home/autherize.html'
    login_url = '/admin'

# @login_required(login_url='/admin')
# def autherize(request):
#     return render(request, 'home/autherize.html', {})
