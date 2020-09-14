from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 125)
    email = models.EmailField(max_length = 55)
    contact = models.IntegerField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    status = models.IntegerField(default = 0,null = True, blank = True)
    def __str__(self):
        return self.name
