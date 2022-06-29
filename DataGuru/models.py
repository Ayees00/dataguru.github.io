from django.db import models


class DataGuru(models.Model):
    jk = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    )
    nama = models.CharField(max_length=100)
    nisn = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    tanggal_lahir = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=10, choices=jk)

    def __str__(self):
        return '{}. {}'.format(self.id, self.nama)
# Create your models here.
