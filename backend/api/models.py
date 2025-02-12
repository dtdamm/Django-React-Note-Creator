from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # All the notes can be immediatly accessed from the user ibject with the name "notes", On delete cascade means that if a user is deleted, all the notes associated with that user will also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title