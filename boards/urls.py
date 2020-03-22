
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('boards/<int:id>/', views.boards_topic, name='boards_topic'),
    path('boards/<int:id>/new_topic/', views.new_topic, name='new_topic'),
    path('boards/<int:id>/topics/<int:topic_id>/',
         views.topic_posts, name='topic_posts'),
    path('boards/<int:id>/topics/<int:topic_id>/reply',
         views.reply, name='reply')
]
