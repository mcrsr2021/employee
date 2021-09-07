from django.db import models

class users(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=125)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['created']