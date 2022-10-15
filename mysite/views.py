from django.shortcuts import render

# Create your views here.


def get_mysite_base(request):
    return render(request, 'mysite/mysite_base.html')
