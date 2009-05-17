from django.db import models
from django.contrib.auth.models import User

class Dweety(models.Model):
    value = models.CharField(max_length=100, verbose_name="dweet")
    #foreign key connection to django's User model
    user = models.ForeignKey(User,blank=True,null=True,verbose_name="user")
    #time stamp model instance creation time
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
    #time stamp model instance update time
    date_modified  = models.DateTimeField(auto_now=True, verbose_name="date modified")

    class Meta:
        ordering = ['-date_created'] #default order scheme
        get_latest_by = "date_created" #for get_latest() method

    def __unicode__(self):
        return self.value

