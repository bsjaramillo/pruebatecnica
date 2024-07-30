from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()

router.register('libros', LibroViewSet)
router.register('categorias', CategoriaViewSet)
router.register('autores', AutorViewSet)
router.register('editoriales', EditorialViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/libros/find_by_autor/<int:pk>/',
         LibroViewSet.as_view({'get': 'find_by_autor'})),
    path('api/libros/find_by_category/<int:pk>/',
         LibroViewSet.as_view({'get': 'find_by_category'})),
    path('api/libros/find_by_editorial/<int:pk>/',
         LibroViewSet.as_view({'get': 'find_by_editorial'})),
    path('api/autores/find_by_category/<int:pk>/',
         AutorViewSet.as_view({'get': 'find_by_category'}))
]
