from django.db import models
import string
import random

def generage_url():
    length = 10
    characterPool = string.ascii_letters + string.digits + string.punctuation
    code = ''.join(random.choice(characterPool) for i in range(length))
    while URL.objects.filter(code=code).exists():
        code = generage_url()
    return code

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    code = models.CharField(max_length=20, unique=True, default=generage_url)
    createdAt = models.DateTimeField(auto_now_add=True)