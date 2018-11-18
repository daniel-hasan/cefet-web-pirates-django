"""web_pirates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from pirates import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ListarTesouros.as_view(),name="lista_tesouros"),
    path('inserir',views.SalvarTesouro.as_view(),name="inserir"),
    path('editar/<int:id>/',views.SalvarTesouro.as_view(),name="editar"),
    path('remover/<int:id>/',views.RemoverTesouro.as_view(),name="excluir"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
