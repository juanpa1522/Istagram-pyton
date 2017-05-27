from django.shortcuts import render

# Create your views here.
def registro(request):
    return render(request, 'registro.html')

def crear_usuario(request):
        _email = request.POST ['email']
        _username = request.POST ['username']
        _password = request.POST ['password']
        _name = request.POST ['nombre']
        print (_email)
        print (_username)
        print (_password)
        print (_nombre)
        user=User.objects.create_user(username = _username, email=email, password=password )
        myUser = MiUsuario (usuario = user)
        myUser.save()
        print (user)
        print(user.password)
        return redirect('inicio')
    else:
        return render(request, 'pagina_inicio')




def inicio(request):
    return render( request, 'inicio_sesion.html')
