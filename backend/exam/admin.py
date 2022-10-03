from django.contrib import admin

from .models import Care, CareItems, Exam, Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)


class CareItemsInline(admin.TabularInline):
    model = CareItems
    extra = 0


@admin.register(Care)
class CareAdmin(admin.ModelAdmin):
    inlines = (CareItemsInline,)
    list_display = ('__str__', 'patient', 'created')
    date_hierarchy = 'created'
