from django.urls import path, include
from account import views
urlpatterns=[
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('notifications/',views.notifications, name = 'notifications' ),
    path('invite/<str:id>/accept/',views.accept_invite, name='accept_invite' ),
    path('invite/<str:id>/reject/', views.reject_invite, name = 'reject_invite')

]