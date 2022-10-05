from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.penyewa)
admin.site.register(models.karyawan)
admin.site.register(models.mobil)
admin.site.register(models.jenismobil)
admin.site.register(models.penyewaan)