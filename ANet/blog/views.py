#-*-coding:utf8-*-
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django import forms
from blog.models import Posts
from django.contrib.auth.models import User

'''自定义注册表单'''
class regForm(forms.Form):
	username = forms.CharField(label=u'用户名')
	password = forms.CharField(widget=forms.PasswordInput, label=u'密码')

'''注册用户信息'''
class userInfoForm(forms.Form):
	#username = forms.CharField()
	#password = forms.CharField(widget=forms.PasswordInput)
	first_name = forms.CharField(required=False,label=u'姓氏')
	last_name = forms.CharField(required=False, label=u'名称')
	email = forms.EmailField(required=False, label=u'邮件')


'''注册页面'''
def register(request):
	if request.method == 'POST':
		rf = regForm(request.POST)
		if rf.is_valid():
			username = rf.cleaned_data['username']
			password = rf.cleaned_data['password']

			if User.objects.all().filter(username__exact=username):
				return HttpResponse(u'用户已经存在')
			else:
				request.session['username'] = username
				User.objects.create_user(username=username,password=password)
				return HttpResponseRedirect('/blog/')
	else:
		rf = regForm()

	return render_to_response('login.html',{'rf': rf})

'''注册用户完善个人信息'''
def userinfo(request):
	if request.method == "POST":
		uif = userInfoForm(request.POST)
		username = request.session.get('username', '')
		if uif.is_valid():
			#username = uif.cleaned_data['username']
			#password = uif.cleaned_data['password']
			first_name = uif.cleaned_data['first_name']
			last_name = uif.cleaned_data['last_name']
			email = uif.cleaned_data['email']

			user = User.objects.all().filter(username__exact=username)
			user.update(first_name=first_name, last_name=last_name, email=email)

			return HttpResponse(u'用户信息更新完成')
	else:
		username = request.session.get('username', '')
		uif = userInfoForm()
		#uif.username = username

	return render_to_response('userinfo.html', {'uif': uif,'username': username})


'''blog首页处理'''
def blog(request):
	username_boolean = False
	posts = Posts.objects.all()
	username = request.session.get('username', u'路人甲')
	if username == u'路人甲':
		username_boolean = True
	return render_to_response('index.html', {'posts': posts,'username':username,'username_boolean': username_boolean})

def logout(request):
	del request.session['username']
	return HttpResponseRedirect('/register/')
