from django.shortcuts import render,redirect
#from Pet.models import

#region index

def Index(request):    
    return render(request, 'Index.html')

#endregion

#region Login

def Registro(request):    
    return render(request, 'Login/Registro.html')

def Ingreso(request):    
    return render(request, 'Login/Ingreso.html')

#endregion