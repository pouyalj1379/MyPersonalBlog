from django.contrib import admin
from .models import *


class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "number", "message")


admin.site.register(Message, MessageAdmin)
admin.site.register(Poem)
admin.site.register(Info)
admin.site.register(ProgrammingExperience)
admin.site.register(OtherExperience)
admin.site.register(HomePageInfo)