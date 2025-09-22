from django.urls import path 
from .    import views 
urlpatterns=[
    path("",view=views.welcome),
    path("register_user/",view=views.reg_user)
]