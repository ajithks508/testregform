from django.urls import path
from .import views

urlpatterns = [
  path('',views.Home,name=''),
  path('registration/',views.register,name='registration/'),
  path('userLogin/',views.loginuser,name='userLogin/'),
  path('edittenant/',views.tenant,name='edittenant/'),
  path('delete',views.deleteuser,name='delete/'),
  ]