from django.shortcuts import render, redirect
from .models import DataGuru
from django.contrib import messages
from .forms import DataGuruForm


def index(request):
    data = {
        'judul': 'Data Guru SDN 6 Sepit',
    }
    return render(request, 'index.html', data)


def list(request):
    dataguru_list = DataGuru.objects.all()
    data = {
        'judul': 'Data Guru SDN 6 Sepit',
        'isi': dataguru_list,
    }
    return render(request, 'DataGuru/list.html', data)


def tambah(request):
    dataguru_tambah = DataGuruForm(request.POST or None)
    if request.method == 'POST':
        if dataguru_tambah.is_valid():
            dataguru_tambah.save()
            messages.success(request, "Data Berhasil Di Simpan")
        return redirect('list')
    data = {
        'judul': 'Tambah Data Guru SDN 6 Sepit',
        'isi': dataguru_tambah,
    }
    return render(request, 'DataGuru/tambah.html', data)


def hapus(request, hapus_id):
    dataguru_hapus = DataGuru.objects.filter(id=hapus_id)
    dataguru_hapus.delete()
    messages.success(request, "Data Berhasil Dihapus")
    return redirect('list')


def ubah(request, ubah_id):
    dataguru_ubah = DataGuru.objects.get(id=ubah_id)
    data_dataguru = {
        'nama': dataguru_ubah.nama,
        'nisn': dataguru_ubah.nisn,
        'alamat': dataguru_ubah.alamat,
        'jabatan': dataguru_ubah.jabatan,
        'tanggal_lahir': dataguru_ubah.tanggal_lahir,
        'jenis_kelamin': dataguru_ubah.jenis_kelamin,
    }
    dataguru_form = DataGuruForm(
        request.POST or None, initial=data_dataguru, instance=dataguru_ubah)
    if request.method == 'POST':
        if dataguru_form.is_valid():
            dataguru_form.save()
            messages.success(request, "Data Berhasil Dirubah")
        return redirect('list')
    data = {
        'judul': "Ubah Data Guru SDN 6 Sepit",
        'isi': dataguru_form,
    }
    return render(request, 'DataGuru/tambah.html', data)
