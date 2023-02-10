from django.db import models


class Repo(models.Model):
    repo_title = models.CharField(max_length=50, unique=True)
    repo_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="repos"
    )

    def _repr_(self):
        return f"<Group ({self.id}) - {self.scientific_name}>"
