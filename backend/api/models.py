from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserData(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)  # Increase the max_length to accommodate hashed passwords
    user_id = models.AutoField(primary_key=True)  
    email = models.EmailField(unique=True)  

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Check if the provided password matches the hashed password
        return check_password(raw_password, self.password)

    def __str__(self) -> str:
        return f"{self.user_name} , {self.user_id} , {self.email}"
