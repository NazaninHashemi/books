from django.shortcuts import render,HttpResponse,redirect
from.models import typeb,tamas,bookinfo
from PIL import Image
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm





# Create your views here.
def homepage(request):
    v=typeb.objects.all()
    return render(request ,"home/home.html",context={"category":v})

def booktype(request,idbook):  
    if idbook=="Story":
       #b=typeb.objects.get(pk=idbook)
       v=bookinfo.objects.filter(genre=idbook) 
       return render(request,"home/tarikh.html",context={"anva":v})  
    else:
       v=bookinfo.objects.filter(genre=idbook) 
       return render(request,"home/tarikh.html",context={"anva":v})
    
def contactus(request):
    if request.method =='POST':
      na=request.POST['name']
      em=request.POST['email']
      ph=request.POST['Phone']
      ma=request.POST['message']
      if na!=None :
        tamas.objects.create(nam=na , email=em, phone=ph , massage=ma )
        #new.save()
        messages.success(request,"Your information has been registered :)")
    return render(request,'home/contact.html')

def infobook(request,idinfo):
    i=bookinfo.objects.get(pk=idinfo)
    return render(request,"home/bookinfo.html",context={"info":i})


def userlogin(request):
    if (request.method == 'POST'):
        u=request.POST['uname']
        p= request.POST['upass']
        user=authenticate(request,userneme=u,password=p)
        if user is not None:
            if user.is_active:
             login(request,user)
             return redirect(request, 'userpanel/')
            else:
              messages.success(request,"register please")
        
        else:
            messages.success(request,"there is an error, try agein")
            return render(request,'home/users.html')
         
    else:
         messages.success(request,"!Enter the information!")
         return render(request,'home/users.html')
     
  #form = AuthenticationForm()
    #if request.method == 'POST':
       # form = AuthenticationForm(request.POST)
        #if form.is_valid():
          #  username = form.cleaned_data.get('uname')
          #  password = form.cleaned_data.get('upass')
          #  user = authenticate(username=username, password=password)
            #if user is not None:
                #login(request,user)
                
                #return redirect('userpanel/')
            #else:
                #messages.error(request,'register please')
        #else:
           # messages.error(request,'there is an error, try agein')
   # context = {'form':form}
    #return render(request,'home/users.html',context)     
    
        
def upanel(request):
    if (request.user.is_authenticated):
        return render(request,"home/userpanel.html")
    else:
        return redirect("/users")

def lout(request):
    logout(request)
    return redirect("/")

def error(request):
    return render(request,"home/error.html")

def reg(request):
    st=False
    contex={"errors":[]}
    if request.method=="POST" :
        
        f=request.POST["fname"]
        p=request.POST["pass"]
        pr=request.POST["rpass"]
        if len(p)<6:
            st=True
            contex["errors"].append("Password must be more than 6 characters")
        if p!=pr:
            st=True
            contex["errors"].append("Enter the correct password")
        if st==False:
            
          User.objects.create(username=f,password=p)
          messages.success(request,"You have become a member of our site! :)")
          return render(request,'home/users.html') 
    else:
         messages.success(request,"Enter the information!") 
         return render(request,'home/reg.html',contex) 
         




    
   
  

