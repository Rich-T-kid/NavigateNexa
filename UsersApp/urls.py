from django.urls import path


from . import views

urlpatterns = [
    path("", views.Userhome, name="index"),
    path("hp",views.Homepage,name="user_home")
]