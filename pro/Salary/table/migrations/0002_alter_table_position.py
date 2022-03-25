# Generated by Django 4.0.3 on 2022-03-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='position',
            field=models.IntegerField(choices=[(1, 'Генеральный директор'), (2, 'Руководитель отдела'), (3, 'Руководитель подразделения'), (4, 'Менеджер'), (5, 'Продавец')], verbose_name='Должность'),
        ),
    ]