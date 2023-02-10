from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()

    def _repr_(self):
        return f"<User ({self.id}) - {self.name}>"
