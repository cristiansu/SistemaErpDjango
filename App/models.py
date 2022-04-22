from statistics import mode
from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_creation', null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True, null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_updated', null=True, blank=True)
    date_updated = models.DateField(auto_now=True, null=True, blank=True)


    class Meta:
        abstract = True #singnifica q no se creará la tabla, pero podrá ser usado por otras entidades