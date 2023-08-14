from django.urls import path, re_path

import women.views
from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/women/ - 500 errr
    path('articles/', articles, name='articles'),  # http://127.0.0.1:8000/articles/
    path('articles/<int:article_id>/', women.views.article_get),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]