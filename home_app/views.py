from django.shortcuts import render
from .models import *
from single_post_app.models import *
from single_news_app.models import *
from django.core.paginator import Paginator


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        number = request.POST.get("number")
        Message.objects.create(name=name, email=email, message=message, number=number)

    home_page_info = HomePageInfo.objects.all()
    stories = Story.objects.all()
    programmingexperience = ProgrammingExperience.objects.all()
    otherexperience = OtherExperience.objects.all()
    infos = Info.objects.all().last()
    poems = Poem.objects.all()
    templates = Template.objects.all()

    page = request.GET.get("story_page")
    story_paginator = Paginator(stories, 5)
    story_objects_list = story_paginator.get_page(page)

    page_number = request.GET.get("page")
    paginator = Paginator(templates, 3)
    objects_list = paginator.get_page(page_number)


    return render(request, "home_app/index.html",
                  context={"poems": poems, "news": objects_list, "infos": infos,
                           "programmingexperience": programmingexperience,
                           "otherexperience": otherexperience,
                           "stories": story_objects_list, "home_page_info": home_page_info})


def story(request, id):
    tail = Story.objects.get(id=id)
    return render(request, "single_post_app/single-post.html", context={"tail": tail})


def template(request, id):
    report = Template.objects.get(id=id)
    return render(request, "single_news_app/single-news.html", context={"report": report})
