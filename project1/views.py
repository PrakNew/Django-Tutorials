from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def about(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    makeupper= request.POST.get('makeupper', 'off')
    makelower = request.POST.get('makelower', 'off')
    countwords = request.POST.get('countwords', 'off')
    removenewline=request.POST.get('removenewline','off')
    s='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    print('-----------',type(djtext),'--------------------')
    if str(removepunc)=='on':
        s1=''
        for x in str(djtext):
            if x not in s:
                s1+=x
        djtext=s1
    if str(makeupper)=='on':
        djtext=djtext.upper()
    if str(makelower)=='on':
        djtext=djtext.lower()
    if str(countwords)=='on':
        djtext= 'The sentence is '+djtext+' and the count of the words is '+str(len(djtext.split()))
    if str(removenewline)=='on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        djtext=analyzed
    if str(removepunc)!='on' and str(countwords)!='on' and str(makeupper)!='on' and str(makelower)!='on' and str(removenewline)!='on':
        return HttpResponse('THERE is some ERROR please resubmit')
    a=str(djtext)
    return render(request,'about.html',{'final':a})
