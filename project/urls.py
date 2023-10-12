from django.conf.urls.static import static
from django.urls import path, include

from project import views
from teamtasker_2 import settings

urlpatterns=[
    path('id/<str:project_id>/', views.project_view, name='project_detail'),
    path('id/<str:project_id>/task/', include("task.urls"), name='task'),
    path('create/', views.create_project, name='create-project'),
    path('id/<str:project_id>/roles', views.modify_roles, name='modify-roles'),
    path('id/<str:project_id>/add_user/', views.add_user, name='add_user')
]
