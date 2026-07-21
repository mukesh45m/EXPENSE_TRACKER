from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # description = models.CharField(max_length=200)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
