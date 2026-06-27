from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_document = models.CharField(max_length=20) #verificar cantidad de digitos de documentos
    user_email = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=9)
    user_adress = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.user_name} {self.user_last_name}'
    