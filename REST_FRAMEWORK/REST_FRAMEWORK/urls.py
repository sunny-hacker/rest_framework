from django.urls import path, include

urlpatterns = [
    path('', include('drf.urls')),
    path('api-auth/', include('rest_framework.urls')),
]