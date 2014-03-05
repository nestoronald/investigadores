# Create your views here.
from django.shortcuts import render_to_response
from Publicaciones.models import *
from django.template import RequestContext
from forms import LoginForm, RegisterForm, addProfileForm, UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from django.core.context_processors import csrf
from django.contrib.auth import login, logout, authenticate
#from django.http import HttpresponseRedirect
# from django.core.context_processsors import csrf

def home(request):
    # Recuperar 10 investigadores como minimo
    mensaje = ""
    if request.user.is_authenticated():
        # return HttpResponseRedirect('/')
        return render_to_response('home.html',context_instance=RequestContext(request))
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect(next)
                else:
                    mensaje = "usuario y/o password incorrecto"
        next = request.REQUEST.get('next')
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje,'next':next}
        return render_to_response('home.html',ctx,context_instance=RequestContext(request))

def investigadores(request):
    inv = Investigador.objects.all()[:10]
    return render_to_response('investigadores.html',{'investigadores':inv},context_instance=RequestContext(request))
def investigador(request,idinv=1):
    return render_to_response('investigador.html',{'investigador':Investigador.objects.get(id=idinv)},context_instance=RequestContext(request))

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect(next)
                else:
                    mensaje = "usuario y/o password incorrecto"
        next = request.REQUEST.get('next')
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje,'next':next}
        return render_to_response('login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            u = User.objects.create_user(username=usuario,email=email,password=password_one)
            u.save() # Guardar el objeto
            return render_to_response('thanks_register.html',context_instance=RequestContext(request))
        else:
            ctx = {'form':form}
            return  render_to_response('register.html',ctx,context_instance=RequestContext(request))
    ctx = {'form':form}
    return render_to_response('register.html',ctx,context_instance=RequestContext(request))

@login_required
def edit_profile(request,id_user):
    info = "iniciado"
    user = Investigador.objects.get(pk=id_user)
    if request.method == "POST":
        form = addProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            edit_prod = form.save(commit=False)
            form.save_m2m()
            edit_prod.status = True
            edit_prod.save() # Guardamos el objeto
            info = "Correcto"
            return HttpResponseRedirect('/producto/%s/'%edit_prod.id)
    else:
        form = addProfileForm(instance=user)
    ctx = {'form':form,'informacion':info}
    return render_to_response('editProfile.html',ctx,context_instance=RequestContext(request))

@login_required
def editar_perfil(request):
    mensaje = ""
    if request.method == 'POST':
        # formulario enviado
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = addProfileForm(request.POST, instance=request.user.perfil_inv)

        if user_form.is_valid() and perfil_form.is_valid():
            # formulario validado correctamente
            user_form.save()
            perfil_form.save()
            mensaje = "Sus datos han sido actualizados"
            user_form = UserForm(instance=request.user)
            perfil_form = addProfileForm(instance=request.user.perfil_inv)
            #return HttpResponseRedirect('/formulario-guardado/')

    else:
        # formulario inicial
        user_form = UserForm(instance=request.user)
        perfil_form = addProfileForm(instance=request.user.perfil_inv)
    ctx = { 'user_form': user_form,  'perfil_form': perfil_form, 'mensaje':mensaje }
    return render_to_response('editarPerfil.html', ctx, context_instance=RequestContext(request))


