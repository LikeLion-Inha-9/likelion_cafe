from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Cafe(models.Model): # 카페 클래스
    id = models.AutoField(primary_key=True) # 카페 아이디
    title = models.CharField(max_length=100) # 카페이름
    explanation = models.TextField() # 카페 설명
    reservation_available = models.BooleanField() #예약 가능여부
    charge_available = models.BooleanField() # 충전 가능 여부
    total_seats = models.SmallIntegerField() # 총 좌석 수
    used_seats = models.SmallIntegerField() # 사용하고 있는 좌석 수
    unused_seats = models.SmallIntegerField() # 미사용 좌석 수
    congestion_status = models.SmallIntegerField() # 혼잡여부(숫자료 표현 0, 1, 2)
    lat = models.SmallIntegerField() #위도
    lng = models.SmallIntegerField() #경도
    thumbnail = models.ImageField(default ="#") #썸네일 이미지


class Review(models.Model): # 리뷰 서비스
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE) # 카페 하나에 종속
    writer = models.CharField(max_length=20)# 작성자
    rating = models.SmallIntegerField() # 별점
    comment = models.TextField() #리뷰내용


class Product(models.Model): #판매할 상품
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE) # 카페 하나에 종속
    title = models.CharField(max_length=100) #상품 이름
    price = models.IntegerField() # 상품가격
    out_of_stock = models.BooleanField() # 매진여부


class Image(models.Model): # 이미지 
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE) #카페 종속
    representative_image = models.ImageField() #카페 대표 이미지