from . import views
from django.urls import path

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='post_by_category')
]