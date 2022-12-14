"""projeto_investe_eu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from inviste_eu import views
from usuarios import views as usuview
from django.contrib.auth import views as authview



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.investir, name='home'),
    path('login/', authview.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', authview.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('/<int:id>', views.detalhe, name='detalhes'),
    path('investimentos/<int:id>', views.editarinvest, name='editar' ),
    path('excluinvest/<int:id>', views.excluinvest, name='excluinvest' ),
    path('newinvest', views.criar, name='newinvest'),
    path('conta/', usuview.usuarionovo, name='usuarionovo'),
    path('semacesso/', usuview.acesso, name='semacesso')
]
