from django.db import models

# Create your models here.
class Report(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=14)
    timeStamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Reports"

class UserDetails(models.Model):
    username = models.CharField(max_length=30)
    adhaar_number = models.IntegerField(default=0)
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = "User Details"