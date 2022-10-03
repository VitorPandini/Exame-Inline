# Generated by Django 4.0 on 2021-12-16 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_care'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(default=None, verbose_name='feito?')),
                ('care', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='care_items', to='exam.care', verbose_name='atendimento')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='care_items_exam', to='exam.exam', verbose_name='exame')),
            ],
            options={
                'verbose_name': 'atendimento item',
                'verbose_name_plural': 'atendimento itens',
                'ordering': ('pk',),
            },
        ),
    ]