from django.shortcuts import render
import pyrebase
from firebase import firebase
import os
import os.path
from django.contrib import auth
import time
from datetime import datetime
from datetime import timezone
import datetime
import pytz
from django.http import HttpResponse
from django.contrib import messages
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('./whitef-data-b8eff.json')

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

config = { 
    "apiKey": "AIzaSyCvY5jMuYXAwUviHG_MgZVdObauFMCx08I",
    "databaseURL": "https://whitef-data-b8eff-default-rtdb.europe-west1.firebasedatabase.app",  
    "authDomain": "whitef-data-b8eff.firebaseapp.com",
    "projectId": "whitef-data-b8eff",
    "storageBucket": "whitef-data-b8eff.appspot.com",
    "messagingSenderId": "125886529819",
    "serviceAccount": "./whitef-data-b8eff.json",
    "appId": "1:125886529819:web:53f13806b2596b227413be"
}

# os.environ['GOOGLE_APLICATION_CREDENTIALS'] = './whitef-data-b8eff.json'
# os.environ['GOOGLE_CLOUD_PROJECT'] = 'whitef-data'

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
# auth = firebase.auth()
storage = firebase.storage()


def home(request):
    return render(request, 'whitefreport/main.html')

def signin(request):
    return render(request, 'whitefreport/signin.html')

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:    
        user = authe.sign_in_with_email_and_password(email, passw)
    # except:
    #     message=("invalid credentials")
    #     return render(request, 'whitefreport/main.html', {'messg':message})
        print(user['localId'])
      
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        
        idtoken = request.session["uid"]
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        # print(user['idToken'])
       
        name = database.child('users').child(a).child('details').child('name').get().val()
        messages.success(request, "You are successfully loged in as User:")
        print(name)    
        return render(request, 'whitefreport/welcome.html', {'e':name})
               
    except:
        message=("Invalid credentials")
        return render(request, 'whitefreport/signin.html', {'messg':message})
      
def logout(request):
    # auth.logout(request)
    try:
      del request.session['uid']
    except KeyError: 
        pass
    return render (request, "whitefreport/signin.html") 

def signUp(request):
    return render(request, 'whitefreport/signup.html')

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.create_user_with_email_and_password(email, passw)
        # authe.send_email_verification(user['idToken'])
    except:
        message = "Credentials are not properly set" 
        return render(request, 'whitefreport/signup.html', {'messg':message})
    uid = user['localId']

    data = {"name":name,"status":email}
    
    database.child("users").child(uid).child("details").set(data)
    return render(request, "whitefreport/main.html")

def create(request):
    idtoken = request.session["uid"]
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, 'whitefreport/create.html',{'e':name})

def post_create(request):
    tz = pytz.timezone('Europe/London')
    time_now = datetime.datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili"+str(millis)) 
    make = request.POST.get('make')
    task = request.POST.get('task')
    work = request.POST.get('work')
    progress = request.POST.get('progress')
    url = request.POST.get('url')
    try:
        idtoken = request.session["uid"]
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print("info"+str(a))
        data = {
            "make": make,
            "task": task,
            "work": work,
            "progress": progress,
            "url": url
            }
            
        database.child('users').child(a).child('reports').child(millis).set(data)
        messages.success(request, "Report successfully submited! ")
        name = database.child('users').child(a).child('details').child('name').get().val()
        return render(request,"whitefreport/welcome.html",{'e':name})
    except KeyError:
        message=("Oooops! User logged out Please Sign in again")
        return render(request, 'whitefreport/signin.html', {'messg':message})

def check(request):
    if request.method == 'GET' and 'csrfmiddlewaretoken' in request.GET:
        search = request.GET.get('search')
        search = search.lower()
        uid = request.GET.get('uid')
        print(search)
        print(uid)
        return HttpResponse("got it")
        # timestamps = database.child('users').child(uid).child('reports').shallow().get().val()

        # work_id=[]
        # for i in timestamps:
        #     wor = database.child('users').child(uid).child('reports').child(i).child('work').get().val()
        #     wor = str(wor)+"$"+str(i)
        #     work_id.append(wor)
        #     matching = [str(string) for string in work_id if search in string.lower()]
        #     s_work=[]
        #     s_id=[]
                
        # for i in matching:
        #     work, ids = i.split('$')
        #     s_work.append(work)
        #     s_id.append(ids)
        #     date = []
        # for i in s_id:
        #     i = float(i)
        #     dat = datetime.datetime.fromtimestamp(i).strftime('%a %d %B %y / %H:%M')
        #     date.append(dat)
        # comb_lis = zip(s_id, date, s_work)
        # name = database.child('users').child(uid).child('details').child('name').get().val()
        # return render(request, 'whitefreport/check.html', {'comb_lis': comb_lis, 'e': name, 'uid': uid})
        
    else:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
    
        timestamps = database.child('users').child(a).child('reports').shallow().get().val()
        
        lis_time = []

        for i in timestamps:
            lis_time.append(i)
        lis_time.sort(reverse=True)
        # print(lis_time)

        make = []
        for i in lis_time:
            mak = database.child('users').child(a).child('reports').child(i).child('make').get().val()
            make.append(mak)
        # print(task)

        task = []
        for i in lis_time:
            tsk = database.child('users').child(a).child('reports').child(i).child('task').get().val()
            task.append(tsk)
        # print(task)
        
        work = []
        for i in lis_time:
            wor = database.child('users').child(a).child('reports').child(i).child('work').get().val()
            work.append(wor)
        # print(work)
            
        date = []
        for i in lis_time:
            i = float(i)
            dat = datetime.datetime.fromtimestamp(i).strftime('%a %d %B %y / %H:%M')
            date.append(dat)
        # print(date)

        comb_lis = zip(lis_time,date,work,task,make)
        name = database.child('users').child(a).child('details').child('name').get().val()
       
        return render(request,"whitefreport/check.html",{'comb_lis':comb_lis,'e':name, 'uid':a})       
    
def post_check(request):
    time = request.GET.get(str('z'))
    if time is None or time == '':
       
        return HttpResponse("Parameter 'z' is missing or empty", status=400)
    
    try:
        i = float(time)
    except ValueError:
        return HttpResponse("Parameter 'z' is not a valid number", status=400)

    idtoken = request.session["uid"]
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    make = database.child('users').child(a).child('reports').child(time).child('make').get().val()
    task = database.child('users').child(a).child('reports').child(time).child('task').get().val()
    work = database.child('users').child(a).child('reports').child(time).child('work').get().val()
    progress = database.child('users').child(a).child('reports').child(time).child('progress').get().val()
    img_url = database.child('users').child(a).child('reports').child(time).child('url').get().val()
    item_id = database.child('users').child(a).child('reports').child(time).get().key()
    print(img_url)
    i = float(time)
    dat = datetime.datetime.fromtimestamp(i).strftime('%A %d - %B -  %Y / %H:%M')
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request,"whitefreport/post_check.html",{'hr':make, 't':task,'w':work,'p':progress, 'd':dat, 'e':name, 'i':img_url, 'm':item_id, 'uid':a})

# people = database.child('users').child('reports').child('work').get().val()
# print(people)
