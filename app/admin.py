from django.contrib import admin

from .models import Candidate, Email, Chat


class ChatAdmin(admin.ModelAdmin):
    list_display = ['candidate_email', 'chat']


admin.site.register(Candidate)
admin.site.register(Email)
admin.site.register(Chat, ChatAdmin)
