from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/task', views.TaskList.as_view()),
    path('api/task/<int:pk>/', views.TaskDetail.as_view()),
    path('api/scanput', views.ScanputList.as_view()),
    path('api/scanput/<int:pk>/', views.ScanputDetail.as_view()),
    path('api/scanport', views.ScanportList.as_view()),
    path('api/scanport/<int:pk>/', views.ScanportDetail.as_view()),
    path('api/setting', views.SettingList.as_view()),
    path('api/setting/<int:pk>/', views.SettingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)