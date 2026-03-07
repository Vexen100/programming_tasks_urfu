from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_list, name='email-list'),
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent, name='sent'),
    path('<int:pk>/', views.email_detail, name='email-detail'),
    path('<int:pk>/move/', views.move_email, name='email-move'),
    path('<int:pk>/delete/', views.delete_email, name='email-delete'),
]

