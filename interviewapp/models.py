from django.db import models

# Create your models here.
class Interview_question(models.Model):
    question_number = models.AutoField(primary_key=True)
    question = models.TextField(max_length=300)
    answer = models.TextField(max_length=2000)
    category = models.CharField(max_length=100,default='python')
    def __str__(self):
        return self.question