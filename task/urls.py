from django.conf.urls.static import static
from django.urls import path
from task import views
from teamtasker_2 import settings

urlpatterns=[
    path('id/<str:task_id>/',views.task_view, name='task_detail'),
    path('create/', views.create_task, name='create-task'),
    path('id/<str:task_id>/solve/',views.solve_task, name='solve-task')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)