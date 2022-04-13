from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppEntrega.models import Lista_de_precios, Cliente, Profesional, Turnos
from AppEntrega.forms import Lista_de_preciosFormulario, ClienteFormulario, ProfesionalFormulario, TurnosFormulario

# Create your views here.
def inicio(request):
    
      return render(request, "AppEntrega/inicio.html")



def listadeprecios(request):

      return render(request, "AppEntrega/listadeprecios.html")


def cliente(request):

      return render(request, "AppEntrega/cliente.html")

def profesional(request):
    
      return render(request, "AppEntrega/profesional.html")

def turnos(request):
    
      return render(request, "AppEntrega/turnos.html")  

def listadeprecios(request):
    
      if request.method == 'POST':

            miFormulario = Lista_de_preciosFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid: 

                  informacion = miFormulario.cleaned_data

                  lista = Lista_de_precios (nombre_serv=informacion['nombre_serv'], precio=informacion['precio']) 

                  lista.save()

                  return render(request, "AppEntrega/inicio.html") 

      else: 

            miFormulario= Lista_de_preciosFormulario() 

      return render(request, "AppEntrega/listadeprecios.html", {"miFormulario":miFormulario})




def cliente(request):

      if request.method == 'POST':

            miFormulario = ClienteFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  cliente = Cliente (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], dni=informacion['dni'], telefono=informacion['telefono']) 

                  cliente.save()

                  return render(request, "AppEntrega/inicio.html") 

      else: 

            miFormulario= ClienteFormulario() 

      return render(request, "AppEntrega/cliente.html", {"miFormulario":miFormulario})

def profesional(request):
    
      if request.method == 'POST':

            miFormulario = ProfesionalFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  profesional = Profesional (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  especialidad=informacion['especialidad']) 

                  profesional.save()

                  return render(request, "AppEntrega/inicio.html") 

      else: 

            miFormulario= ProfesionalFormulario() 

      return render(request, "AppEntrega/profesional.html", {"miFormulario":miFormulario})

def turnos(request):
    
      if request.method == 'POST':

            miFormulario = TurnosFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  turnos = Turnos (nombre=informacion['nombre'], fecha_del_turno=informacion['fecha'], horario_asignado=informacion['horario']) 

                  turnos.save()

                  return render(request, "AppEntrega/inicio.html") 

      else: 

            miFormulario= TurnosFormulario() 

      return render(request, "AppEntrega/turnos.html", {"miFormulario":miFormulario})

def buscar(request):
    
      if  request.GET["telefono"]:

	      
            telefono = request.GET['telefono'] 
            cliente = Cliente.objects.filter(telefono__icontains=telefono)

            return render(request, "AppEntrega/inicio.html", {"cliente":cliente, "telefono":telefono})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return render(request, "AppEntrega/inicio.html", {"respuesta":respuesta})
