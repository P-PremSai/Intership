from django.contrib import admin
from .models import User,Room, Topic, Message,Feedback


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Feedback)
# Register your models here.
