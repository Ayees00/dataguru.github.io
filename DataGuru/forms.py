from django.forms import ModelForm
from django import forms
from .models import DataGuru


class DataGuruForm(ModelForm):
    class Meta:
        model = DataGuru
        fields = '__all__'
        widgets = {
            'nama': forms.TextInput({'class': 'form-control'}),
            'nisn': forms.TextInput({'class': 'form-control'}),
            'alamat': forms.Textarea({'class': 'form-control'}),
            'jabatan': forms.TextInput({'class': 'form-contorl'}),
            'tanggal_lahir': forms.TextInput({'class': 'form-contorl'}),
            'jenis_kelamin': forms.Select({'class': 'form-control'}),
        }
