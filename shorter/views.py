from django.shortcuts import render
from django.http import HttpResponse


from .forms import UrlCreateForm


# def hello(request):
#     return HttpResponse('Hello World')

def url_create(request):
    form = UrlCreateForm(request.POST or None)
    data = {'form':form}
    if request.method == 'POST' and form.is_valid():
        instanse = form.save()
        data('code') = instanse.code_url
    return render(request,"url.html", data)
        
        