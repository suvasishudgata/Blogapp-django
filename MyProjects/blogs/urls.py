from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('register/', register, name="register"),
    path('add_blog', add_blog, name="add_blog"),
    path('blog_detail/<slug>', blog_detail, name="blog_detail"),
    path('see_blog/', see_blog, name="see_blog"),
    path('blog_delete/<id>/', blog_delete, name = "blog_delete"),
    path('update_blog/<slug>/', blog_update, name = "blog_update"),
    path('logout_view/', logout_view, name="logout_view"),

]