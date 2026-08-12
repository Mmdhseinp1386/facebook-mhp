from django.urls import path
from core.views import say_hello, home, post_list, post_detail, new_post, post_delete

urlpatterns = [
    path('hello/', say_hello, name='say_hello'),
    path('home/<username>', home, name='home'),
    path('post/', post_list, name='post_list'),
    path('post/detail/<int:post_id>/', post_detail, name='post_detail'),
    path('new/post/', new_post, name='new_post'),
    path('post/delete/<int:post_id>/', post_delete, name='post_delete')
]