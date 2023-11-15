from django.contrib import admin

# Register your models here.

from .models import Question, Answer, Tag, Like_answer, Like_question, Profile

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Like_answer)
admin.site.register(Like_question)
admin.site.register(Profile)