from django.db import models

# Create your models here.
class P1(models.Model):
    Q1 = models.CharField(max_length=200)
    req = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.Q1

class P2(models.Model):
    Qu = models.ForeignKey(P1,on_delete=models.CASCADE)
    res = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.Qu
