from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


 

# Create your models here.
class Table(models.Model):
    name = models.CharField(verbose_name='ФИО', db_index=True, max_length=100)
    POSITION = (
        (1, 'Генеральный директор'),
        (2, 'Руководитель отдела'),
        (3, 'Руководитель подразделения'),
        (4, 'Менеджер'),
        (5, 'Продавец'),
    )
    position = models.IntegerField(verbose_name='Должность', choices=POSITION)
    date = models.DateField(verbose_name='Дата приема на работу')
    salary = models.DecimalField(verbose_name='Размер заработной платы', max_digits=10, decimal_places=2)
    paid = models.DecimalField(verbose_name='Информация о выплаченной зарплате', max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
   
    