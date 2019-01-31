from django.db import models

# Create your models here.
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver ip:port(8000)
class Banji(models.Model):
    name=models.CharField(max_length=20)
    createtime=models.DateTimeField()
    num=models.IntegerField()
    isGood=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Students(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    sex=models.IntegerField()
    banNo=models.ForeignKey('Banji')
