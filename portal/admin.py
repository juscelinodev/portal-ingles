from django.contrib import admin

# Register your models here.

from .models import Usuario
from .models import Categoria
from .models import Curso
from .models import Aula


class CursoAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class CategoriaAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Usuario)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Aula)
