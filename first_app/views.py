from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    my_dic={'insert_me':"hello I'm Kanu from views"}
    return render(request,'index.html',context=my_dic)

