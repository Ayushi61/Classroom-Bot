from django.shortcuts import render
from .models import User
# import pymysql
#import mysqlclient
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from django.shortcuts import redirect

def welcomePage(req):
    return render(req, 'welcomePage.html')
def login(req):
    #mysql.connector.connect
    connect = mysql.connector.connect(host="localhost", user = "root", password = "TDpatel@31164TDP4", database = "adminlogin", auth_plugin='mysql_native_password')
    cursor = connect.cursor()
    connect2 = mysql.connector.connect(host="localhost", user = "root", password = "TDpatel@31164TDP4", database = "adminlogin", auth_plugin='mysql_native_password')
    cursor2 = connect2.cursor()

    sqlCommand1 = "select email from adminlogin_user"
    sqlCommand2 = "select password from adminlogin_user"
    cursor.execute(sqlCommand1)
    cursor2.execute(sqlCommand2)
    e = []
    p = []

    for i in cursor:
        e.append(i)
    for i in cursor2:
        p.append(i)

    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))

    if req.method == "POST":
        email = req.POST['email']
        password = req.POST['password']
        i=1
        k = len(res)
        while i <k:
            if res[i]==email and res2[i]==password:
                return render(req,'nextpage.html',{'email':email})
                break
            i+=1
        else:
            messages.info(req,"Check username or password")
            return redirect('login')
    
    return render(req, 'login.html')
def register(req):
    user = User()
    if req.method == "POST":
        user.fname = req.POST['fname']
        user.lname= req.POST['lname']
        user.email= req.POST['email']
        user.password= req.POST['password']
        user.confirm_password= req.POST['confirm_password']
        if user.password != user.confirm_password:
            return redirect('register')
        elif user.fname == "" or user.password == "" or user.email == "" or user.lname == "" or user.confirm_password == "":
            messages.info(req, 'Some fields are empty')
            return redirect('register')
        else:
            user.save()

    return render(req, 'register.html')