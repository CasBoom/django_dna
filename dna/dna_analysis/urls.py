from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:profile_id>', views.detail, name="detail")
]