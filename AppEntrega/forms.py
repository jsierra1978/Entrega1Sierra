from django import forms


class Lista_de_preciosFormulario(forms.Form):
    
    nombre_serv= forms.CharField(max_length=40)
    precio= forms.IntegerField()

class ClienteFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    dni= forms.IntegerField()
    telefono= forms.IntegerField()

class ProfesionalFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    especialidad= forms.CharField(max_length=30)

class TurnosFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    fecha_del_turno = forms.DateField()  
    horario_asignado = forms.IntegerField()