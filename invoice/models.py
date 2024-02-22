from django.db import models


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    question = models.TextField()

    def __str__(self):
        return self.question
