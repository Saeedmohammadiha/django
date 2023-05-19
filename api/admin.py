from django.contrib import admin
from .models import City, Group, User, Rest, Status,FollowUp, Message, Meal
# Register your models here.

admin.site.register(City)
admin.site.register(Message)
admin.site.register(FollowUp)
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Rest)
admin.site.register(Status)
admin.site.register(Meal)