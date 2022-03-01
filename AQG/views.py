# from msilib.schema import File
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
import os
from pathlib import Path
# from django.core.files import File
from django.contrib import messages
from django.http import Http404, HttpResponse
from .models import FilesAdmin, Question,Osquestion
from random import randint
import random

# Create your views here.


def home(request):
    return render(request,'home.html')

def admin(request):
    return redirect('admin')

def tologin(request):
    return render(request,'login.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'Wrong credential!!!Ask admin for updating your details')
            return redirect('login')

        
    else:   
        return render(request, 'login.html' )






def logout(request):
    auth.logout(request)
    return redirect('/')


def dashboard(request):
    context = {
        'file': FilesAdmin.objects.all(),
        'user' : User.objects.all()
    }
    return render(request,'dashboard.html',context)

def download( request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists():
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['content-Disposition']='inline;filename='+ os.path.basename(file_path)
            return response
    
    raise Http404


# def fullmark_validation(request):
#     full_mark = request.POST['full_mark']
#     two_mark = request.POST['two_mark']
#     four_mark = request.POST['four_mark']
#     full_mark = int(full_mark)
#     two_mark = int(two_mark)
#     four_mark = int(four_mark)
#     total_two = 2*two_mark
#     total_four = 4* four_mark
#     if(full_mark==(total_two+total_four)):
#         return render(request,'download.html')
#     else:
#         return redirect('dashboard')

def downloadfromhere(request):
    context={
        'file' : FilesAdmin.objects.all()
    }
    return render(request,'download.html',context)



def getdata(request):
    full_mark = request.GET['f_marks']
    pass_mark = request.GET['p_marks']
    two_mark = request.GET['No_two']
    four_mark = request.GET['No_four']
    fac = request.GET["faculty"]
    year = request.GET["year"]
    part = request.GET["part"]
    sub = request.GET["subject"]
    
    full_mark = int(full_mark)
    two_mark = int(two_mark)
    four_mark = int(four_mark)
    pass_mark = int(pass_mark)
    total_two = 2*two_mark
    total_four = 4* four_mark
    if(full_mark==(total_two+total_four)):
        if fac == "BCT":
            if year=="3":
                if part == "II":
                    if sub=="DBMS":
                        questionsdbms= Question.objects.all()
                        
                        q=[i for i in questionsdbms]
                        qn_4 = four_mark
                        qn_2 = two_mark
                        grpA=[]
                        grpB=[]
                        qn=random.shuffle(q)
                        for i in q:
                            if i.mark==2 and qn_2>0:
                                grpA.append(i.qn)
                                qn_2 -=1
                            elif i.mark==4 and qn_4>0:
                                grpB.append(i.qn)
                                qn_4 -=1
                        context = {
                                'questionShort': grpA,
                                'questionLong': grpB,
                                'sub': "DBMS",
                                'pass_mark': pass_mark,
                                'full_mark': full_mark
                                }
                        return render(request, "output.html",context)
                        
                        
                    elif sub == "Operating System":
                        questionsos = Osquestion.objects.all()
                        q=[i for i in questionsos]
                        qn_4 = four_mark
                        qn_2 = two_mark
                        grpA=[]
                        grpB=[]
                        qn=random.shuffle(q)
                        for i in q:
                            if i.mark==2 and qn_2>0:
                                grpA.append(i.qn)
                                qn_2 -=1
                            elif i.mark==4 and qn_4>0:
                                grpB.append(i.qn)
                                qn_4 -=1
                        context = {
                                'questionShort': grpA,
                                'questionLong': grpB,
                                'full_mark': full_mark,
                                'pass_mark': pass_mark,
                                'sub': "Operating System"
                                }
                        return render(request, "output.html",context)
                
    else:
        messages.info(request,'Full marks not met!!')
        return redirect('dashboard')
                        
       



    





# def uploadtoadm(pdf_path):
#     pdf_name = os.path.basename(pdf_path)
#     if FilesAdmin.objects.filter(adminupload = pdf_path).exists():
#         pass
#     else:
#         new_adminfile= FilesAdmin.objects.create(adminupload = pdf_path,title=pdf_name)
#         new_adminfile.save()



# x = uploadtoadm('media_cdn\media\dbms_lab.pdf')

# def upadm(self):
#     path = Path('D:\Minor Project\test_AQM\dbms_lab.txt')
#     with path.open(mode='rb') as ff:
#         FilesAdmin.adminupload = File(ff,title=os.path.basename(path))
#         FilesAdmin.save()
    

# def getfaculty(request):

    
#     questionsdbms= Question.objects.all()
#     questionsos = Osquestion.objects.all()
#     q=[i for i in questionsdbms]
#     qn_4 = 2
#     qn_2 = 2
#     grpA=[]
#     grpB=[]
#     qn=random.shuffle(q)
#     for i in q:
#         if i.mark==2 and qn_2>0:
#             grpA.append(i.qn)
#             qn_2 -=1
#         if i.mark==4 and qn_4>0:
#             grpB.append(i.qn)
#             qn_4 -=1
    
    
    # listsq = [i for i in range(1,qn_2+1)]
    # listsq = str(listsq)
    # listlq = [i for i in range(1,qn_4+1)]
    context = {
        'questionShort': grpA,
        'questionLong': grpB,
        # 'leng': range(1,4),
        # 'listlq': listlq,
        # 'listsq': listsq
    }
    return render(request, "generated.html",context)



