from django.db import models
from Mooding.mainapp.models import Cafe
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def home(req):
    cafe_objects = Cafe.objects.all()
    return render(req, '#', {'data' : cafe_objects})

def cafe_create(req):
    if req.mathod == 'POST':
        cafe_object = Cafe()
        cafe_object.title = req.POST['title']
        cafe_object.explanation = req.POST['explanation']
        cafe_object.reservation_available = req.POST['reservation']
        cafe_object.charge_available = req.POST['charge']
        cafe_object.total_seats = req.POST['total_seats']
        cafe_object.congestion_status = req.POST['congestion_status']
        # 위치랑 경도 받아오는 거 작업하기.
        cafe_object.thumbnail = req.POST['thumbnail']
        cafe_object.save()
        return redirect('/cafe/'+str(cafe_object.id))
    return render(req, 'cafe_create.html')

def cafe_read(req, id):
    cafe_object = get_object_or_404(Cafe, pk=id)
    reviews = cafe_object.review_set.all()
    content = {
        'data' : cafe_object,
        'reviews' :  reviews,
    }
    return render(req, 'cafe.html', content)

def cafe_edit(req, id):
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
        cafe_object.thumbnail = req.POST['thumbnail']
        cafe_object.save()
        cafe_object.save()
        return redirect('/cafe/'+str(id))
    return render(req, 'cafe_edit.html', {'data' : cafe_object})

def cafe_delete(req, id):
    cafe_object = get_object_or_404(Cafe, pk=id)
    cafe_object.delete()
    return redirect('/')

def create_reivew(req, id):
    if req.method == 'POST':
        cafe_object = get_object_or_404(Cafe, pk=id)
        user = User.objects.get(user=req.user)
        cafe_object.reivew_set.create(rating = req.POST['rating'], comment = req.POST['comment'])
        #여기서 회원 닉네임 가져오는 거 추가해서 처리하기
    return redirect('/cafe/'+ str(id))