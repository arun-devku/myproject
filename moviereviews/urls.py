from django.urls import path
from moviereviews import views

urlpatterns = [
   
path('pro1', views.base, name='base'),
path('pro2', views.index, name='index'),
path('pro3/<int:id>', views.details, name='details'),
path('pro4', views.login, name='login'),
path('pro5', views.register, name='register'),
path('pro6', views.index2, name='index2'),
path('pro7', views.account, name='account'),
path('pro8', views.yourpost, name='yourpost'),
path('pro10/<int:id>', views.details_Post, name='details_Post'),
path('<int:id>', views.edit_post, name='edit_post'),
path('pro11/<int:id>', views.delete_post, name='delete_post'),
path('pro12', views.home, name='home'),
path('pro13/<int:id>', views.details_2, name='details_2'),
path('pro14', views.account_edit, name='account_edit'),
path('pro15', views.loginOut, name='loginout'),
path('checkusername', views.checkusername,name='checkusername'),




]