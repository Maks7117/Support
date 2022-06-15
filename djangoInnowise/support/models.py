from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Ticket(models.Model):
    message = models.CharField(verbose_name='Message', db_index=True, max_length=120)

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)