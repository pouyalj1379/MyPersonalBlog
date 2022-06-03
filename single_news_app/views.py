from django.shortcuts import render
from .models import *
from home_app.models import Info

def new(request, id):
    infos = Info.objects.all().last()
    details = Template.objects.get(id=id)
    return render(request, "single_news_app/single-news.html", context={"details": details, "infos":infos})