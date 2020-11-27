from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import  render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template import Template,loader
#from rest_framework.decorators import api_view
from django.db.models import Q

def Home(request):
	temp=loader.get_template('first.html')
	context={}
	return HttpResponse(temp.render(context,request))

def register(request):
	email=request.POST.get('txt_username')
	chk_email_exist=Login.objects.filter(username=email).exists()
	print(chk_email_exist)
	flag=0
	template=loader.get_template('first.html')
	context={}
	try:
		if chk_email_exist==False:
			fname=request.POST.get('f_name')
			lname=request.POST.get('l_name')
			a_ge=request.POST.get('age')
			g=request.POST.get('gender')
			m1=request.POST.get('mobile_1')
			option=request.POST.get('option')
			ad=request.POST.get('address')
			cty=request.POST.get('city')
			contry=request.POST.get('country')
			lction=request.POST.get('location')
			username=request.POST.get('txt_username')
			password=request.POST.get('txt_password')
			context={}
			template=loader.get_template('second.html')
			print("fname",fname)
			print("lname",lname)
			print("a_ge",a_ge)
			print("gender",g)
			print("mobile1",m1)
			print("option",option)
			print("address",ad)
			print("city",cty)
			print("country",contry)
			print("location",lction)
			print("username",username)
			print("password",password)
			obj=Login(username=username,password=password,option=option)
			obj.save()
			print('login id',obj.id)
			if obj.id>0:
				flag=flag+1
				obju=Registeruser(firstname=fname,lastname=lname,age=a_ge,gender=g,mobile1=m1,
					option=option,address=ad,city=cty,country=contry,location=lction,login=obj)
				obju.save()
				if obju.id>0:
					flag=flag+1
	except Exception as e:
         template=loader.get_template('first.html')
         context={'msg':'something went wrong'}
         print("This is the error")
         print(str(e))
	if flag==0:
		template=loader.get_template('second.html')
		context={'name':'successfull'}
	return HttpResponse(template.render(context,request))	
def loginuser(request):
	username=request.POST.get('txt_username')
	password=request.POST.get('txt_password')
	template=loader.get_template('first.html')
	print(username)
	print(password)
	chk_email_exist=Login.objects.filter(username=username).exists()
	print(chk_email_exist)
	if chk_email_exist:
		obj_login=Login.objects.get(username=username)
		if(obj_login.username==username and obj_login.password==password):
			request.session['uid']=obj_login.id
			template=loader.get_template('third.html')
			context={'name':obj_login.username}
			#template=loader.get_template('third.html')
			#context={}
			idd=request.session['uid']
			print(idd)
			dat=Registeruser.objects.get(login_id=idd)
			print("njnjnj")
			print(dat.firstname)
			fname=dat.firstname
			lname=dat.lastname
			a_ge=dat.age
			g=dat.gender
			m1=dat.mobile1
			m2=dat.mobile2
			ad=dat.address
			cty=dat.city
			contry=dat.country
			lction=dat.location
			dat.save()
			print(dat.gender)
			context={"fname":fname,"lname":lname,"age":a_ge,"gender":g,"mobile1":m1,
			"mobile2":m2,"address":ad,"city":cty,"country":contry,"location":lction}
			return HttpResponse(template.render(context,request))
		elif(obj_login.password!=password):
			template=loader.get_template('wrong password.html')
			context={'Msg':'password incorrect'}
	else:
		template=loader.get_template('wrong username.html')
		context={'Msg':'username does not exists'}
	return HttpResponse(template.render(context,request))

def tenant(request):
	template=loader.get_template('third.html')
	context={}
	if(request.method=="POST"):
		myid=request.session['uid']
		print("myid",myid)
		na=request.POST.get('f_name')
		sn=request.POST.get('l_name')
		ag=request.POST.get('age')
		gr=request.POST.get('gender')
		mob1=request.POST.get('mobile_1')
		opt=request.POST.get('option')
		addrs=request.POST.get('address')
		cy=request.POST.get('city')
		ctry=request.POST.get('country')
		ltion=request.POST.get('location')
		print('##########')
		ob=Registeruser.objects.get(login_id=myid)
		ob.firstname=na
		ob.lastname=sn
		ob.age=ag
		ob.mobile1=mob1
		ob.mobile2=opt
		ob.gender=gr
		ob.address=addrs
		ob.city=cy
		ob.country=ctry
		ob.location=ltion
		ob.save()
		context={"fname":na,"lname":sn,"age":ag,"gender":gr,"mobile1":mob1,"option":opt,
		"address":addrs,"city":cy,"country":ctry,"location":ltion}	
		return HttpResponse(template.render(context,request))

	return HttpResponse(template.render(context,request))

def deleteuser(request):
	template=loader.get_template('first.html')
	try:
		myid=request.session['uid']
		obj_login = Login.objects.get(id = myid)
		obj_login.delete()
		obj_user=Registeruser.objects.get(login_id=myid)
		obj_user.delete()
		
	except Exception as e:
		#return HttpResponse("user deleted")
		context={}
		return HttpResponse(template.render(context,request))

