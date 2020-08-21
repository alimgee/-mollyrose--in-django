from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('main.urls')),
    path('news/' , include('news.urls')),
    path('story/' , include('story.urls')),
    path('helpout/' , include('help.urls')),
    path('childhoodcancer/' , include('cancer.urls')),
    path('accounts/', include('allauth.urls')),
]
