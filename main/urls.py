from django.urls import path

from . import views


app_name = 'main'

urlpatterns = (
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'company/create/', views.CompanyCreateView.as_view(), name='company-create'),
    path(r'company/<int:pk>/update/', views.CompanyUpdateView.as_view(), name='company-update'),
    path(r'company/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company-delete'),
)
