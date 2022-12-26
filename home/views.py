from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting
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
        form =ContactForm(request.POST)
        if form.is_valid():
            data = ContactForm()
            data.name = form.cleanad_data['name']
            data.email = form.cleanad_data['email']
            data.phonenumber = form.cleanad_data['phonenumber']
            data.message = form.cleanad_data['message']
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting':setting,'form' :form}
    return render(request,'iletisim.html',context)


def turistikmekan(request):
    setting = Setting.objects.get(pk=1)

    context = {'setting':setting,'page' :'turistikmekan'}
    return render(request, 'turistikmekan.html',context)

