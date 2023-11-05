from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hot', views.hot, name='hot'),
    path('question/<int:question_id>', views.question, name='question'),
    path('tag/<str:tag_title>', views.tag, name='tag'),
    path('ask', views.ask, name='ask'),
    path('setting', views.setting, name='setting'),
    path('signup', views.singup, name='signup'),
    path('login', views.login, name='login'),
    path('admin/', admin.site.urls),
]
