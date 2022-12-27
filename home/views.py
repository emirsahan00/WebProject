from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting, ContactFormMessage, SignUpForm, ContactFormu
from product.models import Product


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:3]
    context = {'setting':setting,
               'page' :'home',
               'sliderdata': sliderdata}
    return render(request, 'eski.html',context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting':setting,'page' :'hakkımızda'}
    return render(request, 'hakkımızda.html',context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting':setting,'page' :'iletisim'}
    return render(request, 'iletisim.html',context)

def about(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting':setting,'page' :'about'}
    return render(request, 'about.html',context)

def iletisim1(request):

    if request.method =='POST':
        form =ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            #data.ip = request.META.get('REMOTE_ADDR')
            data.message = form.cleaned_data['message']

            data.save()
            messages.success(request,"mesaj iletildi")
            return HttpResponseRedirect('/iletisim/footer')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting':setting,'form' :form}
    return render(request,'footer.html',context)


def turistikmekan(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting':setting,'page' :'turistikmekan'}
    return render(request, 'turistikmekan.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Giriş başarısız! Hatalı kullanıcı adı veya parola girişi.")
            return HttpResponseRedirect ('/login')
    return render(request, 'login.html')

def signup_view(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    context = {'form':form}
    return render(request, 'signup.html', context)

