from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# ************************table class********************************

class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True)
    classe = (
        ('TC1', 'TC1'),
        ('TC2', 'TC2'),
        ('DIC1-GC', 'DIC1-GC'),
        ('DIC1-GEM', 'DIC1-GEM'),
        ('DIC1-GIT', 'DIC1-GIT'),
        ('DIC1-AERO', 'DIC1-AERO'),
        ('DIC2-GC', 'DIC2-GC'),
        ('DIC2-GEM', 'DIC2-GEM'),
        ('DIC2-GIT', 'DIC2-GIT'),
        ('DIC2-AERO', 'DIC2-AERO'),
        ('DIC3-GC', 'DIC3-GC'),
        ('DIC3-GEM', 'DIC3-GEM'),
        ('DIC3-GIT', 'DIC3-GIT'),
        ('DIC3-AERO', 'DIC3-AERO'),
    )
    nom_classe = models.CharField(max_length=10, choices=classe)

    def __str__(self):
        p = self.nom_classe
        return p


# **********************table eleve*******************************

class Eleve(models.Model):
    eleve_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_eleve = models.ForeignKey(Classe, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100, default='ma bio')
    photo_e = models.ImageField(upload_to='upload', default=None)

    def __str__(self):
        return self.eleve_user


# **************************table Matiere********************************

class Matiere(models.Model):
    id_matiere = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=200)
    id_classe = models.ForeignKey(Classe, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.libelle


# **************************table prof**************************

class Prof(models.Model):
    mat_ens = models.CharField(max_length=200)
    prof_user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100, default='ma bio')
    photo_p = models.ImageField(upload_to='upload', default=None)

    def __str__(self):
        return self.prof_user


class Enseigner(models.Model):
    id_prof = models.ForeignKey(Prof, on_delete=models.CASCADE, default=1)
    id_matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, default=1)


class Document(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='document/pdfs')
    matiere_doc = models.ForeignKey(Matiere, on_delete=models.CASCADE, default=1)
    ext = (
        ('ppt', 'ppt'),
        ('docx', 'docx'),
        ('pdf', 'pdf'),
        ('zip', 'zip'),
        ('xls', 'xls'),
        ('autre', 'autre')
    )
    extension_doc = models.CharField(max_length=10, choices=ext, default='autre')
    choix = (
        ('Cours', 'cours'),
        ('Tp', 'Tp'),
        ('Td', 'Td')
    )
    type_doc = models.CharField(max_length=10, choices=choix, default='Cours')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

# ****************************************************
