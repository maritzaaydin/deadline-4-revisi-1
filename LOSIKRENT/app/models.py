from django.db import models

# Create your models here.
class penyewa(models.Model):
    idpenyewa = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    nomortelepon = models.IntegerField()
    alamat = models.CharField(max_length=50)
    nomorktp = models.IntegerField()
    dokumen = models.CharField(max_length=10)

    def __str__(self):
        return str(self.nama)

class karyawan(models.Model):
    idkaryawan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=10)
    alamat = models.CharField(max_length=50)
    nomortelepon = models.IntegerField()

    def __str__(self):
        return str(self.nama)

class jenismobil (models.Model):
    idjenismobil = models.AutoField(primary_key=True)
    namamobil = models.CharField(max_length=50)
    jumlahmobil = models.IntegerField()
    hargasewa = models.IntegerField()

    def __str__(self):
        return str(self.namamobil)

class mobil (models.Model):
    idmobil = models.AutoField(primary_key=True)
    idjenismobil = models.ForeignKey(jenismobil, on_delete=models.CASCADE, null=True)
    nopolisi = models.CharField(max_length=8)
    konfirmasi = models.BooleanField()

    def __str__(self):
        return str(self.idmobil)

class penyewaan (models.Model):
    idpenyewaan = models.AutoField(primary_key=True)
    idpenyewa = models.ForeignKey(penyewa, on_delete=models.CASCADE)
    idkaryawan = models.ForeignKey(karyawan, on_delete=models.CASCADE)
    idmobil = models.ForeignKey(mobil, on_delete=models.CASCADE)
    tanggalpenyewaan = models.DateField()
    durasi = models.IntegerField()
    tanggalpengembalian = models.DateField()

    def __str__(self):
        return str(self.tanggalpenyewaan)


