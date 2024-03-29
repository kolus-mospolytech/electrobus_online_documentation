"""backend_liaz URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog import views

router = routers.DefaultRouter()
router.register(r'consumables', views.ConsumableViewSet)
router.register(r'parts', views.PartViewSet)
router.register(r'unit_types', views.UnitTypeViewSet)
router.register(r'units', views.UnitViewSet)


urlpatterns = [
                  path('grappelli/', include('grappelli.urls')),
                  path('_nested_admin/', include('nested_admin.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('admin/', admin.site.urls),
                  path('', include(router.urls)),
                  path('api/', include('rest_framework.urls', namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
