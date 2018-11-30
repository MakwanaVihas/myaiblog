from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import os
# Create your views here.
def index(request):
    return render(request,"index.html")
def index1(request):
    return render(request,"index.html")
def page(request,id):
    # a=getFile(id)
    # head=a[2]
    # web_source=a[-1]
    # a[0].remove(a[-1])
    # a[0].remove(a[2])
    # context22={'file':a[0],'src':a[1],'head':head,'web_source':web_source}
    page="page"+str(id)+".html"
    return render(request,page) 
def getFile(id):
    a=[]
    src="static/AI"+str(id)+".jpg"
    b="text"+str(id)+".txt"
    pwd=os.path.dirname(__file__)
    file_path = os.path.join(pwd, b)
    file=open(file_path)
    for i in file:
        a.append(i)
    return [a,src,a[0],a[-1]]