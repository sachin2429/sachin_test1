from django.contrib import admin
from django.urls import path
from .views import add_book,save_book,stud_info,save_stud,view_update_book,view_book,update_book,register_user,login_user,logout_user


urlpatterns = [
    path('add_book', add_book),
    path('save_book',save_book),
    path('stud_info',stud_info),
    path('save_stud',save_stud),
    path('',view_book),
    path('view_update_book/<int:id>',view_update_book),
    path('update_book/<int:id>',update_book),
     path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
    
]