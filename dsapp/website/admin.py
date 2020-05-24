from django.contrib import admin
from . models import Flashcard, User, Topic, Subtopic, Question, Interview

# Register your models here.
admin.site.register(Flashcard)
admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Question)
admin.site.register(Interview)