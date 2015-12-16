from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.

class usuario(models.Model):

    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=50)
    email = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

    def save(self, *args, **kwargs):
        self.guid = hashlib.md5(str(random()).encode('utf-8')).hexdigest()
        super(usuario, self).save(*args, **kwargs)

class anuncio(models.Model):
    #usuario = models.OneToOneField(User)
    usuario = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'

    def save(self, *args, **kwargs):
        self.usuario = User.get_username(self)
        self.save()



