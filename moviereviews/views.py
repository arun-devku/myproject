from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *


# Create your views here.
def base(request):
    return render(request, 'base.html')
def index(request):
    movie=request.GET.get("name")
   
    if movie:
        movies=Movies2.objects.filter(name__icontains=movie)
        obj=Item.objects.all() 
        return render(request, 'index.html',{"movie":movies,"video":obj}) 

      
        if request.method=="POST":
            try:
                name=request.POST['name']
                dir=request.POST['director']
                cast=request.POST['cast']
                desc=request.POST['description']
                release=request.POST['release']
                rating=request.POST['rating']
                img=request.FILES['images']
                logid=request.session['logdata']
                moviesobj=Movies2(name=name,director=dir,cast=cast,description=desc,releasedate=release,rating=rating,image=img)
                moviesobj.save()
                movies=Movies2.objects.all()
                obj=Item.objects.all()
                return redirect("/moviestreet/pro2")
            except:
                return render(request, 'index.html',{"msg":"something went wrong try again"})    
    else:
        try:
            logid=request.session['logdata']
            movies=Movies2.objects.filter(user=logid)
            moviez=Movies2.objects.all()
            print(movies)
            obj=Item.objects.all()
            return render(request, 'index.html',{"movie":movies,"video":obj,"movie":moviez})
        except:
            return render(request, 'login.html',{'msg':"you must be logged in"})   




def details(request, id):
    try:
        logid=request.session['logdata']
        movies=Movies2.objects.filter(id=id)
        return render(request, 'details.html',{"movie":movies})
    except:
        return render(request, 'login.html',{'msg':"you must be logged in"})   
def login(request):
        if request.method=="POST":
            try:
                username=request.POST['email']
                password=request.POST['password']
                logindata=LoginDetails.objects.get(username=username,password=password)
                request.session['logdata']=logindata.id
                return redirect("/moviestreet/pro2")
            except:
                return render(request, 'login.html',{'msg':"Invalid username or Password"})    
        else:
            return render (request, 'login.html') 
            
    
def register(request):
    if request.method=='POST':
        try:
            firstName=request.POST['firstname']
            lastName=request.POST['lastname']
            dateOfBirth=request.POST['dateofbirth']
            username=request.POST['emailid']
            password=request.POST['password']
            confirmPassword=request.POST['confirmPassword']
            phone=request.POST['phonenumber']
            logobj=LoginDetails(username=username,password=password)
            logobj.save()
            registerobj=Register(firstName=firstName,lastName=lastName,dateOfBirth=dateOfBirth,confirmPassword=confirmPassword,phone=phone,user=logobj)
            registerobj.save()
            return render(request, 'login.html',{'rgstr':"ACCOUNT CREATED SUCCESSFULLY LOGIN NOW" })
        except:
            return render(request, 'login.html',{'msge':"something went error try again" })    
    else:

        return render(request, 'registration.html')     

def index2(request):
     if request.method=="POST":
        name=request.POST['name']
        dir=request.POST['director']
        cast=request.POST['cast']
        desc=request.POST['description']
        release=request.POST['release']
        rating=request.POST['rating']
        img=request.FILES['images']
        logid=request.session['logdata']
        moviesobj=Movies2(name=name,director=dir,cast=cast,description=desc,releasedate=release,rating=rating,image=img,user_id=logid)
        moviesobj.save()
        movies=Movies2.objects.filter(id=logid)
        obj=Item.objects.all()
        return redirect("/moviestreet/pro2")
     else:
         try:
            logid=request.session['logdata']
            movies=Movies2.objects.filter(user=logid)
            moviez=Movies2.objects.all()
            print(movies)
            obj=Item.objects.all()
            return render(request, 'index2.html',{"movie":movies,"video":obj,"movie":moviez})
         except:
              return render(request, 'login.html',{'msg':"you must be logged in"})   

# def edit(request,id):
#     if request.method=="POST":
        
#         # namee=request.POST['']
#         name=request.POST.get('Name')
#         print("working....")
#         dirctr=request.POST.get('Dir')
#         cast=request.POST.get('cast')
#         desc=request.POST.get('description')
#         release=request.POST.get('release')
#         rating=request.POST.get('rating')
#         img=request.FILES.get('images')
#         logid=request.session['logdata']
#         moviesobj=Movies2.objects.filter(user=logid)
#         moviesobj.name=name
#         moviesobj.director=dirctr
#         moviesobj.cast=cast
#         moviesobj.description=desc
#         moviesobj.save()
       
       
   
        
#         return redirect("/moviestreet/pro6")
#     else:

#         logid=request.session['logdata']
#         movies=Movies2.objects.filter(id=id)
#         return render(request, 'edit.html',{"movie":movies})
def account(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        date=request.POST['dateofbirth']
        cp=request.POST['confirmpasswrd']
        
        mob=request.POST['phonenumber']
        logid=request.session['logdata']
        user=Register.objects.get(user=logid)
        # for u in user:

        user.firstName=firstname
        user.lastName=lastname
        user.dateOfBirth=date
        user.confirmPassword=cp
        user.phone=mob
        user.save()
        
        # logid=request.session['logdata']
        email=LoginDetails.objects.get(id=logid)
        movies=Movies2.objects.filter(user=logid)    # movies=Movies2.objects.filter(user=logid)
        return render(request, 'account.html',{"movie":movies,"user":user,"email":email}) 
        # try:
        #     # userdetails=Register.objects.get(user=logid)
          
        # except:

        #     return redirect("/moviestreet/pro7")    
    else:
        try:
            logid=request.session['logdata']
            movies=Movies2.objects.filter(user=logid)
            userdetails=Register.objects.get(user=logid)
            email=LoginDetails.objects.get(id=logid)
            return render(request, 'account.html',{"movie":movies,"user":userdetails,"email":email})    
        except:
            return render(request, 'login.html',{'msg':"you must be logged in"})    

def yourpost(request):
    try:
 
        logid=request.session['logdata']
        movies=Movies2.objects.filter(user=logid)

        return render(request, 'accountpost.html',{"movie":movies})
    except:
        return render(request, 'login.html',{'msg':"you must be logged in"})     
def details_Post(request, id):
    try:
        logid=request.session['logdata']
        movies=Movies2.objects.filter(id=id)
        return render(request, 'details2.html',{"movie":movies})
    except:
        return render(request, 'login.html',{'msg':"you must be logged in"})     

def edit_post(request, id):
    if request.method=="POST":
        try:

        
            name=request.POST.get('name')
         
            dirctr=request.POST.get('director')
            print("working....")
            cast=request.POST.get('cast')
            desc=request.POST.get('description')
            print("not workinat")
            release=request.POST.get('release')
            rating=request.POST.get('rating')

            # img=request.FILES['images']
            print('its okay')
            moviesobj=Movies2.objects.get(id=id)
            moviesobj.name=name
            print('wrkng')
            print(moviesobj.name)
            moviesobj.director=dirctr
            moviesobj.cast=cast
            moviesobj.description=desc
            moviesobj.releasedate=release
            moviesobj.rating=rating
            # moviesobj.image=img
            moviesobj.save()
            print(moviesobj)
            if 'images' in request.FILES:
                img=request.FILES['images']
            
                moviesobj=Movies2.objects.get(id=id)
                moviesobj.image=img
                moviesobj.save()
                return render(request, 'details2.html',{"movie":moviesobj})
            return render(request, 'details2.html',{"movie":moviesobj})

           
        except:                            
        
            movies=Movies2.objects.filter(id=id)
            return render(request, 'details2.html',{"movie":movies})

      
        
    else:
        try:
            logid=request.session['logdata']
            movies=Movies2.objects.filter(id=id)
            return render(request, 'edit.html',{"movie":movies})
        except:
            return render(request, 'login.html',{'msg':"you must be logged in"})    


       

def delete_post(request, id):
    if request.method=="POST":
        movies=Movies2.objects.filter(id=id) 
        movies.delete()
        return redirect("/moviestreet/pro8")       
    else:
        try:
            return redirect("/moviestreet/pro8")
        except:
            return render(request, 'login.html',{'msg':"you must be logged in"})    
def home(request):
    movie=request.GET.get("name")
   
    if movie:
        movies=Movies2.objects.filter(name__icontains=movie)
        obj=Item.objects.all() 
        return render(request, 'home.html',{"movie":movies,"video":obj}) 

    else:

        movies=Movies2.objects.all()    
        obj=Item.objects.all()
        return render(request, 'home.html',{"movie":movies,"video":obj})    

def details_2(request, id):
    
    movies=Movies2.objects.filter(id=id)
    return render(request, 'details_2.html',{"movie":movies})

def account_edit(request):
    logid=request.session['logdata']
    movies=Movies2.objects.filter(user=logid)
    userdetails=Register.objects.filter(user=logid).first()
    email=LoginDetails.objects.get(id=logid)
    return render(request, 'account.html',{"movie":movies,"user":userdetails,"email":email})




def loginOut(request):
    del request.session['logdata']
    
    return redirect('/moviestreet/pro4') 
def checkusername(request):
    username=request.GET['user']
    print(username)
    check=LoginDetails.objects.filter(username=username).exists()
    print(check)
    if check:
        return JsonResponse({"check":'exist'})
    else:
        return JsonResponse({"check":"not exist"})