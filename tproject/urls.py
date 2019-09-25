from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tkitaka/', include('tkitaka.urls')),   # tkitaka 앱으로 매칭
    # path('post/', include('post.urls')),   # tkitaka 앱으로 매칭
    # path('chat/', include('chat.urls')),   # tkitaka 앱으로 매칭
]
