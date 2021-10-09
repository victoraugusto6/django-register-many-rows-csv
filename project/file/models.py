from django.db import models


class File(models.Model):
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file)
