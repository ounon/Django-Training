from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def index(request):
    date = datetime.today()
    return render(request, "MyApp/index.html", context={"date": date})
