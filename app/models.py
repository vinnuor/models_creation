from django.db import models

# Create your models here.
class Topic(models.model):
    topic_name=models.CharFieled(max_length=100,primary_key=True)



class Webpage(models.model):
    topic_name=models.foreigenkey(Topic,on_delete=models.CASCADE)
    URL=models.URLField()

class AccessRecord(models.model):
    name=models.forigenkey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
