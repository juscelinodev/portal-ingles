"""projeto URL Configuration

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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static


# When importing a file, Python only searches the directory that the entry-point script 
# is running from and sys.path which includes locations such as the package installation directory
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'c:/dev/portal-ingles/portal')
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('categoria', views.categoria, name='categoria'),
    path('categoria/add', views.categoria_add, name='categoria_add'),
    path('categoria/edit/<int:categoria_pk>', views.categoria_edit, name='categoria_edit'),
    path('categoria/delete/<int:categoria_pk>', views.categoria_delete, name='categoria_delete'),
    path('curso', views.curso, name='curso'),
    path('cursos', views.cursos, name='cursos'),
    path('curso/add', views.curso_add, name='curso_add'),
    path('curso/edit/<int:curso_pk>', views.curso_edit, name='curso_edit'),
    path('curso/delete/<int:curso_pk>', views.curso_delete, name='curso_delete'),
    path('aula', views.aula, name='aula'),
    path('matricula', views.matricula, name='matricula'),
    path('matricula/add', views.matricula_add, name='matricula_add'),
    path('matricula/delete/<int:matricula_pk>', views.matricula_delete, name='matricula_delete'),
    path('aula/add', views.aula_add, name='aula_add'),
    path('aula/edit/<int:aula_pk>', views.aula_edit, name='aula_edit'),
    path('aula/delete/<int:aula_pk>', views.aula_delete, name='aula_delete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # para as thumbnails

