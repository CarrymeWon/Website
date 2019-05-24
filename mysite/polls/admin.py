from django.contrib import admin
from .models import Question, Hackathon
# question need be managed, so put here

# Register your models here.
admin.site.register(Question)
admin.site.register(Hackathon)