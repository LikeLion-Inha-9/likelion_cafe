	
from django.shortcuts import redirect, render
from django.contrib import auth
from .models import CustomUser
 
def signup_view(request):
	res_data = {}
	if request.method =='POST':
		if request.POST['password1'] == request.POST['password2']:
			user = CustomUser.objects.create_user(
				username = request.POST['username'], 
				password=request.POST['password1'], 
				nickname= request.POST['nickname']
			)
			auth.login(request, user)
			return redirect('home')
		else:
			res_data['error'] = '비밀번호가 다릅니다.'
	return render(request, 'signup.html', res_data)

    	
def login_view(request):
	res_data = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			res_data['error'] = '아이디나 비밀번호가 틀렸어요~'
	return render(request, 'login.html', res_data)
    
    
#로그아웃
def logout_view(request):
	auth.logout(request)
	return redirect('home')