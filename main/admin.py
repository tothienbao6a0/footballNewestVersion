from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(List)
admin.site.register(Question)
admin.site.register(Score)
#this page registers all the models in the site 