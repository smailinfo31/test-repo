
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("cars/", include("cars.urls")),
    path('', include('leads.urls')),
    path('', include('fronend.urls')),

]
