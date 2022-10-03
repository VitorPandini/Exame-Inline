from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Patient(models.Model):
    registration = models.CharField('matrícula', max_length=7, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='paciente',
        related_name='patients'
    )

    class Meta:
        ordering = ('user__first_name',)
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'

    def __str__(self):
        return f'{self.user.first_name}'

    # def get_absolute_url(self):
    #     return reverse_lazy('_detail', kwargs={'pk': self.pk})


class Exam(models.Model):
    title = models.CharField('título', max_length=50, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'exame'
        verbose_name_plural = 'exames'

    def __str__(self):
        return f'{self.title}'

    # def get_absolute_url(self):
    #     return reverse_lazy('_detail', kwargs={'pk': self.pk})


class Care(models.Model):
    doctor = models.CharField('médico', max_length=100)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='paciente',
        related_name='cares',
    )
    created = models.DateTimeField('data', auto_now_add=True)

    class Meta:
        ordering = ('doctor',)
        verbose_name = 'atendimento'
        verbose_name_plural = 'atendimentos'

    def __str__(self):
        return f'{self.doctor}'

    def get_absolute_url(self):
        return reverse_lazy('exam:care_detail', kwargs={'pk': self.pk})


class CareItems(models.Model):
    care = models.ForeignKey(
        Care,
        on_delete=models.CASCADE,
        verbose_name='atendimento',
        related_name='care_items',
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        verbose_name='exame',
        related_name='care_items_exam',
    )
    is_done = models.BooleanField('feito?', default=False)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'atendimento item'
        verbose_name_plural = 'atendimento itens'

    def __str__(self):
        return f'{self.pk}'

        # def get_absolute_url(self):
        #     return reverse_lazy('_detail', kwargs={'pk': self.pk})
