from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
class Game(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    speed = models.IntegerField()
    gametype = models.IntegerField(default = 10)

    def __str__(self):
        return f"{self.user_id}: {self.speed} wpm | type: {self.gametype} words"