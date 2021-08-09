from .utils import generate_random_string

from django.db import models

class Url(models.Model):
    origin_url = models.URLField(unique=True)
    code = models.CharField(max_length=5, unique=True)


    def save(self, *args, **kwargs):
        while True:
            random_str = generate_random_string()
            if not Url.objects.filter(short_code=random_str).exists():
                self.short_code = random_str
                break
            else:
                continue
        super().save(*args, **kwargs)