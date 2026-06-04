from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    is_treated = models.BooleanField(default=False)
