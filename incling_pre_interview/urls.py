"""incling_pre_interview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import serializers, viewsets, routers
from tasks.models import Task, Tile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'type', 'tile', 'id', )


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ('status', 'launch_date', 'id', )


class TileViewset(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewset)
router.register(r'tiles', TileViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
