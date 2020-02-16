from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Departement(models.Model):
    dept = (
        ('TR', 'Tronc Commun'),
        ('GC', 'Génie Civil'),
        ('GEM', 'Génie Electromécanique'),
        ('FA', 'Filière Aréonautique'),
        ('GIT', 'Génie Informatique et Télécommunications'),
    )
    id_dept = models.AutoField(primary_key=True)
    nom_dept = models.CharField(max_length=3, choices=dept)


class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True)
    classe = (
        ('tc1', 'TC1'),
        ('tc2', 'TC2'),
        ('dic1', 'DIC1'),
        ('dic2', 'DIC2'),
        ('dic3', 'DIC3'),
    )
    nom_classe = models.CharField(max_length=4, choices=classe)
    id_dept = models.ForeignKey(Departement, on_delete=models.CASCADE)


class Prof(models.Model):
    mat_ens = models.CharField(max_length=200)
    prof_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Matiere(models.Model):
    id_matiere = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=200)
    id_prof = models.ForeignKey(Prof, on_delete=models.CASCADE)


class Class_mat(models.Model):
    id_classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    id_matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    num_semestre = models.CharField(max_length=20)


class Eleve(models.Model):
    eleve_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_eleve = models.ForeignKey(Classe, on_delete=models.CASCADE)

    def __str__(self):
        return self.eleve_user.username


class Profil(models.Model):
    bio = models.TextField()
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    profil_user =  models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.profil_user.username
