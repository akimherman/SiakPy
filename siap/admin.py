from django.contrib import admin

from .models import mahasiswa, matkul, krs, kurikulum


# from siap.forms import MyForm, CustomSetForm


# Register your models here.

class krsAdmin(admin.ModelAdmin):
    list_display = ('nim', 'kode_matkul')


class mahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nim', 'nama')


class matkulAdmin(admin.ModelAdmin):
    list_display = ('kode_matkul', 'nama_matkul')


admin.site.register(krs, krsAdmin)
admin.site.register(mahasiswa, mahasiswaAdmin)
admin.site.register(matkul, matkulAdmin)
admin.site.register(kurikulum)

"""
@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    form = MyForm


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    form = CustomSetForm 
"""
