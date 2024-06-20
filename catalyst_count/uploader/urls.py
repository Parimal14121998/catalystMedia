from django.urls import path
from .views import upload_file, upload_success, manage_users, query_builder

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('success/', upload_success, name='upload_success'),
    path('users/', manage_users, name='manage_users'),
    path('query/', query_builder, name='query_builder'),

]
