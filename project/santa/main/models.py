from django.db import models

class Task(models.Model):
    title = models.CharField('Username', max_length=50)
    task = models.TextField('Wish')

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Wish'
        verbose_name_plural = 'Wishes'
        
