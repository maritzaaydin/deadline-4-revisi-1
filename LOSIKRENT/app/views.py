from hashlib import algorithms_guaranteed
from django.shortcuts import render,redirect
from . import models

# Create your views here.
# penyewa
def penyewa(request):
    allpenyewaobj = models.penyewa.objects.all()
    # getpenyewaobj = models.penyewa.objects.get(idpenyewa=1)
    # filterpenyewaobj = models.penyewa.objects.filter(dokumen='ktp')
    return render (request, 'penyewa.html', {
        'allpenyewaobj' : allpenyewaobj,
        # 'getpenyewaobj' : getpenyewaobj,
        # 'filterpenyewaobj' : filterpenyewaobj
    })

def createdatapenyewa(request):
    if request.method == "GET":
        return render(request,'createdatapenyewa.html')
    else:
        nama = request.POST['nama']
        nomortelepon = request.POST['nomortelepon']
        alamat = request.POST['alamat']
        nomorktp = request.POST['nomorktp']
        dokumen = request.POST['dokumen']

        newpenyewa = models.penyewa(
            nama = nama,
            nomortelepon = nomortelepon,
            alamat = alamat,
            nomorktp = nomorktp,
            dokumen = dokumen,
        ).save()
        return redirect('penyewa')

def updatepenyewa(request,id):
    penyewaobj = models.penyewa.objects.get(idpenyewa=id)
    if request.method == "GET":
        return render(request,'updatepenyewa.html', {
            'allpenyewa' : penyewaobj,
        })
    else:
        penyewaobj.nama = request.POST['nama']
        penyewaobj.nomortelepon = request.POST['nomortelepon']
        penyewaobj.alamat = request.POST['alamat']
        penyewaobj.nomorktp = request.POST['nomorktp']
        penyewaobj.dokumen = request.POST['dokumen']
        penyewaobj.save()
        return redirect('penyewa')

def deletepenyewa(request,id):
    penyewaobj = models.penyewa.objects.get(idpenyewa=id)
    penyewaobj.delete()
    return redirect('penyewa')


# karyawan
def karyawan(request):
    allkaryawanobj = models.karyawan.objects.all()
    # getkaryawanobj = models.karyawan.objects.get(idkaryawan=1)
    return render (request, 'karyawan.html', {
        'allkaryawanobj' : allkaryawanobj,
        # 'getkaryawanobj' : getkaryawanobj,
    })

def createdatakaryawan(request):
    if request.method == "GET":
        return render(request,'createdatakaryawan.html')
    else:
        nama = request.POST['nama']
        alamat = request.POST['alamat']
        nomortelepon = request.POST['nomortelepon']

        newkaryawan = models.karyawan(
            nama = nama,
            alamat = alamat,
            nomortelepon = nomortelepon,
        ).save()
        return redirect('karyawan')

def updatekaryawan(request,id):
    karyawanobj = models.karyawan.objects.get(idkaryawan=id)
    if request.method == "GET":
        return render(request,'updatekaryawan.html', {
            'allkaryawan' : karyawanobj,
        })
    else:
        karyawanobj.nama = request.POST['nama']      
        karyawanobj.alamat = request.POST['alamat']
        karyawanobj.nomortelepon = request.POST['nomortelepon']
        karyawanobj.save()
        return redirect('karyawan')

def deletekaryawan(request,id):
    karyawanobj = models.karyawan.objects.get(idkaryawan=id)
    karyawanobj.delete()
    return redirect('karyawan')


# jenis mobil
def jenismobil(request):
    alljenismobilobj = models.jenismobil.objects.all()
    # getjenismobilobj = models.jenismobil.objects.get(idjenismobil=1)
    return render (request, 'jenismobil.html', {
        'alljenismobilobj' : alljenismobilobj,
        # 'getjenismobilobj' : getjenismobilobj,
    })

def createdatajenismobil(request):
    if request.method == "GET":
        return render(request,'createdatajenismobil.html')
    else:
        namamobil = request.POST['namamobil']
        jumlahmobil = request.POST['jumlahmobil']
        hargasewa = request.POST['hargasewa']

        newjenismobil = models.jenismobil(
            namamobil = namamobil,
            jumlahmobil = jumlahmobil,
            hargasewa = hargasewa,
        ).save()
        return redirect('jenismobil')

def updatejenismobil(request,id):
    jenismobilobj = models.jenismobil.objects.get(idjenismobil=id)
    if request.method == "GET":
        return render(request,'updatejenismobil.html', {
            'alljenismobil' : jenismobilobj,
        })
    else:
        jenismobilobj.namamobil = request.POST['namamobil']      
        jenismobilobj.jumlahmobil = request.POST['jumlahmobil']
        jenismobilobj.hargasewa = request.POST['hargasewa']
        jenismobilobj.save()
        return redirect('jenismobil')

def deletejenismobil(request,id):
    jenismobilobj = models.jenismobil.objects.get(idjenismobil=id)
    jenismobilobj.delete()
    return redirect('jenismobil')


#mobil
def mobil(request):
    allmobilobj = models.mobil.objects.all()
    # getmobilobj = models.mobil.objects.get(idmobil=1)
    return render (request, 'mobil.html', {
        'allmobilobj' : allmobilobj,
        # 'getmobilobj' : getmobilobj,
    })

def createdatamobil(request):
    if request.method == "GET":
        return render(request,'createdatamobil.html')
    else:
        # idjenismobil = request.POST['idjenismobil']
        nopolisi = request.POST['nopolisi']
        konfirmasi = request.POST['konfirmasi']

        newmobil = models.mobil(
            # idjenismobil = idjenismobil,
            nopolisi = nopolisi,
            konfirmasi = konfirmasi,
        ).save()
        return redirect('mobil')

def updatemobil(request,id):
    jenismobilobj = models.jenismobil.objects.all()
    mobilobj = models.mobil.objects.get(idmobil=id)
    if request.method == "GET":
        return render(request,'updatemobil.html', {
            'alljenismobil' : jenismobilobj,
            'allmobil' : mobilobj,
        })
    else:
        mobilobj.idjenismobil = request.POST['idjenismobil']      
        mobilobj.nopolisi = request.POST['nopolisi']
        mobilobj.konfirmasi = request.POST['konfirmasi']
        mobilobj.save()
        return redirect('mobil')

def deletemobil(request,id):
    mobilobj = models.mobil.objects.get(idmobil=id)
    mobilobj.delete()
    return redirect('mobil') 


#penyewaan 
def penyewaan(request):
    allpenyewaanobj = models.penyewaan.objects.all()
    # getpenyewaanobj = models.penyewaan.objects.get(idpenyewaan=1)
    return render (request, 'penyewaan.html', {
        'allpenyewaanobj' : allpenyewaanobj,
        # 'getpenyewaanobj' : getpenyewaanobj,
    })

def createdatapenyewaan(request):
    if request.method == "GET":
        return render(request,'createdatapenyewaan.html')
    else:
        # idpenyewa = request.POST['idenyewa']
        # idkaryawan = request.POST['idkaryawan']
        # idmobil = request.POST['idmobil']
        tanggalpenyewaan = request.POST['tanggalpenyewaan']
        durasi = request.POST['durasi']
        tanggalpengembalian = request.POST['tanggalpengembalian']

        newpenyewaan = models.penyewaan(
            # idpenyewa = idpenyewa,
            # idkaryawan = idkaryawan,
            # idmobil = idmobil,
            tanggalpenyewaan = tanggalpenyewaan,
            durasi = durasi,
            tanggapengembalian = tanggalpengembalian,
        ).save()
        return redirect('penyewaan')

def updatepenyewaan(request,id):
    penyewaanobj = models.penyewaan.objects.get(idpenyewaan=id)
    if request.method == "GET":
        return render(request,'updatepenyewaan.html', {
            'allpenyewaan' : penyewaanobj,
        })
    else:
        # penyewaanobj.idpenyewa = request.POST['nama']      
        # penyewaanobj.idkaryawan = request.POST['alamat']
        # penyewaanobj.idmobil = request.POST['nomortelepon']
        penyewaanobj.tanggalpenyewaan = request.POST['tanggalpenyewaan']
        penyewaanobj.durasi = request.POST['durasi']
        penyewaanobj.tanggalpengembalian = request.POST['tanggalpengembalian']
        penyewaanobj.save()
        return redirect('penyewaan')

def deletepenyewaan(request,id):
    penyewaanobj = models.penyewaan.objects.get(idpenyewaan=id)
    penyewaanobj.delete()
    return redirect('penyewaan')







