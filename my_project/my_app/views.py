from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'my_app/index.html',{'text':'HELLO'})
def other(req):
    return render(req,'my_app/other.html')
def relative(req):
    return render(req,'my_app/relative.html')
def base(req):
    return render(req,'my_app/base.html')
