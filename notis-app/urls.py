from django.urls import path
from . import views

# Этот список пока пуст, но именно здесь мы будем добавлять пути для REST API 
# на следующем этапе, когда создадим views.py
urlpatterns = [
    
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'notes', views.NoteViewSet, basename='note')

urlpatterns = [
    # Этот путь отвечает за все CRUD-операции с заметками:
    # GET /api/notes/, POST /api/notes/, GET /api/notes/1/, PUT /api/notes/1/, DELETE /api/notes/1/
    path('', include(router.urls)),
]
