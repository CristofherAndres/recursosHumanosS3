from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sueldo = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + self.nombre + " $ " + str(self.sueldo)
