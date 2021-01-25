from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('delete/<List_id>',views.delete,name='delete'),
    path('Cross_Off/<List_id>',views.Cross_Off,name='Cross_Off'),
    path('Uncross/<List_id>',views.Uncross,name='Uncross'),
    path('edit/<List_id>',views.edit,name='edit'),

]
