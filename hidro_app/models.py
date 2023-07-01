from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.Charfield(max_length=200)
    rating = models.PisitiveSmallIntegrerField(blank=False,null=False)
    abv = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = "usuario_table"
    
    def __str__(self):
        return f"El miembro de la comunidad Hidropina es: {self.nombre}, Rating {self.abv}"
    
    def get_field(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
        