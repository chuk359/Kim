from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth import get_user_model
User = get_user_model()


 

# Create your models here.
class Table(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    POSITION = (
        (1, 'CEO'),
        (2, 'Director'),
        (3, 'Team Lead'),
        (4, 'Manager'),
        (5, 'Specialist'),
    )
    employment_position = models.IntegerField(choices=POSITION)
    employment_start_date = models.DateField()
    salary = models.IntegerField()
    paid = models.IntegerField()
    сhief = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    
    def str(self):
        return str(self.id) + ' Name: ' + self.name

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):  
        return self.name