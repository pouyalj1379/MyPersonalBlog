from django.shortcuts import render
from .models import *
from home_app.models import Info


def story(request, id):
    infos = Info.objects.all().last()
    details = Story.objects.get(id=id)
    return render(request, "single_post_app/single-post.html", context={"details": details, "infos": infos})