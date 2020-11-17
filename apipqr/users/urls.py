from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apipqr.users.views  import ClienteViewSet
router = DefaultRouter()
router.register(r'cliente', ClienteViewSet, basename='cliente')
urlpatterns=[

    path('', include(router.urls))
    # path('users/signup/',UserSingnupAPIView.as_view(), name='login'),
]
