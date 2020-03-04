from django.contrib import admin

from .models import *

# Register your models here.


admin.site.site_header = 'Polydoc Admin Dashboard'
admin.site.site_title = 'Polydoc Admin'
admin.site.index_title = 'Polydoc Admin'


class classe(admin.ModelAdmin):
    list_display = ['id_classe', 'nom_classe']
    search_fields = ('nom_classe',)


admin.site.register(Classe, classe)


class matiere(admin.ModelAdmin):
    list_display = ['id_matiere', 'id_classe', 'libelle']
    search_fields = ('libelle',)


admin.site.register(Matiere, matiere)


class eleve(admin.ModelAdmin):
    list_display = ('eleve_user', 'class_eleve', 'bio')
    search_fields = ('eleve_user',)


admin.site.register(Eleve, eleve)


class prof(admin.ModelAdmin):
    list_display = ('prof_user', 'mat_ens', 'bio')
    search_fields = ('prof_user',)


admin.site.register(Prof, prof)


class doc(admin.ModelAdmin):
    list_display = ['title', 'author', 'pdf', 'extension_doc', 'matiere_doc']
    search_fields = ('title',)


admin.site.register(Document, doc)
