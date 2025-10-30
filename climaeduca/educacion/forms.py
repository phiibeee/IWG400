from django import forms

class RegistroForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    correo = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)
