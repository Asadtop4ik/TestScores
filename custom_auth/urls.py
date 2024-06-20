from django.urls import path, include

urlpatterns = [
    path('custom_auth/', include('djoser.urls')),
    path('custom_auth/', include('djoser.urls.jwt')),
]
