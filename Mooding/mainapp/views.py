
from django.db import models
from Mooding.mainapp.models import *
from django.contrib import auth
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def home(req): # 메인화면 로딩할때 사용
    cafe_objects = Cafe.objects.all()
    return render(req, '#', {'data' : cafe_objects})

##################################카페 CRUD######################################


def cafe_create(req): #카페 생성
    if req.mathod == 'POST':
        cafe_object = Cafe()
        cafe_object.title = req.POST['title']
        cafe_object.explanation = req.POST['explanation']
        cafe_object.reservation_available = req.POST['reservation']
        cafe_object.charge_available = req.POST['charge']
        cafe_object.total_seats = req.POST['total_seats']
        cafe_object.congestion_status = req.POST['congestion_status']
        # 위치랑 경도 받아오는 거 작업하기.(네이버 지도)
        cafe_object.thumbnail = req.POST['thumbnail']
        cafe_object.close_day = req.POST['close_day']
        cafe_object.cafe_phone_number = req.POST['phone_number']
        cafe_object.save()
        for img in req.FILES.getlist('#'): #여기에 이미지파일 받는 name 넣기
            photo = Image()
            photo.cafe = cafe_object
            photo.representative_image = img
            photo.save()
        return redirect('/cafe/'+str(cafe_object.id))
    return render(req, 'cafe_create.html')


def cafe_read(req, id): #카페 읽어오기

    cafe_object = get_object_or_404(Cafe, pk=id)
    reviews = cafe_object.review_set.all()
    content = {
        'data' : cafe_object,
        'reviews' :  reviews,
    }
    return render(req, 'cafe.html', content)

def cafe_edit(req, id):  #카페 내용 수정
    cafe_object = get_object_or_404(Cafe, pk=id)
    if req.mathod == 'POST':
        cafe_object = Cafe()
        cafe_object.title = req.POST['title']
        cafe_object.explanation = req.POST['explanation']
        cafe_object.reservation_available = req.POST['reservation']
        cafe_object.charge_available = req.POST['charge']
        cafe_object.total_seats = req.POST['total_seats']
        cafe_object.congestion_status = req.POST['congestion_status']
        # 위치랑 경도 받아오는 거 작업하기.
        cafe_object.operating_hour = req.POST['operating_hour']
        
        cafe_object.thumbnail = req.POST['thumbnail']
        cafe_object.save()
        return redirect('/cafe/'+str(id))
    return render(req, 'cafe_edit.html', {'data' : cafe_object})

def cafe_delete(req, id): #카페 삭제
    cafe_object = get_object_or_404(Cafe, pk=id)
    cafe_object.delete()
    return redirect('/')



##################################리뷰 CRUD######################################

def reivew_create(req, id):
    if req.method == 'POST':
        cafe_object = get_object_or_404(Cafe, pk=id)
        #user = User.objects.get(user=req.user)
        user = CustomUser.objects.get(user=req.user)
        cafe_object.reivew_set.create(writer = user.nickname, rating = req.POST['rating'], comment = req.POST['comment'])
        #여기서 회원 닉네임 가져오는 거 추가해서 처리하기
    return redirect('/cafe/'+ str(id))

def review_delete(req,id):
    review_object = get_object_or_404(Review, pk=id)
    review_object.delete()
    return redirect('/')

def review_modify(req, id):
    review_object = get_object_or_404(Review, pk=id)
    user = CustomUser.objects.get(user=req.user)
    if req.mathod == 'POST':
        review_object = Review()
        review_object.writer = user.nickname
        review_object.rating = req.POST['rating']
        review_object.comment = req.POST['comment']
        #return redirect('/cafe/'+str(id))
    #return render(req, 'cafe_edit.html', {'data' : cafe_object})

##################################쿠폰관련#############################

    def coupon_create(req,id):
        coupon_object = Coupon()
        coupon_object.user = req.user
        coupon_object.cafe = Cafe.objects.filter(id=id)
        coupon_object.save
        
    def coupon_stamping(req, id):
        user_object = req.user
        cafe_object = Cafe.objects.filter(id=id)
        coupon_object = Coupon.objects.filter(user=user_object, cafe = cafe_object)
        coupon_object.stamp += 1
        if coupon_object.stamp == 12:
            coupon_object.free_coupon += 1
            coupon_object.stamp = 0

    def coupon_getPrize(req,id):
        user_object = req.user
        cafe_object = Cafe.objects.filter(id=id)
        coupon_object = Coupon.objects.filter(user=user_object, cafe = cafe_object)
        if coupon_object.free >= 1:
            coupon_object.free_coupon -= 1

#################################로그인 관련############################
 
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