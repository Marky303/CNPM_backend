from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Djoser authentication endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
    # Printing application
    path('spss/', include('printing.api.urls')),
    
    # User authentication related
    path('account/', include('account.api.urls'))
]
