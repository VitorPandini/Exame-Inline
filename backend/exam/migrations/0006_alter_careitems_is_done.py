# Generated by Django 4.0 on 2021-12-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_alter_careitems_is_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careitems',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='feito?'),
        ),
    ]