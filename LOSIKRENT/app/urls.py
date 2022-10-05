from django.urls import path


from . import views

urlpatterns = [
    path('penyewa',views.penyewa,name='penyewa'),
    path('createdatapenyewa',views.createdatapenyewa,name='createdatapenyewa'),
    path('updatepenyewa/<str:id>', views.updatepenyewa,name='updatepenyewa'),
    path('deletepenyewa/<str:id>', views.deletepenyewa,name='deletepenyewa'),   
    path('karyawan',views.karyawan,name='karyawan'),
    path('createdatakaryawan',views.createdatakaryawan,name='createdatakaryawan'),
    path('updatekaryawan/<str:id>', views.updatekaryawan,name='updatekaryawan'),
    path('deletekaryawan/<str:id>', views.deletekaryawan,name='deletekaryawan'),
    path('jenismobil',views.jenismobil,name='jenismobil'),
    path('createdatajenismobil',views.createdatajenismobil,name='createdatajenismobil'),
    path('updatejenismobil/<str:id>', views.updatejenismobil,name='updatejenismobil'),
    path('deletejenismobil/<str:id>', views.deletejenismobil,name='deletejenismobil'),
    path('mobil',views.mobil,name='mobil'),
    path('createdatamobil',views.createdatamobil,name='createdatamobil'),
    path('updatemobil/<str:id>', views.updatemobil,name='updatemobil'),
    path('deletemobil/<str:id>', views.deletemobil,name='deletemobil'),
    path('penyewaan', views.penyewaan,name='penyewaan'),
    path('createdatapenyewaan',views.createdatapenyewaan,name='createdatapenyewaan'),
    path('updatepenyewaan/<str:id>', views.updatepenyewaan,name='updatepenyewaan'),
    path('deletepenyewaan/<str:id>', views.deletepenyewaan,name='deletepenyewaan'),
    
]