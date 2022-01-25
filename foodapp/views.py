from django.shortcuts import render
from django.views import View
# Create your views here.


class MainView(View):

    def get(self, request):
        return render(request, 'project.html')


class ServicesView(View):

    def get(self, request):
        return render(request, 'services.html')