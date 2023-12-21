from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage
def index(request):
    webpg=AccessRecord.objects.all()
    dic_my={'Access_record':webpg}
    return render(request,'index.html',context=dic_my)

