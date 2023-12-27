from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage
from . import form
def index(request):
    webpg=AccessRecord.objects.all()
    dic_my={'Access_record':webpg}
    return render(request,'index.html',context=dic_my)
def form_name(request):
    forms=form.FormName()

    if request.method == 'POST':
        forms =form.FormName(request.POST)
        if forms.is_valid():
            print("validation success")
            print(forms.cleaned_data['name'])
            print(forms.cleaned_data['email'])
            print(forms.cleaned_data['text'])
    
    return render(request,'base_app/form_page.html', {'form':forms})