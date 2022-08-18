from django.shortcuts import render

from myapp.models import MyModel


def myapp_view(request):
    models = MyModel.objects.all()
    return render(request, "index.html", {"models": models})
