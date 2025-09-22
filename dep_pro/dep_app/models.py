from django.db import models

# Create your models here.
from django.db import models

class PracAppUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=50)
    mobile = models.CharField(unique=True, max_length=10)
    password = models.CharField(max_length=255)
    profile_pic = models.URLField(max_length=500, blank=True, null=True)  # store Cloudinary URL

    class Meta:
        db_table = "prac_app_user"