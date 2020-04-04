from django.urls import path, include
import dna_analysis.views
from . import views

urlpatterns = [
    path('<int:profile_id>', views.detail, name="detail"),
]