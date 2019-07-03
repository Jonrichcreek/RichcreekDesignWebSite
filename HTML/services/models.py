from django.db import models
from datetime import datetime
class Service(models.Model):
    title = models.CharField(max_length = 200)
    pic_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    pic_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pic_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pic_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pic_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    blurb = models.TextField(blank = True)
    description = models.TextField(blank = True)
    publish = models.BooleanField(default= True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    
    