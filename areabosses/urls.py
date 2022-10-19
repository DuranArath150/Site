from django.urls import URLPattern, path

from areabosses import views

app_name = "ab"

urlpatterns = [
    path("create_areabosses/", views.CreateAreaBoss.as_view(), name="create_areabosses"),
    
]