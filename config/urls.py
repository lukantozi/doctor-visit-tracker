from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

handler404 = 'app.views.custom_404'
handler403 = 'app.views.custom_403'
handler400 = 'app.views.custom_400'
