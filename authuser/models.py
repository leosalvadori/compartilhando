from django.db import models
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